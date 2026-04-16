import numpy as np
import matplotlib.pyplot as plt

# Data for the pie chart
arr = np.array([1, 1.75, 3, 3.5, 5.5, 6, 13.5, 14, 18, 18.5, 22.85, 23, 26, 27, 29, 30.5, 32, 32])
names = ["Evansh", "Yuvika", "Jenisha", 'Evanshi', "Priyank", "Heenal", "Ekta", "Akhil", "Milan", "Anuj", "Sandeep", "Muskan", "Aman", "Vikas", "Preeti", "Ritu", "Jaideep", "Jyoti"]

# Plotting the pie chart
plt.figure(figsize=(14,12))  # Further increasing the figure size
plt.pie(arr, labels=names, autopct='%1.1f%%', 
        wedgeprops={'edgecolor': 'black'}, 
        textprops={'fontsize': 10},
        labeldistance=0.8)  # Further increase the distance of labels from the center

# Adding a legend outside of the pie chart
plt.legend(loc="center left", bbox_to_anchor=(0.9, 0.5), title="Experience")

# Adding a title
plt.title("Experience Distribution")

# Ensuring the pie chart is circular
plt.axis('equal')

# Display the chart
plt.show()
