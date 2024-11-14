from setuptools import setup
import os

dir_setup = os.path.dirname(os.path.realpath(__file__))

__version__ = "0.1.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='aview_python',
      version=__version__,
      description='A set of Python scripts to automate modeling and mechanisms analysis using MSC Adams View.',
      author='Pedro Jorge De Los Santos',
      author_email='delossantosmfq@gmail.com',
      license = "MIT",
      keywords=["MSC Adams","Kinematics","Dynamics","Scripting"],
      url='https://github.com/JorgeDeLosSantos/aview_python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['aview_python',],
      install_requires=[''],
      classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: Implementation :: CPython",
      ]
      )
