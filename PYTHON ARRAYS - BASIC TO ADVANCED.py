# ========================================================
#           PYTHON ARRAYS - BASIC TO ADVANCED
# ========================================================

# This program demonstrates:
# 1. Array Creation
# 2. Accessing Elements
# 3. Updating Elements
# 4. Looping Arrays
# 5. Array Methods
# 6. Multi-Dimensional Arrays
# 7. NumPy Arrays
# 8. Sorting Arrays
# 9. Searching Arrays
# 10. Real-world Examples

# ========================================================


# ========================================================
#                   IMPORT ARRAY MODULE
# ========================================================

# Python array module

import array

# ========================================================
#                   CREATE ARRAY
# ========================================================

# 'i' means integer type array

numbers = array.array('i', [10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)


# ========================================================
#               ACCESS ARRAY ELEMENTS
# ========================================================

print("\nAccess Elements")

print(numbers[0])

print(numbers[2])

print(numbers[-1])


# ========================================================
#               UPDATE ARRAY ELEMENTS
# ========================================================

numbers[1] = 99

print("\nUpdated Array")

print(numbers)


# ========================================================
#               LOOP THROUGH ARRAY
# ========================================================

print("\nLoop Through Array")

for num in numbers:

    print(num)


# ========================================================
#               ARRAY LENGTH
# ========================================================

print("\nArray Length")

print(len(numbers))


# ========================================================
#               APPEND ELEMENT
# ========================================================

numbers.append(60)

print("\nAfter Append")

print(numbers)


# ========================================================
#               INSERT ELEMENT
# ========================================================

numbers.insert(2, 25)

print("\nAfter Insert")

print(numbers)


# ========================================================
#               REMOVE ELEMENT
# ========================================================

numbers.remove(40)

print("\nAfter Remove")

print(numbers)


# ========================================================
#               POP ELEMENT
# ========================================================

numbers.pop()

print("\nAfter Pop")

print(numbers)


# ========================================================
#               ARRAY REVERSE
# ========================================================

numbers.reverse()

print("\nReversed Array")

print(numbers)


# ========================================================
#               ARRAY INDEX SEARCH
# ========================================================

print("\nIndex Search")

print(numbers.index(25))


# ========================================================
#               ARRAY COUNT
# ========================================================

numbers.append(25)

print("\nCount of 25")

print(numbers.count(25))


# ========================================================
#               SORT ARRAY
# ========================================================

sorted_array = sorted(numbers)

print("\nSorted Array")

print(sorted_array)


# ========================================================
#               ARRAY SLICING
# ========================================================

print("\nArray Slicing")

print(numbers[1:4])


# ========================================================
#               MULTI-DIMENSION ARRAY
# ========================================================

print("\n2D Array")

matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]
]

for row in matrix:

    print(row)


# ========================================================
#               SEARCH ELEMENT
# ========================================================

print("\nSearch Element")

search = 99

if search in numbers:

    print("Element Found")

else:

    print("Element Not Found")


# ========================================================
#               ARRAY SUM
# ========================================================

print("\nArray Sum")

print(sum(numbers))


# ========================================================
#               ARRAY MAXIMUM & MINIMUM
# ========================================================

print("\nMaximum Value")

print(max(numbers))

print("\nMinimum Value")

print(min(numbers))


# ========================================================
#               REAL WORLD EXAMPLE
#           STUDENT MARKS MANAGEMENT
# ========================================================

print("\nStudent Marks Management")

marks = array.array('i', [80, 90, 75, 88, 95])

total = sum(marks)

average = total / len(marks)

print("Marks:", marks)

print("Total:", total)

print("Average:", average)


# ========================================================
#                   NUMPY ARRAYS
# ========================================================

# NumPy provides advanced array features.

import numpy as np

np_array = np.array([1, 2, 3, 4, 5])

print("\nNumPy Array")

print(np_array)


# ========================================================
#               NUMPY ARRAY OPERATIONS
# ========================================================

print("\nNumPy Addition")

print(np_array + 10)

print("\nNumPy Multiplication")

print(np_array * 2)


# ========================================================
#               MULTI-DIMENSION NUMPY
# ========================================================

matrix2 = np.array([

    [1, 2, 3],

    [4, 5, 6]
])

print("\n2D NumPy Array")

print(matrix2)


# ========================================================
#               RESHAPE ARRAY
# ========================================================

reshape_array = np.array([1,2,3,4,5,6])

print("\nReshape Array")

print(reshape_array.reshape(2,3))


# ========================================================
#               RANDOM ARRAY
# ========================================================

random_array = np.random.randint(1, 100, 5)

print("\nRandom Array")

print(random_array)


# ========================================================
#               ZERO AND ONE ARRAYS
# ========================================================

print("\nZeros Array")

print(np.zeros((2,2)))

print("\nOnes Array")

print(np.ones((2,2)))


# ========================================================
#               ARRAY MATHEMATICAL OPERATIONS
# ========================================================

a = np.array([1,2,3])

b = np.array([4,5,6])

print("\nAddition")

print(a + b)

print("\nSubtraction")

print(a - b)

print("\nMultiplication")

print(a * b)


# ========================================================
#                   PROGRAM END
# ========================================================

# Arrays are used for:
# - Data Storage
# - Data Processing
# - Machine Learning
# - Data Science
# - Numerical Computation

# Types:
# 1. Python Array
# 2. NumPy Array

# ========================================================