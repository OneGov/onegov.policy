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

    def _workplace_inline_link_test(self, id_, label):
        browser = Browser(self.layer['app'])
        browser.handleErrors = False
        browser.addHeader('Authorization', 'Basic %s:%s' % (
                SITE_OWNER_NAME, SITE_OWNER_PASSWORD))

        portal_url = self.layer['portal'].portal_url()
        browser.open('/'.join((portal_url, self.translated('workplace'))))
        doc = PyQuery(browser.contents)

        links = doc('#content .sl-text-wrapper a')
        filtered_links = filter(
            lambda node: node.text_content() == label,
            links)

        self.assertEquals(
            len(filtered_links),
            1,
            'Expected one link "%s", but found: %s' % (
                label,
                str(map(lambda node: node.text_content(), filtered_links))))

        self.assertEquals(
            filtered_links[0].get('href'),
            '../%s' % id_,
            'Link "%s" seems to point to a wrong place.' % filtered_links[0].text_content())


    def test_workspaces_inline_link(self):
        self._workplace_inline_link_test(self.translated('workspaces'),
                                         self.translated('Workspaces'))

    def test_library_inline_link(self):
        self._workplace_inline_link_test(self.translated('library'),
                                         self.translated('Library'))

    def test_billboard_inline_link(self):
        self._workplace_inline_link_test(self.translated('billboard'),
                                         self.translated('Billboard'))

    def test_ticketbox_inline_link(self):
        self._workplace_inline_link_test(self.translated('ticketboxes'),
                                         self.translated('TicketBox'))
