import numpy as np
import random
from data_loader import load_Q1_csv, load_Q2_csv

def calculate_statistics(data):
    """Calculate mean and standard deviation for each column in the data."""
    data = np.array(data)
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    return mean, std_dev

def find_outliers(data, std_dev_threshold=2):
    """Find outliers greater than the specified number of standard deviations."""
    mean, std_dev = calculate_statistics(data)
    outliers = []
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if abs(value - mean[j]) > std_dev_threshold * std_dev[j]:
                outliers.append((i, j, value))  # (row_index, col_index, value)
    return outliers

def remove_outliers(data, std_dev_threshold=2):
    """Remove outliers from the data."""
    mean, std_dev = calculate_statistics(data)
    cleaned_data = []
    for row in data:
        is_outlier = False
        for i, value in enumerate(row):
            if abs(value - mean[i]) > std_dev_threshold * std_dev[i]:
                is_outlier = True
                break
        if not is_outlier:
            cleaned_data.append(row)
    return cleaned_data

def normalize_data(data):
    """Normalize data so all values are within the range [-1, 1] and mean is 0."""
    data = np.array(data)
    min_vals = np.min(data, axis=0)
    max_vals = np.max(data, axis=0)
    # Scale to [-1, 1]
    normalized_data = 2 * ((data - min_vals) / (max_vals - min_vals)) - 1
    normalized_data -= np.mean(normalized_data, axis=0)  # Center the data to mean 0
    return normalized_data


def process_data():
    """Main function to load, process, and display the data."""
    # Load data from Q1.csv and Q2.csv
    data_q1 = load_Q1_csv()
    data_q2 = load_Q2_csv()

    # Find and display outliers
    outliers_q1 = find_outliers(data_q1)
    outliers_q2 = find_outliers(data_q2)
    print("Outliers in Q1.csv:", outliers_q1)
    print("Outliers in Q2.csv:", outliers_q2)

    # Remove outliers from the data
    data_q1_cleaned = remove_outliers(data_q1)
    data_q2_cleaned = remove_outliers(data_q2)

    # Normalize the cleaned data
    data_q1_normalized = normalize_data(data_q1_cleaned)
    data_q2_normalized = normalize_data(data_q2_cleaned)

    # Display 10 random values from the normalized data
    print("\n10 Random Values from Normalized Q1 Data:")
    print(random.sample(list(data_q1_normalized), 10))

    print("\n10 Random Values from Normalized Q2 Data:")
    print(random.sample(list(data_q2_normalized), 10))

    # Split data into X_data and Y_data
    X_data_q1 = np.array([row[1] for row in data_q1_normalized])
    Y_data_q1 = np.array([row[0] for row in data_q1_normalized])

    X_data_q2 = np.array([row[1] for row in data_q2_normalized])
    Y_data_q2 = np.array([row[0] for row in data_q2_normalized])

    print("\nFirst 10 values of X_data (Q1):", X_data_q1[:10])
    print("First 10 values of Y_data (Q1):", Y_data_q1[:10])

    print("\nFirst 10 values of X_data (Q2):", X_data_q2[:10])
    print("First 10 values of Y_data (Q2):", Y_data_q2[:10])

    return X_data_q1, Y_data_q1, X_data_q2, Y_data_q2

if __name__ == "__main__":
    process_data()
