import os
from setuptools import setup

__version__ = '0.1.0'


setup(
  name='pykrb5',
  version=__version__,
  description='pure python kerberos 5 implementation',
  url='http://github.com/mhorowitz/pykrb5',
  author='Marc Horowitz',
  packages=['krb5'],
  install_requires=[
    'pyDes==0.2.1',
    'pyasn1==0.0.12a',
    'flufl.enum==3.1',
  ],
  entry_points = {
    'console_scripts': [
      'kdestroy=krb5.bin.kdestroy:main',
      'kinit=krb5.bin.kinit:main',
      'kvno=krb5.bin.kvno:main',
      'klist=krb5.bin.klist:main',
    ],
  }
)
