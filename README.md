# Python Mathematical Toolkit: Vector Algebra Data Type

A custom Python implementation of a **2D Vector** data type designed to handle linear algebra operations. This project is the second installment in the **Python Mathematical Toolkit** series, focusing on Object-Oriented Programming (OOP) to represent and manipulate geometric vectors in a 2D plane.

## 🚀 Key Features

* **Geometric Computations:** Built-in methods for calculating **Magnitude** (length) and **Unit Vectors**.
* **Vector Relationships:** Includes logic to determine the **Angle** between two vectors and a check for **Orthogonality** (perpendicularity).
* **Advanced Algebra:** Supports **Vector Projection** (projecting Vector A onto Vector B) and the **Dot Product**.
* **Scalar & Vector Arithmetic:** Handles standard vector addition, subtraction, and multiplication by a scalar.
* **Interactive CLI:** A feature-rich command-line menu that allows users to perform complex vector analysis dynamically.

## 📐 Mathematical Logic

The class implements 2D vector math ($v = x\mathbf{i} + y\mathbf{j}$) using the following formulas:

| Operation | Python Method / Logic | Formula Used |
| :--- | :--- | :--- |
| **Magnitude** | `v.magnitude()` | `(x**2 + y**2)**0.5` |
| **Addition** | `v1.vector_addition(v2)` | `Vector(x1+x2, y1+y2)` |
| **Subtraction** | `v1.vector_subtraction(v2)` | `Vector(x1-x2, y1-y2)` |
| **Dot Product** | `v1.dot_product(v2)` | `(x1*x2) + (y1*y2)` |
| **Unit Vector** | `v.unit_vector()` | `Vector(x/mag, y/mag)` |
| **Angle** | `v1.angle_bw_vectors(v2)` | `acos(dot_prod / (mag1 * mag2))` |
| **Orthogonality** | `v1.orthogonal(v2)` | `True if dot_product == 0` |
| **Projection** | `v1.vector_projection(v2)` | `(dot_prod / mag2**2) * v2`

## 💻 How to Use

1. **Clone the Repository:**
    ```bash
    git clone [https://github.com/moizcoder01/Python-Mathematical-Toolkit-Vector-Algebra-Data-Type.git)
    ```
2. **Run the Script:**
    ```bash
    python "DataType creation.py"
    ```
3. **Follow the Prompts:**
    * Select an operation from the menu (1-9).
    * Enter coordinates in $x, y$ format when prompted.
    * View the calculated result (e.g., Magnitude, Unit Vector, or Projection).

---
**Part of the Python Mathematical Toolkit Series Fraction DataType** *Built with ❤️ by [moizcoder01][https://github.com/moizcoder01/Python-Mathematical-Toolkit-Fraction-Data-Type.git)
