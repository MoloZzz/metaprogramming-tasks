from _matrix_inverse import ffi, lib # type: ignore
import numpy as np

def inverse_matrix_python(matrix):
    """
    Compute the inverse of a square matrix using C function.
    Input: matrix (2D list or numpy array)
    Returns: inverse matrix as numpy array or None if singular
    """
    # Convert input to numpy array if it isn't
    matrix = np.array(matrix, dtype=np.float64)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a square matrix")

    n = matrix.shape[0]
    print(f"Matrix size n: {n}")
    
    # Ensure input matrix is contiguous
    input_matrix = np.ascontiguousarray(matrix.flatten(), dtype=np.float64)
    print("Input matrix data:", input_matrix)
    
    # Allocate output matrix
    output_matrix = lib.allocate_matrix(n)
    if not output_matrix:
        raise MemoryError("Failed to allocate output matrix")

    # Debug: Print output_matrix address as integer
    output_addr = int(ffi.cast("uintptr_t", output_matrix))
    print(f"Output matrix address (hex): {hex(output_addr)}")

    # Copy input matrix to C-compatible array
    input_ptr = ffi.cast("double *", input_matrix.ctypes.data)
    
    # Debug: Print pointers
    print(f"Input pointer: {input_ptr}")
    print(f"Output pointer: {output_matrix}")

    # Call C function
    result = lib.inverse_matrix(input_ptr, output_matrix, n)
    if result != 0:
        lib.free_matrix(output_matrix)
        print("Matrix is singular, cannot compute inverse")
        return None

    # Convert output to numpy array
    inverse = np.zeros((n, n), dtype=np.float64)
    for i in range(n * n):
        inverse[i // n, i % n] = output_matrix[i]

    # Free memory
    lib.free_matrix(output_matrix)
    
    return inverse

# Example usage
if __name__ == "__main__":
    # Test matrix (3x3)
    matrix = [
        [4, 7, 2],
        [3, 6, 1],
        [2, 1, 5]
    ]
    
    print("Input matrix:")
    print(np.array(matrix))
    
    inverse = inverse_matrix_python(matrix)
    if inverse is not None:
        print("\nInverse matrix:")
        print(inverse)
        
        # Verify: A * A^-1 should be identity
        print("\nVerification (A * A^-1):")
        print(np.dot(np.array(matrix), inverse))