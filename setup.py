# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.2dev0'


long_description = (
    read('README.rst')
    + '\n' +
    read('docs/HISTORY.rst')
    + '\n' +
    read('CONTRIBUTORS.rst')
    )


setup(
    name='collective.lastlogin',
    version=version,
    description="Show the list of Plone users with the last login date.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='',
    author='Zest Software',
    author_email='info@zestsoftware.nl',
    url='https://github.com/collective/collective.lastlogin.git',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )