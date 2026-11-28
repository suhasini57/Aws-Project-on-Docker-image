import numpy as np

def calculate_twice_of_array(arr):
    return arr*2

if np.__version__ == "2.5.2":
    print("NumPy is exactly 2.5.2")

    numpy_array = np.array([12, 45, 7, 89, 23, 56, 34, 78, 91, 15,
                62, 38, 5, 73, 49, 27, 84, 19, 66, 41,
                93, 8, 55, 30, 71, 22, 87, 14, 60, 36,
                98, 3, 52, 25, 79, 44])

    print(calculate_twice_of_array(numpy_array))
else:
    print(f"NumPy is {np.__version__}, not 2.5.2")

