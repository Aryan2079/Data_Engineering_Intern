# Create a NumPy array containing numbers from 10 to 50 with step 5.
# Create a 3x3 matrix with random integers between 1 and 100.
# Find the mean, median, and standard deviation of an array.
# Reshape a 1D array of 12 elements into a 3x4 matrix.
# Extract all even numbers from an array.
# Replace all values greater than 50 with 0.
# Perform element-wise multiplication of two arrays.
# Compute the dot product of two matrices.
# Find the index of the maximum and minimum values in an array.
# Normalize an array so values are between 0 and 1.

import numpy as np

# question 1
arr1 = np.arange(10,50,5)

# question 2
arr2 = np.random.randint(1, 100, (3,3))

# question 3
arr2_mean = np.mean(arr2)
arr2_median = np.median(arr2)
arr2_std = np.std(arr2)

# question 4
arr4 = np.arange(12)
print(arr4.reshape((3,4)))

# question 5
arr5 = np.arange(101)
print(np.where(arr5 % 2 == 0))

# question 6
arr6 = np.arange(101)
print(np.where(arr6 > 50, 0, 1))

# question 7
arr7a = np.array([1,2,3])
arr7b = np.array([4,5,6])
print(np.multiply(arr7a, arr7b))

# question 8
arr8a = np.array([1,2,3])
arr8b = np.array([4,5,6])
print(np.dot(arr8a, arr8b))

# question 9
arr9 = np.random.randint(10,100, (1, 10))
print(np.argmin(arr9))
print(np.argmax(arr9))

# question 10 
arr10 = np.random.randint(10, 100, (1, 10))
x_norm = (arr10 - np.min(arr10)) / (np.max(arr10) - np.min(arr10))
print(x_norm)
