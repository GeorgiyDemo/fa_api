from setuptools import setup

setup(name='fa_api',
      version='0.1',
      author='Georgiy Demenchuk',
      author_email='demenchuk.george@protonmail.com',
      license='GPLv3',
      url='https://github.com/GeorgiyDemo/fa_api',
      keywords='python api wrapper ruz fa ru faru library апи питон пайтон обёртка библиотека',
      description='API wrapper for ruz.fa.ru',
      packages=['fa_api'],
      install_requires=[
         'requests==2.23.0',
         'fake-headers==1.0.2',
      ]
      )
