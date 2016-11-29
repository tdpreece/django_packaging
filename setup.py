from setuptools import setup, find_packages


setup(
    name="django_package_example",
    version="0.0.1",
    install_requires=('django>=1.4,<1.10'),
    package_dir={'': 'src'},
    packages=find_packages('src'),
)
