import numpy as np
import time

# Define two Python lists
py_list1 = list(range(100000))
py_list2 = list(range(100000, 200000))

# Define two Numpy arrays
np_array1 = np.arange(100000)
np_array2 = np.arange(100000, 200000)

# Adding Python lists
start_time = time.time()
result_list = [a + b for a, b in zip(py_list1, py_list2)]
print("Time taken to add Python lists: ", time.time() - start_time)

# Adding Numpy arrays
start_time = time.time()
result_array = np_array1 + np_array2
print("Time taken to add Numpy arrays: ", time.time() - start_time)