import pandas as pd

# Create a DataFrame with the given data
data = {
    'Price': [1700, 1250, 1025, 1200, 1100, 4600, 3900, 4100, 4800, 1800, 1325, 1570, 1275, 1700, 1050, 1275, 1200, 1030, 1600, 880, 825, 750, 900, 800, 630, 800, 1100, 680, 680, 940, 680, 750, 1200, 530],
    'Storage Capacity (cu.ft.)': [16, 16, 15.9, 15.9, 13.5, 15.4, 13.6, 14.4, 15, 16.2, 16.3, 16.3, 17.5, 16.8, 13.3, 14.6, 13.2, 13.3, 17.7, 13.3, 14.4, 16.9, 16.9, 16, 14, 14.1, 16.1, 16.4, 14.1, 14.3, 16.5, 15.9, 14.5],
    'Energy consumption KWH/YR.': [490, 520, 520, 520, 560, 511, 571, 513, 567, 613, 653, 653, 654, 668, 625, 715, 686, 671, 660, 650, 440, 514, 463, 478, 417, 450, 458, 480, 440, 479, 528, 472, 479],
    'Energy efficiency (kWh/YR/cu.ft.)': [30.63, 32.5, 32.7, 32.7, 41.48, 33.18, 41.99, 35.63, 37.8, 37.84, 40.06, 40.06, 37.37, 39.76, 46.99, 42.31, 46.99, 50.45, 37.29, 48.87, 30.56, 30.41, 30.66, 28.63, 34.14, 29.57, 27.95, 27.93, 34.04, 31.21, 33.5, 32, 29.69, 33.03]
}

df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

print(correlation_matrix)
