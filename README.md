#   Python Lists and Matrices Algorithms

This project contains Python implementations of algorithms for list manipulation, including complement calculation, list shifting, perfect list checking, and matrix operations.

This project was developed as part of the 20606 course of the Open University.

The full assignment instructions are available in [Task 3.pdf](Task%203.pdf).

##   Table of Contents

* [Project Description](#project-description)
* [Algorithms Implemented](#algorithms-implemented)
    * [List Complement](#list-complement)
    * [List Shift](#list-shift)
    * [Perfect List Check](#perfect-list-check)
    * [Matrix Operations](#matrix-operations)
* [Usage](#usage)
* [Author](#author)

##   Project Description

The project provides Python functions to perform the following tasks:

* Calculate the complement of a list of natural numbers.
* Shift a list to the right by a specified number of positions.
* Check if a list is "perfect" according to defined rules.
* Check if a 2D list is an identity matrix and perform operations on matrices.

##   Algorithms Implemented

###   List Complement

The `complement(lst)` function calculates the complement of a list of distinct natural numbers within the range of 1 to the maximum value in the list.

###   List Shift

The `shift_k_right(lst, k)` function shifts a list to the right by *k* positions with wrap-around. The `shift_right_size(a, b)` function determines the shift size needed to make two lists equal.

###   Perfect List Check

The `is_perfect(lst)` function checks if a list is "perfect" based on a specific scanning algorithm that follows the values in the list as indices.

###   Matrix Operations

The `identity_matrix(mat)` function checks if a 2D list is an identity matrix. The `create_sub_matrix(mat, size)` function extracts a centered square sub-matrix. The `max_identity_matrix(mat)` function finds the size of the largest centered identity sub-matrix.

##   Usage

To use the code in this repository:

1.  Ensure you have Python 3.x installed.
2.  Save the `mmn13.py` file.
3.  Run the script from the command line.
4.  You can call the functions directly with appropriate inputs as needed.

##   Author

Sagi Menahem.
