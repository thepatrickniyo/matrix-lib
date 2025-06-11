"""
Quick demonstration of alumath_peergroup_6 library capabilities.
Perfect for showcasing the library features.
"""

from alumath_peergroup_6 import Matrix, multiply, hadamard_product, broadcast_multiply

def demo_basic_usage():
    """Demonstrate basic library usage."""
    print("🎯 ALUMATH_PEERGROUP_6 QUICK DEMO")
    print("=" * 40)
    
    print("📊 Creating matrices...")
    
    # Create some example matrices
    matrix_a = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix_b = Matrix([[7, 8], [9, 10], [11, 12]])
    
    print(f"Matrix A (2×3):\n{matrix_a}")
    print(f"Matrix B (3×2):\n{matrix_b}")
    
    # Standard matrix multiplication
    print("\n🔢 Standard Matrix Multiplication (A × B):")
    result = multiply(matrix_a, matrix_b, method="standard")
    print(f"Result (2×2):\n{result}")
    
    # Element-wise multiplication
    print("\n⚡ Element-wise Multiplication (Hadamard Product):")
    square_a = Matrix([[1, 2], [3, 4]])
    square_b = Matrix([[5, 6], [7, 8]])
    
    print(f"Square A:\n{square_a}")
    print(f"Square B:\n{square_b}")
    
    hadamard_result = hadamard_product(square_a, square_b)
    print(f"A ⊙ B:\n{hadamard_result}")
    
    # Broadcasting
    print("\n📡 Broadcasting (Matrix × Scalar):")
    scalar = Matrix([[3]])
    print(f"Scalar:\n{scalar}")
    
    broadcast_result = broadcast_multiply(square_a, scalar)
    print(f"Matrix × Scalar:\n{broadcast_result}")
    
    # Matrix properties
    print("\n📏 Matrix Properties:")
    print(f"Matrix A shape: {matrix_a.shape}")
    print(f"Matrix A rows: {matrix_a.rows}, columns: {matrix_a.cols}")
    print(f"Element at (0,1): {matrix_a.get_element(0, 1)}")
    print(f"First row: {matrix_a.get_row(0)}")
    print(f"Second column: {matrix_a.get_column(1)}")
    
    # Transpose
    print(f"\nTranspose of A:\n{matrix_a.transpose()}")
    
    print("\n🎉 Demo completed! Your library is working perfectly!")

if __name__ == "__main__":
    demo_basic_usage()
