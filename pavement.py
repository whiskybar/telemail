from paver.easy import *
from paver.setuputils import setup


VERSION = (0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


options(
    setup = dict(
    name = 'telemail',
    description = "A simple interface to managing email for a hosting.",
    url = "https://github.com/whiskybar/telemail",
    long_description = "A simple interface to managing email for a hosting.",
    version = __versionstr__,
    author = "Jiri Barton",
    author_email = "jbar@tele3.cz",
    packages = ['telemail'],
    zip_safe = False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ]),
)

setup(**options.setup)

