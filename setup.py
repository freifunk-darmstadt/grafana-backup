import codecs
import os.path

import sys
from setuptools import setup, find_packages

from grafana_backup import __PROJECT__, __VERSION__


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

here = os.path.abspath(os.path.dirname(__file__))


# use README as long description
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as handle:
    long_description = handle.read()

# required dependencies
required = [
    'click',
    'requests',
]


setup(
    name=__PROJECT__,
    version=__VERSION__,
    description='Create dashboards backups using the Grafana API.',
    long_description=long_description,
    author='Andreas Rammhold',
    author_email='andreas@rammhold.de',
    url='https://www.github.com/freifunk-darmstadt/grafana-backup',
    license='GPLv2',
    install_requires=required,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['grafana-backup=grafana_backup:backup']
    },
)

