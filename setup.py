"""Minimal setup file for Py Map Reporter"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read() 

setup(
    name ='map_analyzer',
    version = '0.2.1',
    description="A Python tool for GHS map analysis",

    author = 'Melodypapa',
    author_email = "melodypapa@outlook.com",
    url="https://github.com/melodypapa/py-map-analyzer",

    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='GHS Map', 

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    install_requires=['toml', "openpyxl"],
    include_package_data=True,
    
    extras_require={'pytest': 'pytest-cov'},

    python_requires=">=3.5",

    license="MIT",

    entry_points={
        'console_scripts': [
            'map-analyzer = map_analyzer.cli.map_analyzer:main'
        ]
    }
)
