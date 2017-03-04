""" A setuptools based setup module.

    Adapted from:
    https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='Constantine',
    version='0.1',
    description='A poster generator that does something that should have been automated ages ago.',
    url='https://github.com/icydoge/Constantine',
    author='C Shi',
    author_email='icydoge@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Text Processing :: General',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='pdf generator',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={},
    entry_points={
        'console_scripts': [
            'Constantine=Constantine:main',
        ],
    },
)
