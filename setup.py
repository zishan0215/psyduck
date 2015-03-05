try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Psyduck Encrypted Chat',
	'author': '12CSSXX',
	'url': 'https://github.com/zishanAhmad/psyduck',
	'download_url': 'https://github.com/zishanAhmad/psyduck',
	'author_email': 'zishanrbp@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['PSYDUCK'],
	'scripts': [],
	'name': 'psyduck'
}

setup(**config)