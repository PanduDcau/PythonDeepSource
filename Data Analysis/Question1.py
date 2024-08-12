import numpy as np

# Reading the data from 'dataset.csv' into a numpy array
data = np.genfromtxt('Tutorial(dataset).csv', delimiter=',', skip_header=1).astype(int)

# Display the array
print("Array:\n", data)

# Display all the values in the first row
print("\nFirst row:", data[0])

# Display all the values in the last row
print("\nLast row:", data[-1])

# Display values in rows from 5th to 9th and columns 1st and 2nd
print("\nRows 5th to 9th, Columns 1st and 2nd:\n", data[4:9, 0:2])

# Create three arrays a, b, c by separating three columns
a = data[:, 0]
b = data[:, 1]
c = data[:, 2]

# Add 5 to all the values in array a
a_plus_5 = a + 5
print("\nArray 'a' after adding 5:\n", a_plus_5)

# Add each value in array a to each value in array b and display the answers
a_plus_b = a + b
print("\nArray 'a + b':\n", a_plus_b)