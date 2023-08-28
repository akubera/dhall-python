#!/usr/bin/env python3

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    rust_extensions=[RustExtension("dhall.dhall", binding=Binding.PyO3)],
)
