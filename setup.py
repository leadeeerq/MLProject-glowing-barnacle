# The setup script is the centre of all activity in building, distributing, and installing modules using Distutils.
from setuptools import find_packages, setup

setup(
    name = 'MLProject',
    version = '1.0',
    author = 'Arcadiusz',
    author_email= 'arkadiusz.nikonowicz@gmail.com',
    packages=find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)