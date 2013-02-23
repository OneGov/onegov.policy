from onegov.policy.testing import GERMAN_BUNDLE_INTEGRATION
from onegov.policy.tests.test_bundle_english import TestBundleEnglish


class TestBundleGerman(TestBundleEnglish):

    layer = GERMAN_BUNDLE_INTEGRATION

    translations = {
        'workplace': 'arbeitsplatz',
        'Workplace': 'Arbeitsplatz',
        'Workspaces': u'Arbeitsr\xe4ume',
        'workspaces': 'arbeitsraeume',
        'library': 'bibliothek',
        'Library': 'Bibliothek',
        }
