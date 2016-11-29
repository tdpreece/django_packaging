from django.test import TestCase

from django_package_example.models import Person


class TestModels(TestCase):
    def test(self):
        Person.objects.create(first_name='Tim', last_name='Preece')
        p = Person.objects.get(first_name='Tim')
        self.assertEqual(p.last_name, 'Preece')
