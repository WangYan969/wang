# coding:utf-8
from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'test01',
    version = '0.0.1',
    keywords = ('simple', 'test'),
    description = 'just a simple test',
    license = 'MIT License',

    author = 'WangYan',
    author_email = '201002002@@@',

    packages = find_packages(),
    platforms = 'any',
)
