#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Managed by bumpversion
version = '0.4.1'

def convert_md_to_rst(filename):
    try:
       import pypandoc
       rst = pypandoc.convert('{}.md'.format(filename), 'rst')
    except (IOError, ImportError):
       rst = ''
    return rst


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = convert_md_to_rst('README')
history = convert_md_to_rst('HISTORY')

setup(
    name='django-jsonsuit',
    version=version,
    description="""Django goodies to dress JSON data in a suit.""",
    long_description=readme + '\n\n' + history,
    author='Marc Zimmermann',
    author_email='tooreht@gmail.com',
    url='https://github.com/tooreht/django-jsonsuit',
    packages=[
        'jsonsuit',
    ],
    include_package_data=True,
    install_requires=[
        'django>=1.8',
    ],
    license="MIT",
    zip_safe=False,
    keywords='django-jsonsuit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
