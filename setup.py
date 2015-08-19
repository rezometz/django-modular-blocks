import os
import sys
from setuptools import setup, find_packages
from django.core import management

import os

modular_blocks = __import__('modular_blocks')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# translation files compilation
currentdir = os.getcwd()
os.chdir(os.path.join(currentdir, 'modular_blocks'))
management.call_command('compilemessages', stdout=sys.stdout)
os.chdir(currentdir)

setup(
    name='django-modular-blocks',
    packages=find_packages(),
    author='Gabriel Pichot',
    author_email='gabriel.pichot@gmail.com',
    url='https://github.com/gpichot/django-modular-blocks',
    description=(
        'Django Modular Blocks ease the integration of third'
        'parties application as blocks in a page.'
    ),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
    ],
    keywords=['modular', 'modules', ],
    install_requires=[
#       'Django == 1.6.1',
    ],
)
