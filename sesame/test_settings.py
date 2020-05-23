from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings

from . import settings
from .test_signals import reset_sesame_settings  # noqa


class TestSettings(TestCase):
    @override_settings(SESAME_INVALIDATE_ON_PASSWORD_CHANGE=False, SESAME_MAX_AGE=None)
    def test_insecure_configuration(self):
        with self.assertRaises(ImproperlyConfigured) as exc:
            settings.check()
        self.assertEqual(
            str(exc.exception),
            "Insecure configuration: set SESAME_MAX_AGE to a low value "
            "or set SESAME_INVALIDATE_ON_PASSWORD_CHANGE to True",
        )
