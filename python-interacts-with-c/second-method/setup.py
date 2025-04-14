from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "wordfreq",
        sources=["wordfreq.pyx", "wordfreq_core.c"],
        language="c",
    )
]

setup(
    name="wordfreq",
    ext_modules=cythonize(ext_modules),
    zip_safe=False,
)