from onegov.policy.testing import ENGLISH_BUNDLE_INTEGRATION
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.testing.z2 import Browser
from pyquery import PyQuery
from unittest2 import TestCase


class TestBundleEnglish(TestCase):

    layer = ENGLISH_BUNDLE_INTEGRATION

    translations = {}

    def translated(self, text):
        return self.translations.get(text, text)

    def test_site_created(self):
        self.assertTrue(self.layer['portal'])

    def test_workplace_translated(self):
        workplace = self.layer['portal'].get(self.translated('workplace'))
        self.assertTrue(workplace)
        self.assertEquals(workplace.Title(), self.translated('Workplace'))

    def test_workspaces_inline_link(self):
        browser = Browser(self.layer['app'])
        browser.handleErrors = False
        browser.addHeader('Authorization', 'Basic %s:%s' % (
                SITE_OWNER_NAME, SITE_OWNER_PASSWORD))

        portal_url = self.layer['portal'].portal_url()
        browser.open('/'.join((portal_url, self.translated('workplace'))))
        doc = PyQuery(browser.contents)

        links = doc('#content .sl-text-wrapper a')
        workspaces_links = filter(
            lambda node: node.text_content() == self.translated('Workspaces'),
            links)

        self.assertEquals(
            len(workspaces_links),
            1,
            'Expected one link "%s", but found: %s' % (
                self.translated('Workspaces'),
                str(map(lambda node: node.text_content(), links))))

        self.assertEquals(
            links[0].get('href'),
            '../%s' % self.translated('workspaces'),
            'Link "%s" seems to point to a wrong place.' % links[0].text_content())
