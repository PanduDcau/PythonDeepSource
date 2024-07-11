##Install these Plugins
#pip install pandas matplotlib openpyxl

import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode, stdev, StatisticsError

# Load the dataset
file_path = '/mnt/data/Dataset.xls'  # Adjust the file path as necessary
data = pd.read_excel(file_path)

# Assuming the rainfall data is in a column named 'Rainfall'
rainfall_data = data['Rainfall']

# 1. Highest rainfall
highest_rainfall = rainfall_data.max()
print(f"Highest rainfall: {highest_rainfall}")

# 2. Least rainfall
least_rainfall = rainfall_data.min()
print(f"Least rainfall: {least_rainfall}")

# 3. Average rainfall
average_rainfall = rainfall_data.mean()
print(f"Average rainfall: {average_rainfall}")

# 4. Mode of rainfall values
try:
    mode_rainfall = mode(rainfall_data)
except StatisticsError as e:
    mode_rainfall = "No unique mode"
print(f"Mode of rainfall values: {mode_rainfall}")

# 5. Standard deviation
std_dev_rainfall = stdev(rainfall_data)
print(f"Standard deviation: {std_dev_rainfall}")

# 6. Draw a histogram for rainfall data
plt.hist(rainfall_data, bins=10, edgecolor='black')
plt.title('Rainfall Data Histogram')
plt.xlabel('Rainfall')
plt.ylabel('Frequency')
plt.show()
