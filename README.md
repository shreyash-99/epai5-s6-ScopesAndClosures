# Assignment - Closure Functions

## Problem Statement

1. **Check Function Docstring Length**: Write a closure that takes a function and checks whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable.

2. **Next Fibonacci Number**: Write a closure that gives you the next Fibonacci number.

3. **Count Function Calls**: Write a closure that can keep track of how many times `add`, `mul`, and `div` functions were called, and update a global dictionary variable with the counts.

4. **Count Function Calls with Custom Dictionary**: Modify the above closure such that now we can pass in different dictionary variables to update different dictionaries.

### Submission Requirements

- Code implementation.
- Test code with the following requirements:
  - 4 tests for checking the docstring length closure.
  - 2 tests for the Fibonacci number closure.
  - 6 tests for counting function calls.
  - 6 tests for counting function calls with a custom dictionary.
  - At least 7 additional test cases to check boundary conditions.
- Upload the code to GitHub, run actions, and then proceed to answer the assignment Q&A.

## Solution Explanation

### 1. Check Function Docstring Length

This closure checks if the docstring of a given function has more than 50 characters.

- **`check_function_min_length_docstring`**: A closure is created with a free variable `min_length` set to 50. The inner function checks if the docstring length of the passed function is greater than or equal to `min_length`.

### 2. Next Fibonacci Number

This closure generates the next number in the Fibonacci sequence.

- **`fibonacci`**: A closure with a cache to store computed Fibonacci numbers. The inner function calculates and returns the next Fibonacci number using recursion and memoization.

### 3. Count Function Calls

This closure tracks how many times specific functions (`add`, `mul`, `div`) are called and updates a global dictionary with these counts.

- **`counter_add_mul_div`**: Returns three inner functions, each wrapping `add`, `mul`, and `div` respectively. These inner functions update a shared dictionary that keeps track of how many times each function is called.

### 4. Count Function Calls with Custom Dictionary

This closure allows passing different dictionary variables to track function calls.

- **`counter_3_functions`**: Takes three functions and their names, returning three inner functions that update a passed-in dictionary to track how many times each of the three functions is called.

## Tests

The solution includes tests to ensure the closures work correctly. The tests check various conditions and edge cases to validate the implementation.

## Test Overview

This section provides an overview of the different types of tests written for validating the closures and their functionalities in the assignment.

### General Tests
- **`test_readme_exists`**: Checks if the `README.md` file exists in the directory.


### Tests for `check_function_min_length_docstring` Closure
- **`test_minlength_docstring_check_if_function_exist`**: Verifies the existence of the `check_function_min_length_docstring` function in the module.
- **`test_minlength_docstring_check_working`**: Validates the functionality of the docstring length check with different docstring lengths.
- **`test_minlength_docstring_changing_minlength1` and `test_minlength_docstring_changing_minlength2`**: Ensure that changing the minimum length through the closure works correctly.
- **`test_minlength_docstring_function_param_types`**: Checks if the function raises `TypeError` for invalid parameter types.
- **`test_minlength_docstring_closure_function_params`**: Validates error handling for invalid parameters passed to the closure's inner functions.

### Tests for `fibonacci` Closure
- **`test_fibonacci_function_exist`**: Ensures the `fibonacci` function exists.
- **`test_fibonacci_input_params`**: Verifies that the function raises appropriate errors for invalid input parameters.
- **`test_fibonacci_final_output`**: Checks if the Fibonacci function returns the correct sequence values.

### Tests for `counter` Closure
- **`test_function_counter_exist`**: Verifies the existence of the `counter` function.
- **`test_function_counter_input_params`**: Ensures the function raises errors for invalid input parameters.
- **`test_function_counter_final_output`**: Validates that the counter correctly tracks the number of function calls.

### Tests for `counter_add_mul_div` Closure
- **`test_count_add_mul_div_exist`**: Checks if the `counter_add_mul_div` function exists.
- **`test_count_add_mul_div_params_init`**: Ensures the function handles parameter initialization errors correctly.
- **`test_count_add_mul_div_func_param`**: Validates error handling for invalid parameters passed to the add, multiply, and divide functions.
- **`test_count_add_mul_div_functionality_add`, `test_count_add_mul_div_functionality_mul`, `test_count_add_mul_div_functionality_div`**: Verify the correctness of the add, multiply, and divide functions and their respective counters.
- **`test_count_add_mul_div_functionality_counter`**: Ensures that the counters for all three functions track the number of calls accurately.

### Tests for `counter_3_functions` Closure
- **`test_3_function_counter_exist`**: Verifies the existence of the `counter_3_functions` function.
- **`test_3_function_counter_init`**: Ensures the function raises errors for incorrect initialization parameters.
- **`test_3_function_counter_func1_init`, `test_3_function_counter_func2_init`, `test_3_function_counter_func3_init`**: Validate that the closure retains the original function's docstring and name.
- **`test_3_function_counter_working`**: Checks that the counters for the three functions track the number of calls correctly.

These tests comprehensively validate the functionality and robustness of the closures implemented in the assignment, ensuring correct behavior under various conditions and inputs.
