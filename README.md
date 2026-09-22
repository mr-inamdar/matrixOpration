# matrixOpration

# 🔢 3×3 Matrix Operations using NumPy

A Python project that implements common **3×3 matrix operations** using NumPy.

The main purpose of this project is to understand how matrix operations such as **determinant, adjoint, inverse, and trace** work mathematically by implementing the logic manually instead of directly using NumPy's built-in matrix functions.

## ✨ Features

The program supports the following operations:

1. **Adjoint of a Matrix**
2. **Determinant of a Matrix**
3. **Inverse of a Matrix**
4. **Trace of a Matrix**

The user enters the elements of a **3×3 matrix**, selects an operation, and the program displays the result.

## 🛠️ Technologies Used

* **Python 3**
* **NumPy**

## 📂 Project Structure

```text
Matrix-Operations/
│
├── matrix.py
└── README.md
```

## ⚙️ Installation

Install NumPy using:

```bash
pip install numpy
```

## ▶️ How to Run

Run the Python file:

```bash
python matrix.py
```

The program will ask you to enter the 9 elements of the matrix.

### Example Input

```text
Enter a element of matrix with a defferece of one blanck space:
1 2 3 4 5 6 7 8 9
```

Then select an operation:

```text
1. adjA
2. detA
3. invA
4. tresA

Enter a curasponding no to per this task opretion:
```

## 📐 Supported Operations

### 1. Adjoint

Calculates the **adjoint (adjugate) matrix** using cofactors.

```text
adj(A)
```

### 2. Determinant

Calculates the determinant of the 3×3 matrix.

```text
det(A)
```

### 3. Inverse

Calculates the inverse using:

```text
A⁻¹ = adj(A) / det(A)
```

The inverse exists only when:

```text
det(A) ≠ 0
```

### 4. Trace

Calculates the sum of the main diagonal elements:

```text
Trace(A) = a₁₁ + a₂₂ + a₃₃
```

## 🧪 Example

For the matrix:

```text
1 2 3
0 1 4
5 6 0
```

The program can calculate its:

* Determinant
* Adjoint
* Inverse
* Trace

## 🎯 Purpose

This project was created as a **Python and NumPy learning/practice project**.

It helps demonstrate:

* Working with NumPy arrays
* Nested loops
* Matrix indexing
* Functions
* Conditional statements
* Pattern matching with `match-case`
* Mathematical implementation using Python
* User input handling

## ⚠️ Limitations

This implementation is specifically designed for **3×3 matrices**.

It is an educational implementation and does not replace NumPy's optimized matrix functions for real-world numerical computing.

## 🚀 Possible Improvements

Future versions could include:

* Support for matrices of different sizes
* Matrix multiplication
* Transpose operation
* Rank calculation
* Eigenvalues and eigenvectors
* Better input validation
* Handling singular matrices before calculating the inverse
* A GUI using Tkinter

## 👨‍💻 Author

**Zeeshan**

A Python practice project focused on understanding matrix mathematics and NumPy.

## 📄 License

This project is intended for educational and learning purposes.
