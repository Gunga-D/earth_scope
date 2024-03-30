from setuptools import setup, find_packages

setup(
   name='geoscope',
   version='1.0.0',
   packages=find_packages(),
   install_requires=[
      'click',
      'obspy',
   ],
   entry_points='''
      [console_scripts]
      geoscope=bin.cli:run
      ''',
)