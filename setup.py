"""Setup module."""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dupes',
    version='0.0.1',
    description='Detect visually similar images.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cgoldberg/dupes',
    author='Corey Goldberg',
    keywords='image detection perceptual hashing',
    py_modules=['dupes'],
    python_requires='>=3.3',
    install_requires=['ImageHash'],
    project_urls={
        'Source': 'https://github.com/cgoldberg/dupes',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
