import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Data
x = np.array([1, 1.75, 3, 3.5, 5.5, 6, 13.5, 14, 18, 18.5, 21.5, 22.75, 26, 27, 28, 30.5, 32, 32])
y = np.array(['Evansh', 'Yuvika', 'Jenisha', 'Evanshi', 'Priyank', 'Mishthi', 'Ekta', 'Ansh', 'Milan', 'Anuj', 'Surya', 'Muskan', 'Happy', 'Vikki', 'Pinki', 'Ritu', 'Monu', 'Jyoti'])

# Plot
plt.figure(figsize=(12, 6))  # Increase the figure size for better readability
plt.bar(y, x, color='c', width=0.6)
plt.title("Us, Cousins, and Their Kids")
plt.xlabel("Names")
plt.ylabel("Values")
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability

# Show plot
plt.show()