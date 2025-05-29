"""
Student: [Sagi Menahem]
ID: [208645937]
Assignment: Maman 13

This file contains solutions for the problems in Maman 13.

"""

# --- Constants ---
# Starting index, typically 0.
START_INDEX = 0
# Value indicating termination.
TERMINATION_VALUE = 0
# Error for unequal row lengths.
ERROR_MESSAGE_UNEQUAL_ROWS = "Not all rows are equal"
# Error for non-integer matrix values.
ERROR_MESSAGE_NON_INTEGER_VALUES = "Not all values are int"


# --- Question 1 Functions ---
def complement(lst):
    """
    Calculates the complement of a list of distinct natural numbers.

    Args:
        lst (list): List of distinct natural numbers.

    Returns:
        list: The complement list. Empty if input is empty.
    """
    # Handle empty input list.
    if len(lst) == 0:
        return []

    # Find max value for range limit.
    max_val = max(lst)

    # Initialize list for missing numbers.
    complement_list = []

    # Check each number from 1 to max_val.
    for cur in range(1, max_val + 1):
        # Flag to track if current number is found.
        found = False

        # Iterate through input list to find the number.
        for item in lst:
            if item == cur:
                found = True
                # Stop searching if found.
                break

        # Add number to complement if not found in input list.
        if not found:
            complement_list.append(cur)

    # Return list of missing numbers.
    return complement_list


# --- Question 2 Function ---
def shift_k_right(lst, k):
    """
    Shifts a list right by k positions with wrap-around.

    Args:
        lst (list): The input list.
        k (int): Non-negative shift amount <= len(lst).

    Returns:
        list: The right-shifted list.

    Raises:
        ValueError: If k is invalid.
    """
    # Validate shift amount.
    if k < 0 or k > len(lst):
        raise ValueError("Shift amount (k) must be non-negative and not greater than the list length")

    # Get list size.
    list_length = len(lst)

    # Calculate effective shift for wrap-around.
    effective_k = k % list_length

    # No shift needed.
    if effective_k == 0:
        return list(lst)

    # Perform the right shift
    shifted_list = lst[list_length - effective_k:] + lst[:list_length - effective_k]

    # Return the result.
    return shifted_list

def shift_right_size(a, b):
    """
    Finds the right shift size for list b to match list a.

    Args:
        a (list): The target list.
        b (list): The list to shift.

    Returns:
        int: The shift size k if match found, else None.
             Returns 0 for empty lists of same length.
    """
    # Lists must have same length.
    if len(a) != len(b):
        return None

    # Empty lists match with shift 0.
    if len(a) == 0:
        return 0

    # Get list length.
    list_length = len(a)

    # Try all possible shift sizes.
    for k in range(list_length):
        # Apply shift to list b.
        try:
            shifted_b = shift_k_right(b, k)
        except ValueError:
            # If k is invalid, skip to the next iteration
            return None


        # Check if shifted b matches a.
        if a == shifted_b:
            # Return shift size if match found.
            return k

    # No matching shift found.
    return None


# --- Question 3 Function ---
def is_perfect(lst):
    """
    Checks if a list is "perfect" via value-driven scanning.

    Args:
        lst (list): List of integers.

    Returns:
        bool: True if perfect, False otherwise. True for empty list.

    Raises:
        IndexError: Scan index out of bounds.
        TypeError: Non-integer cell value encountered.
    """
    # Empty list is perfect.
    if len(lst) == 0:
        return True

    # Start scan at index 0.
    current_index = START_INDEX

    # Track visited indices to detect cycles.
    visited_indices = []

    # Flag for termination at value 0.
    is_terminated = False

    # Start the scanning loop.
    while True:
        # Check if index is within list bounds.
        if current_index < 0 or current_index >= len(lst):
            raise IndexError("Index out of bounds")

        # Check if index was already visited (indicates a cycle).
        if current_index in visited_indices:
             break

        # Mark current index as visited.
        visited_indices.append(current_index)

        # Get value that determines next index.
        current_value = lst[current_index]

        # Check if value is an integer.
        if not isinstance(current_value, int):
            raise TypeError("Cell value must be an integer")

        # Check for termination condition (value is 0).
        if current_value == TERMINATION_VALUE:
            is_terminated = True
            break

        # Move to next index based on current value.
        current_index = current_value

    # Perfect if terminated AND all cells were visited.
    if is_terminated and len(visited_indices) == len(lst):
        return True
    else:
        return False


# --- Question 4 Function ---
def identity_matrix(mat):
    """
    Checks if a 2D list is an identity matrix.

    Args:
        mat (list): A 2D list.

    Returns:
        bool: True if identity matrix, False otherwise. False for empty matrix.

    Raises:
        TypeError: Non-integer element found.
    """
    # Empty matrix is not identity.
    if not mat:
        return False

    # Get matrix dimensions.
    num_rows = len(mat)
    num_cols = len(mat[0])

    # Must be a square matrix.
    if num_rows != num_cols:
        return False

    # Check each row.
    for i in range(num_rows):
        # Ensure consistent row lengths.
        if len(mat[i]) != num_cols:
             return False

        # Check each element in the row.
        for j in range(num_cols):
            # Get element value.
            cur = mat[i][j]

            # Check if element is an integer.
            if not isinstance(cur, int):
                raise TypeError(ERROR_MESSAGE_NON_INTEGER_VALUES)

            # Check diagonal elements (must be 1).
            if i == j:
                if cur != 1:
                    return False
            # Check non-diagonal elements (must be 0).
            else:
                if cur != 0:
                    return False

    # All checks passed, it's an identity matrix.
    return True

def create_sub_matrix(mat, size):
    """
    Extracts a centered square sub-matrix of a given size.

    Args:
        mat (list): The input 2D list (matrix).
        size (int): Size of the square sub-matrix.

    Returns:
        list: The centered sub-matrix.

    Raises:
        IndexError: Empty matrix, empty/unequal rows.
    """
    # Get number of rows.
    num_rows = len(mat)

    # Handle empty matrix case.
    if num_rows == 0:
        raise IndexError("Cannot create sub-matrix from empty matrix")

    # Get column count.
    try:
        num_cols_first_row = len(mat[0])
    except IndexError:
        raise IndexError("First row is empty")

    # Check for unequal row lengths.
    for i in range(num_rows):
        if len(mat[i]) != num_cols_first_row:
            raise IndexError(ERROR_MESSAGE_UNEQUAL_ROWS)

    # Calculate center indices and offset for sub-matrix.
    center_row_index = num_rows // 2
    offset = size // 2
    center_col_index = num_cols_first_row // 2

    # Determine sub-matrix start/end row/column indices.
    start_row = center_row_index - offset
    end_row = center_row_index + offset + 1
    start_col = center_col_index - offset
    end_col = center_col_index + offset + 1

    # Initialize new list for the sub-matrix.
    sub_matrix = []

    # Extract rows and columns for the sub-matrix.
    for i in range(start_row, end_row):
        # Slice relevant columns from the current row.
        sub_row = mat[i][start_col:end_col]
        # Add the sliced row to the new sub-matrix.
        sub_matrix.append(sub_row)

    # Return the extracted sub-matrix.
    return sub_matrix

def max_identity_matrix(mat):
    """
    Finds the size of the largest centered identity sub-matrix.

    Args:
        mat (list): Input 2D list (matrix), assumed square with odd rows.

    Returns:
        int: Size of largest centered identity sub-matrix, or 0 if none found.
             Returns 0 on IndexError/TypeError with specific message.
    """
    # Handle potential errors during sub-matrix processing.
    try:
        # Empty matrix has no identity sub-matrix >= size 1.
        if not mat:
             return 0

        # Get number of rows to determine largest size to check.
        num_rows = len(mat)

        # Iterate through possible odd sub-matrix sizes (largest to smallest).
        for current_size in range(num_rows, 0, -2):
            # Extract sub-matrix for current size.
            sub_mat = create_sub_matrix(mat, current_size)

            # Check if the extracted sub-matrix is an identity matrix.
            if identity_matrix(sub_mat):
                # Return size of the first identity sub-matrix found (largest).
                return current_size

        # No identity sub-matrix found.
        return 0

    except IndexError:
        # Handle index errors
        print(ERROR_MESSAGE_UNEQUAL_ROWS)
        return 0

    except TypeError:
        # Handle type errors
        print(ERROR_MESSAGE_NON_INTEGER_VALUES)
        return 0