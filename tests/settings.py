import django


SECRET_KEY = 'aAbBcC123%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    },
}

INSTALLED_APPS = (
    'django_package_example',
)

if django.VERSION[:2] < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
