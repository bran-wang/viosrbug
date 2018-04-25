# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='viosrbug',
    version='0.1',
    description='',
    author='bran',
    author_email='branw@vmware.com',
    install_requires=[
        "pecan",
    ],
    test_suite='viosrbug',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)
