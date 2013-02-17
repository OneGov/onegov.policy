#!/usr/bin/env python

from json import load
import os
import re


DOMAIN = 'onegov.policy.contentcreation'


locales_dir = os.path.abspath(os.path.dirname(__file__))
profiles_dir = os.path.abspath(os.path.join(
        locales_dir, '..', 'profiles'))
potfile_path = os.path.join(locales_dir, '%s.pot' % DOMAIN)

TRANSLATABLE_KEY_EXPR = re.compile(
    r'^[^:]*:translate\(%s\)$' % re.escape(DOMAIN))


content_creation_files = []
for dirpath, dirnames, filenames in os.walk(profiles_dir):
    if not dirpath.rstrip('/').endswith('/content_creation'):
        continue

    content_creation_files.extend(
        map(lambda name: os.path.join(dirpath, name),
            filter(lambda name: name.endswith('.json'), filenames)))


def get_translated_values(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if TRANSLATABLE_KEY_EXPR.match(key):
                yield value
            for result in get_translated_values(value):
                yield result

    elif hasattr(data, '__iter__'):
        for value in data:
            for result in get_translated_values(value):
                yield result


msgids = set()
for jsonpath in content_creation_files:
    data = load(open(jsonpath))
    msgids.update(get_translated_values(data))


with open(potfile_path, 'w+') as potfile:
    potfile.write('\n'.join((
                r'# --- PLEASE EDIT THE LINES BELOW CORRECTLY ---',
                r'# SOME DESCRIPTIVE TITLE.',
                r'# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.',
                r'msgid ""',
                r'msgstr ""',
                r'"Project-Id-Version: PACKAGE VERSION\n"',
                r'"POT-Creation-Date: 2013-02-01 16:26+0000\n"',
                r'"PO-Revision-Date: YEAR-MO-DA HO:MI +ZONE\n"',
                r'"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"',
                r'"Language-Team: LANGUAGE <LL@li.org>\n"',
                r'"MIME-Version: 1.0\n"',
                r'"Content-Type: text/plain; charset=utf-8\n"',
                r'"Content-Transfer-Encoding: 8bit\n"',
                r'"Plural-Forms: nplurals=1; plural=0\n"',
                r'"Language-Code: en\n"',
                r'"Language-Name: English\n"',
                r'"Preferred-Encodings: utf-8 latin1\n"',
                r'"Domain: %s\n"' % DOMAIN)))

    for msgid in msgids:
        potfile.write('\n'.join((
                    '\n',
                    'msgid "%s"' % msgid,
                    'msgstr ""')))


for dirpath, dirnames, filenames in os.walk(locales_dir):
    pofiles = map(lambda name: os.path.join(dirpath, name),
                  filter(lambda name: name == '%s.po' % DOMAIN, filenames))

    for path in pofiles:
        os.system('i18ndude sync --pot %s %s' % (potfile_path, path))

        # remove language and domain from pofile because they are implicitly
        # given by path and filename and they are always english in this
        # state.

        filedata = open(path).readlines()
        with open(path, 'w+') as file_:
            for line in filedata:
                if line.startswith('"Language-'):
                    continue
                elif line.startswith('"Domain:'):
                    continue
                else:
                    file_.write(line)
