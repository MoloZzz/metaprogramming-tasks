from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'lis',  # Назва модуля
        ['lis.cpp'],  # Файл із кодом C
        include_dirs=[pybind11.get_include()],  # Шлях до pybind11
        language='c++',
        extra_compile_args=['-std=c++11'],  # Стандарт C++ (якщо потрібно)
    ),
]

setup(
    name='lis',
    version='0.1',
    ext_modules=ext_modules,
    zip_safe=False,
)