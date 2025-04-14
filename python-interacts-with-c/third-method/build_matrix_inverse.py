from cffi import FFI
import os

# Initialize CFFI
ffi = FFI()

# Define the C interface
with open('matrix_inverse.h', 'r') as f:
    ffi.cdef(f.read())

# Source code for compilation
ffi.set_source(
    "_matrix_inverse",
    '#include "matrix_inverse.h"',
    sources=['matrix_inverse.c'],
    include_dirs=[os.getcwd()],
)


# Compile the module
if __name__ == "__main__":
    ffi.compile(verbose=True)