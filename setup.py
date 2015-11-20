#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="soundcloud-dl",
    version="0.1.0",
    url='https://github.com/kangfend/soundcloud-dl',
    description='Soundcloud downloader.',
    license='MIT',
    author='Sutrisno Efendi',
    author_email='kangfend@gmail.com',
    packages=find_packages(),
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
    scripts=['bin/soundcloud-dl'],
)
