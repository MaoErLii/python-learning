# Simple Assignment Statement

## In a simple assignment, we create new variables, assign and change values. This statement provides an expression and a variable name as a label to preserve the value of the expression  

## Example

  ``` 示例

  Case-1: Right-Hand-Side(RHS) is just a value-based expression

  >>> test = "Learn Python"

  /**
    1. If you create another string with the same value, Python will create a new object and assign it to a different location in memory.

    2. Python wiil allocate the same memory address in the following two scenarios.
        * the string don't have whitespace and contain less than 20 characters.
        * in case of integers ranging between -5 to +255.
  */


  Case-2: Right-Hand Side(RHS) is a current python variable

  >>> another_test = test

  /**
    the above statement won't triggle any new allocation in memery
  */

  >>> test = "Learn Python"
  >>> id(test)
  >>> another_test = test
  >>> id(another_test)


  Case-3: Right-Hand Side(RHS) is an operation

  >>> test = 2 * 5 / 10.0
  >>> print(test)
  >>> type(test)

  >>> test = 2 * 5
  >>> print(test)
  >>> type(test)

  /**
    the result would depend on the otcome of the operation.
  */

  ```
