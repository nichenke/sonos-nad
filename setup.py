#!/usr/bin/env python

from setuptools import setup

REQUIREMENTS = list(open('requirements.txt'))

setup(name='sonos-nad',
      version='1.0',
      description='Work with NAD-356 and Sonos controller',
      author='Nic Henke',
      author_email='henken@unholymess.com',
      packages=['sonos-nad'],
      install_requires=REQUIREMENTS,
      license='GPLv2')

