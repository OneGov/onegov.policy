from onegov.policy.testing import GERMAN_BUNDLE_LAYER
from onegov.policy.tests.test_bundle_english import TestBundleEnglish


class TestBundleGerman(TestBundleEnglish):

    layer = GERMAN_BUNDLE_LAYER

    translations = {
        'workplace': 'arbeitsplatz',
        'Workplace': 'Arbeitsplatz',
        'Workspaces': u'Arbeitsr\xe4ume',
        'workspaces': 'arbeitsraeume'
        }
