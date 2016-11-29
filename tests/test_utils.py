from django.test import TestCase

from django_package_example.utils import hello


class TestUtils(TestCase):
    def test(self):
        self.assertEqual(hello(), 'hello')
