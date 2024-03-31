from setuptools import setup
from os import path
from io import open
import pathlib

with open(path.join(pathlib.Path(__file__).parent, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]

setup(
    name='geoscope',
    version='1.0.0',
    py_modules=['geoscope'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'geoscope = bin.cli:run'
        ]
    }
)