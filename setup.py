# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in haberldesign/__init__.py
from haberldesign import __version__ as version

setup(
	name='haberldesign',
	version=version,
	description='Custom App for haberldesign',
	author='Armin Haberl',
	author_email='office@haberldesign.at',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
