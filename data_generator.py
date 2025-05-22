import json
import csv
import random

# 100_000 (y, x) pairs where x is within the range [-1000.0, +1000.0]
data = []
for _ in range(100_000):
    x = random.uniform(-1000.0, 1000.0)
    y = 2.0 + 0.5 * x
    data.append([y, x])

with open("L1.json", "w") as json_file:
    json.dump({"linear": data}, json_file)

with open("L1.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["y", "x"])
    writer.writerows(data)

data_q2 = []
for _, x in data:
    x1 = 0.5 * x
    x2 = -3 * (x ** 2)
    y = 2.0 + 0.5 * x - 3 * (x ** 2)
    data_q2.append([y, x1, x2])

with open("Q1.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["y", "x"])
    writer.writerows([[row[0], row[1]] for row in data_q2])

with open("Q2.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["y", "x1", "x2"])
    writer.writerows(data_q2)

print("Files saved: L1.json, L1.csv, Q1.csv, Q2.csv")
