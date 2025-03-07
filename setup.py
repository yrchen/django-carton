import os

from distutils.core import setup
from setuptools import find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

import carton


setup(
    name='django-carton',
    version=carton.__version__,
    description=carton.__doc__,
    packages=find_packages(),
    url='http://github.com/lazybird/django-carton/',
    author='lazybird',
    long_description=open('README.md').read(),
    include_package_data=True,
)
