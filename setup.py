#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from jsonsuit/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("jsonsuit", "__init__.py")


def convert_md_to_rst(filename):
    try:
       import pypandoc
       rst = pypandoc.convert_file('{}.md'.format(filename), 'rst')
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
requirements = open('requirements.txt').readlines()

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
    install_requires=requirements,
    python_requires='>=3.9',
    license="MIT",
    zip_safe=False,
    keywords=['django-jsonsuit', 'django', 'json', 'suit'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
