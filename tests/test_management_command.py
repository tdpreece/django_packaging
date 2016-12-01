from django.core.management import call_command
from django.test import TestCase


from django_package_example.models import Person


class TestManagementCommand(TestCase):
    def test(self):
        Person.objects.create(first_name='Tim', last_name='Preece', age='1')
        call_command('age')
        p = Person.objects.get(first_name='Tim')
        self.assertEqual(p.age, 2)
