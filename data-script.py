import json
import os
import pandas as pd

# Define file paths
json_folder_path = os.path.join(os.getcwd(), 'JSON-HERE')  # Folder containing the JSON file
excel_folder_path = os.path.join(os.getcwd(), 'EXCEL-HERE')  # Folder containing the Excel file

# Find the first JSON file in the JSON-HERE folder
json_file_name = next(file for file in os.listdir(json_folder_path) if file.endswith(".json"))
json_file_path = os.path.join(json_folder_path, json_file_name)

# Load JSON data
with open(json_file_path, 'r') as f:
    json_data = json.load(f)

# Clear out specific fields with "X" values
for entry in json_data:
    for key in ["Drop-In Tutoring", "Appointment-Based Tutoring", "TRIO SSS", "eTutoring", "Supplemental Instruction", "Peer-Led Team Learning"]:
        if entry[key] == "X":
            entry[key] = ""

# Read Excel file from EXCEL-HERE folder
excel_file_name = next(file for file in os.listdir(excel_folder_path) if file.endswith(".xlsx"))
excel_file_path = os.path.join(excel_folder_path, excel_file_name)
df = pd.read_excel(excel_file_path)

# Replace NaN with empty string and strip any extra spaces
df.fillna("", inplace=True)
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Iterate over the Excel rows and update JSON data
for _, row in df.iterrows():
    subject = row['Subject']
    number = row['Number']
    for entry in json_data:
        if entry["Subject"].strip() == subject and entry["Number"] == number:
            for key in ["Drop-In Tutoring", "Appointment-Based Tutoring", "TRIO SSS", "eTutoring", "Supplemental Instruction", "Peer-Led Team Learning"]:
                if row[key] == "X":
                    entry[key] = "X"

# Save updated JSON data
with open(json_file_path, 'w') as f:
    json.dump(json_data, f, indent=4)

print("JSON data has been updated.")
