#!/usr/bin/env python3
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('seacow/metadata.py') as metadata_file:
    exec(metadata_file.read())

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
        'kxg',
]

test_requirements = [
]


setup(
    name='seacow',
    version=__version__,
    author=__author__,
    author_email=__email__,
    long_description=readme,
    url='https://github.com/alexmitchell/seacow',
    packages=[
        'seacow',
    ],
    entry_points = {
        'console_scripts': [
            'seacow=seacow:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license='GPLv3',
    zip_safe=False,
    keywords=[
        'seacow',
        'game',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Games/Entertainment',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
