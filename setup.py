from setuptools import setup


setup(
  name = 'ftpknocker',
  packages = ['ftpknocker'],
  version = '1.0.4',
  license = 'MIT',
  description = 'ftpknocker is a multi-threaded scanner for finding anonymous FTP servers',
  author = 'Kevin Kennell',
  author_email = 'kevin@kennell.de',
  install_requires=[
        'click',
        'netaddr'
  ],
  url = 'https://github.com/kennell/ftpknocker',
  keywords = ['ftp', 'security'],
  classifiers = [],
  entry_points={
    'console_scripts': [
      'ftpknocker = ftpknocker.cli:main'
    ]
  }
)