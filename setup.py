import os.path
from setuptools import setup, find_packages

VERSION = (0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

ROOT = os.path.dirname(__file__)
requirements = [line.strip() for line in open(os.path.join(ROOT, 'requirements.txt'))]

setup(
    name = 'telemail',
    version = __versionstr__,
    description = 'A simple interface to managing email for a hosting.',
    long_description = '\n'.join((
        'telemail',
        '',
        'A simple interface to managing email for a hosting.',
    )),
    author = 'Jiri Barton',
    author_email='jbar@tele3.cz',
    license = 'BSD',

    packages = find_packages(),
    package_data = {
        '': ['fixtures/*.yaml', 'templates/*/*.html', 'locale/*/*/*.mo'],
    },
    include_package_data = True,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'setuptools>=0.6b1',
    ] + requirements,
)

