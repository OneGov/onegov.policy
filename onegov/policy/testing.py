from ftw.inflator.bundle import get_bundle_by_name
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_SITE_ID
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import TEST_USER_ROLES
from plone.app.testing.layers import PloneFixture
from plone.testing import Layer
from plone.testing import z2
from plone.testing import zodb
from zope.configuration import xmlconfig


def clear_transmogrifier_registry():
    # reset transmogrifier registry when setting up, so that
    # we can re-register blueprints using ZCML.
    from collective.transmogrifier import transmogrifier
    # pylint: disable=W0212
    transmogrifier.configuration_registry._config_info = {}
    transmogrifier.configuration_registry._config_ids = []
    # pylint: enable=W0212


class OneGovFixture(PloneFixture):

    def setUpProducts(self, app):
        super(OneGovFixture, self).setUpProducts(app)
        configurationContext = self['configurationContext']

        # Plone < 4.3
        import Products.GenericSetup
        xmlconfig.file('meta.zcml', Products.GenericSetup,
                       context=configurationContext)

        import Products.Five
        xmlconfig.file('meta.zcml', Products.Five,
                       context=configurationContext)

        # Auto-include all Plone addon ZCMLs
        import z3c.autoinclude
        xmlconfig.file('meta.zcml', z3c.autoinclude,
                       context=configurationContext)
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <includePlugins package="plone" />'
            '</configure>',
            context=configurationContext)

        # intitialize packages
        z2.installProduct(app, 'Products.CMFPlacefulWorkflow')
        z2.installProduct(app, 'ftw.billboard')
        z2.installProduct(app, 'ftw.blog')
        z2.installProduct(app, 'ftw.book')
        z2.installProduct(app, 'ftw.contentpage')
        z2.installProduct(app, 'ftw.file')
        z2.installProduct(app, 'ftw.keywordoverlay')
        z2.installProduct(app, 'ftw.meeting')
        z2.installProduct(app, 'ftw.notification.base')
        z2.installProduct(app, 'ftw.notification.email')
        z2.installProduct(app, 'ftw.permissionmanager')
        z2.installProduct(app, 'ftw.workspace')
        z2.installProduct(app, 'ftwbook.graphicblock')
        z2.installProduct(app, 'izug.ticketbox')
        z2.installProduct(app, 'simplelayout.base')
        z2.installProduct(app, 'simplelayout.types.common')
        z2.installProduct(app, 'simplelayout.ui.base')
        z2.installProduct(app, 'simplelayout.ui.dragndrop')

    def tearDown(self):
        super(OneGovFixture, self).tearDown()
        clear_transmogrifier_registry()

    def setUpDefaultContent(self, app):
        # Do not install plone site in this base layer,
        # so that we can reuse it an setup multiple sites
        # with different languages in sequence.

        with z2.zopeApp() as app:
            app['acl_users'].userFolderAddUser(
                SITE_OWNER_NAME,
                SITE_OWNER_PASSWORD,
                ['Manager'],
                [])


ONEGOV_FIXTURE = OneGovFixture()


class BundleLayer(Layer):

    defaultBases = (ONEGOV_FIXTURE, )

    def __init__(self, language, *args, **kwargs):
        super(BundleLayer, self).__init__(*args, **kwargs)
        self.language = language

    def setUp(self):
        # Stack a new DemoStorage
        self['zodbDB'] = zodb.stackDemoStorage(
            self.get('zodbDB'), name='BundleLayer:%s' % self.language)

        with z2.zopeApp() as app:
            z2.login(app['acl_users'], SITE_OWNER_NAME)

            # instll a plone site with the bundle
            bundle = get_bundle_by_name('OneGov Box (Example content)')
            bundle.install(app, PLONE_SITE_ID, language=self.language)

            # create the plone test user
            pas = app[PLONE_SITE_ID]['acl_users']
            pas.source_users.addUser(
                    TEST_USER_ID,
                    TEST_USER_NAME,
                    TEST_USER_PASSWORD)
            for role in TEST_USER_ROLES:
                pas.portal_role_manager.doAssignRoleToPrincipal(TEST_USER_ID, role)

            z2.logout()

    def tearDown(self):
        # Zap the stacked ZODB
        self['zodbDB'].close()
        del self['zodbDB']


ENGLISH_BUNDLE_INTEGRATION = IntegrationTesting(
    bases=(BundleLayer('en'), ),
    name="onegov.policy:bundle:en")

GERMAN_BUNDLE_INTEGRATION = IntegrationTesting(
    bases=(BundleLayer('de'), ),
    name="onegov.policy:bundle:de")
