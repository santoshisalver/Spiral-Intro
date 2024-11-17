# Spiral Matrix Traversal

This Python program implements the spiral traversal of a 2D matrix. 
Given an `m x n` matrix, the program traverses the matrix in a spiral order and prints the elements in the required sequence.

## Description

The program creates a matrix of dimensions `m x n` and fills it with numbers starting from 1. 
It then traverses the matrix in a spiral order (starting from the top-left corner and moving in a spiral direction) and prints the elements in that order.

The matrix traversal starts with:

1. The top row from left to right.
2. The last column from top to bottom.
3. The bottom row from right to left.
4. The first column from bottom to top.

This process repeats for the inner layers of the matrix until all elements are covered.

## Functionality

### `spiral(m, n, a)`

#### Parameters:
- `m` (int): The number of rows in the matrix.
- `n` (int): The number of columns in the matrix.
- `a` (list of lists): The 2D matrix (of size `m x n`) to be traversed.

#### Description:
The function takes a matrix `a` of dimensions `m x n` and prints the elements in spiral order.

### Example

#### Input:
A 4x4 matrix filled with numbers 1 to 16:
###output
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
