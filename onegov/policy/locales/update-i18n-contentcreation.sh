#!/usr/bin/env sh

if [[ "$0" != "./update-i18n-contentcreation.sh" ]]; then
    echo "Run from onegov/policy/locales with ./update-i18n-contentcreation.sh"
    exit 1
fi

DOMAIN=onegov.policy.contentcreation
POFILENAME=${DOMAIN}.po
POTFILE=${DOMAIN}.pot

cat > $POTFILE <<EOF
# --- PLEASE EDIT THE LINES BELOW CORRECTLY ---
# SOME DESCRIPTIVE TITLE.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2013-02-01 16:26+0000\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI +ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=1; plural=0\n"
"Language-Code: en\n"
"Language-Name: English\n"
"Preferred-Encodings: utf-8 latin1\n"
"Domain: $DOMAIN\n"
EOF

for msgid in $(grep -r ":translate($DOMAIN)" ../profiles | sed -e 's/.*: "\([^"]*\)",$/\1/g'); do
    echo "" >> $POTFILE
    echo "msgid \"$msgid\"" >> $POTFILE
    echo "msgstr \"\"" >> $POTFILE
done

for pofile in $(find . -name $POFILENAME); do
    i18ndude sync --pot $POTFILE $pofile
done
