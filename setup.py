from distutils.core import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='pylib',
      version='0.0.1',
      description='All your Python services need',
      author='Alice Xia',
      author_email='miss.alice.xia@gmail.com',
      url='https://github.com/missAliceXia/pylib/',
      packages=find_packages(),
      install_requires=requirements)
