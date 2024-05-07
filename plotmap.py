import seaborn as sns
import matplotlib.pyplot as plt

# Define the correlation matrix
correlation_matrix = [
    [1, -0.040671, 0.123753, 0.123783],
    [-0.040671, 1, 0.130492, -0.409956],
    [0.123753, 0.130492, 1, 0.847458],
    [0.123783, -0.409956, 0.847458, 1]
]

# Define the labels for the axes
labels = ['Price', 'Storage Capacity (cu.ft.)', 'Energy consumption KWH/YR.', 'Energy efficiency (kWh/YR/cu.ft.)']

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', xticklabels=labels, yticklabels=labels)
plt.title('Correlation Matrix Heatmap')
plt.xlabel('Variables')
plt.ylabel('Variables')
plt.show()
