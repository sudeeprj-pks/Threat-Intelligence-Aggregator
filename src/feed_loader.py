
import os
import json
import csv

FEEDS_FOLDER = "../feeds"


def load_txt(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def load_csv(file_path):
    data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip header safely
        for row in reader:
            if row and row[0].strip():
                data.append(row[0].strip())
    return data


def load_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
        return [item["url"] for item in data if "url" in item]


def load_all_feeds():
    all_data = {}

    for file in os.listdir(FEEDS_FOLDER):
        path = os.path.join(FEEDS_FOLDER, file)

        if file.endswith(".txt"):
            all_data[file] = load_txt(path)

        elif file.endswith(".csv"):
            all_data[file] = load_csv(path)

        elif file.endswith(".json"):
            all_data[file] = load_json(path)

    return all_data
