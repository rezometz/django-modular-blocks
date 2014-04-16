from setuptools import setup, find_packages

import os

modular_blocks = __import__('modular_blocks')


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
       'Django >= 1.5',
    ],
)
