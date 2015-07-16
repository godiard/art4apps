#! /usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    import ez_setup
    ez_setup.use_setuptools(version="0.6c1")

from setuptools import setup

setup(
    name="art4apps",
    version= "0.3.2",
    packages=["art4apps"],
    namespace_packages=['art4apps'],
    include_package_data = True,
    zip_safe = False,
    url = "http://www.art4apps.org/",
    description="Art4Apps images and data to use it",
    license="BSD License",
    maintainer="Gonzalo Odiard",
    maintainer_email="godiard@gmail.com",
)
