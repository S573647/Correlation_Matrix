import pandas as pd

# Create a dictionary with the given data
data = {
    'Price': [1700.00,1250.00,1025.00,1200.00,1100.00,4600.00,3900.00,4100.00,4800.00,1800.00,1325.00,1570.00,1275.00,1700.00,1275.00,1050.00,1150.00,1200.00,1030.00,1600.00,880.00,825.00,750.00,900.00,800.00,630.00,800.00,1100.00,680.00,680.00,940.00,680.00,750.00,1200.00,530.00],
    'Storage Capacity (cu.ft.)': [16,16,15.9,15.9,13.5,15.4,13.6,14.4,15,16.2,16.3,16.3,17.5,16.8,13.3,16.9,14.6,13.2,13.3,17.7,13.3,14.4,16.9,15.1,16,14,14.1,16.1,16.4,14.1,14.1,14.3,16.5,15.9,14.5],
    'Energy consumption KWH/YR.': [490,520,520,520,560,511,571,513,567,613,653,653,654,668,625,715,686,647,671,660,650,440,514,463,458,478,417,450,458,480,440,479,528,472,479],
    'Energy efficiency (kWh/YR/cu.ft.)': [30.63,32.50,32.70,32.70,41.48,33.18,41.99,35.63,37.80,37.84,40.06,40.06,37.37,39.76,46.99,42.31,46.99,49.02,50.45,37.29,48.87,30.56,30.41,30.66,28.63,34.14,29.57,27.95,27.93,34.04,31.21,33.50,32.00,29.69,33.03]
}

# Check the length of each column
for key, value in data.items():
    print(f"Length of {key}: {len(value)}")

df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

print(correlation_matrix)

# Define the file path
file_path = "correlation_matrix.txt"

# Write the correlation matrix to the file
with open(file_path, 'w') as file:
    file.write(correlation_matrix.to_string())