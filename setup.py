# -*- coding: utf-8 -*-
'''
Created on 2017-09-26

@author: yangpengjs 
'''
import io
import os
import re
from distutils.core import setup

from setuptools import find_packages

packages = find_packages('app')

LONGDOC = """
graphql is a web app base on
    Python Flask + gql.

Aims to send GraphQL requests easily
"""


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(name='graphqlpy-client',
      version=find_version('app/__init__.py'),
      description=(u'使用Flask开发的一个 web app, 用来进行GraphQL请求。'),
      long_description=LONGDOC,
      author='yangpengjs',
      author_email='591995637@qq.com',
      url='https://github.com/yangwii',
      license='MIT',
      install_requires=[
          'flask==0.12.2',
          'flask-sqlalchemy==2.1',
          'gql==0.1.0',
          'graphene==1.4.1',
          'Flask-GraphQL==1.4.1',
          'redis==2.10.5',
          'graphene-sqlalchemy==1.1.1'
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Utilities'
      ],
      keywords='Flask, GraphQL, gql, client',
      include_package_data=True,
      packages=['app'],
      py_modules=['manage'],
      zip_safe=False,
      entry_points={
          'console_scripts': ['graphqlpy-client=manage:run']
      })
