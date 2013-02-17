from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.testing import z2
from zope.configuration import xmlconfig


class OneGovBoxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # reset transmogrifier registry when setting up, so that
        # we can re-register blueprints using ZCML.
        from collective.transmogrifier import transmogrifier
        # pylint: disable=W0212
        transmogrifier.configuration_registry._config_info = {}
        transmogrifier.configuration_registry._config_ids = []
        # pylint: enable=W0212

        # Auto-include all Plone addon ZCMLs
        import z3c.autoinclude
        xmlconfig.file('meta.zcml', z3c.autoinclude,
                       context=configurationContext)
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <includePlugins package="plone" />'
            '</configure>',
            context=configurationContext)

        # Initialize packages
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
        z2.installProduct(app, 'ftw.poodle')
        z2.installProduct(app, 'ftw.workspace')
        z2.installProduct(app, 'ftwbook.graphicblock')
        z2.installProduct(app, 'izug.ticketbox')
        z2.installProduct(app, 'simplelayout.base')
        z2.installProduct(app, 'simplelayout.types.common')
        z2.installProduct(app, 'simplelayout.ui.base')
        z2.installProduct(app, 'simplelayout.ui.dragndrop')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'onegov.policy:default')


ONEGOV_BOX_FIXTURE = OneGovBoxLayer()
ONEGOV_BOX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ONEGOV_BOX_FIXTURE, ),
    name="onegov.policy:integration")
ONEGOV_BOX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ONEGOV_BOX_FIXTURE, ),
    name="onegov.policy:functional")
