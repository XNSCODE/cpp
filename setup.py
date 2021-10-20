from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name="ambf",
    ext_modules = cythonize(Extension(
    "ambf",
    sources=["ambf.py", "ambf.cpp"],
    libraries=["ambf"],
    language="c++",
)))
