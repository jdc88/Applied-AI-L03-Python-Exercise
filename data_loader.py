import json
import csv

def load_json(file_path):
    """Load data from a JSON file into a Python dictionary."""
    with open(file_path, "r") as json_file:
        return json.load(json_file)

def load_csv(file_path):
    """Load data from a CSV file into a list of lists."""
    data = []
    with open(file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            data.append([float(value) for value in row])
    return data

def load_L1_json():
    """Load L1 data from L1.json."""
    data = load_json("L1.json")
    return data["linear"]

def load_L1_csv():
    """Load L1 data from L1.csv."""
    return load_csv("L1.csv")

def load_Q1_csv():
    """Load Q1 data from Q1.csv."""
    return load_csv("Q1.csv")

def load_Q2_csv():
    """Load Q2 data from Q2.csv."""
    return load_csv("Q2.csv")

print("The data is read and loaded.")