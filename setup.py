from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.5'
DESCRIPTION = 'Collection of automotive calculations'
LONG_DESCRIPTION = 'This repository provides a collection of mathematical formulas commonly used in the automotive industry, with a particular focus on Brushless DC (BLDC) motors.'

with open('README.md') as f:
    long_description = f.read()

# Setting up
setup(
    name="autoCal",
    version=VERSION,
    author="GladsonThomas",
    author_email="<gladson.thomas.official@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'calculations', 'automotive', 'EV', 'BLDC'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)