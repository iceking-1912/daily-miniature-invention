/*
 * example.cpp
 * Implements a 3D vector class with basic algebraic operations.
 */

#include <iostream>
#include <cmath> // For std::sqrt

class Vector3D {
public:
    double x, y, z;

    // Constructor
    Vector3D(double x_val = 0.0, double y_val = 0.0, double z_val = 0.0)
        : x(x_val), y(y_val), z(z_val) {}

    // Vector addition: v1 + v2
    Vector3D operator+(const Vector3D& other) const {
        return Vector3D(x + other.x, y + other.y, z + other.z);
    }

    // Vector subtraction: v1 - v2
    Vector3D operator-(const Vector3D& other) const {
        return Vector3D(x - other.x, y - other.y, z - other.z);
    }

    // Scalar multiplication: v * scalar
    Vector3D operator*(double scalar) const {
        return Vector3D(x * scalar, y * scalar, z * scalar);
    }

    // Dot product
    double dot(const Vector3D& other) const {
        return x * other.x + y * other.y + z * other.z;
    }

    // Magnitude of the vector
    double magnitude() const {
        return std::sqrt(x * x + y * y + z * z);
    }

    // Normalize the vector (returns a unit vector)
    Vector3D normalize() const {
        double mag = magnitude();
        if (mag > 1e-9) { // Avoid division by zero for very small magnitudes
            return Vector3D(x / mag, y / mag, z / mag);
        }
        return Vector3D(); // Return a zero vector if magnitude is zero
    }

    // Print vector coordinates to console
    void print() const {
        std::cout << "(" << x << ", " << y << ", " << z << ")" << std::endl;
    }
};

// Global scalar multiplication (scalar * vector) for flexibility
Vector3D operator*(double scalar, const Vector3D& vec) {
    return Vector3D(vec.x * scalar, vec.y * scalar, vec.z * scalar);
}

// Example usage in main function
int main() {
    // Create two 3D vectors
    Vector3D v1(1.0, 2.0, 3.0);
    Vector3D v2(4.0, -1.0, 2.0);

    std::cout << "Initial Vectors:\n";
    std::cout << "  v1: "; v1.print();
    std::cout << "  v2: "; v2.print();
    std::cout << "--------------------\n";

    // Demonstrate vector addition
    Vector3D v_sum = v1 + v2;
    std::cout << "v1 + v2: "; v_sum.print();

    // Demonstrate vector subtraction
    Vector3D v_diff = v1 - v2;
    std::cout << "v1 - v2: "; v_diff.print();

    // Demonstrate scalar multiplication
    Vector3D v_scaled_by_v1 = v1 * 2.5; // vector * scalar
    std::cout << "v1 * 2.5: "; v_scaled_by_v1.print();

    Vector3D v_scaled_by_scalar = 3.0 * v2; // scalar * vector
    std::cout << "3.0 * v2: "; v_scaled_by_scalar.print();

    // Demonstrate dot product
    double dot_product = v1.dot(v2);
    std::cout << "Dot product of v1 and v2: " << dot_product << std::endl;

    // Demonstrate magnitude calculation
    double mag_v1 = v1.magnitude();
    std::cout << "Magnitude of v1: " << mag_v1 << std::endl;

    // Demonstrate vector normalization
    Vector3D v1_normalized = v1.normalize();
    std::cout << "Normalized v1: "; v1_normalized.print();
    std::cout << "  Magnitude of normalized v1: " << v1_normalized.magnitude() << std::endl;

    // Test with a zero vector
    Vector3D zero_vec;
    std::cout << "Normalized zero vector: "; zero_vec.normalize().print();

    return 0;
}
