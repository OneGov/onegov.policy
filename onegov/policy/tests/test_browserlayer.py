from Products.CMFCore.utils import getToolByName
from onegov.policy.interfaces import IOneGovLayer
from onegov.policy.testing import ENGLISH_BUNDLE_INTEGRATION
from plone.browserlayer.utils import registered_layers
from unittest2 import TestCase


class TestBrowserlayerInstalled(TestCase):

    layer = ENGLISH_BUNDLE_INTEGRATION

    def test_onegov_policy_profile_installed(self):
        portal = self.layer['portal']
        portal_setup = getToolByName(portal, 'portal_setup')

        version = portal_setup.getLastVersionForProfile(
            'onegov.policy:default')
        self.assertNotEqual(version, None)
        self.assertNotEqual(version, 'unknown')

    def test_request_layer_active(self):
        layers = registered_layers()
        self.assertIn(IOneGovLayer, layers)
