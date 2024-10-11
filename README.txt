# JSON and Excel Data Updater

This script is designed to update a JSON file with data from an Excel file. It performs the following operations:

1. **Clears Specific Fields**: Updates fields with "X" values in the JSON data.
2. **Reads Excel Data**: Processes an Excel file to update the JSON data.
3. **Updates JSON Data**: Syncs JSON data based on Excel data.

## Prerequisites

- Python 3.x

## Dependencies

The script requires the `pandas` library. It is used to read and process the Excel file. The `json` library is included with Python, so no additional installation is needed for that.

### Installing Dependencies

To install the required dependencies, you can use `pip`. Follow these steps:

1. **Install pandas**:

   Open a terminal or command prompt and run the following command:

   ```bash
   pip install pandas
   ```

## Directory Structure

```
/path/to/project
│
├── JSON-HERE/
│   └── your-json-file.json
│
├── EXCEL-HERE/
│   └── your-excel-file.xlsx
│
└── data-script.py
```

## Script Details

### File Paths

- **JSON Folder Path**: Folder containing the JSON file. Default is `JSON-HERE`.
- **Excel Folder Path**: Folder containing the Excel file. Default is `EXCEL-HERE`.
- **JSON File Path**: Path to the JSON file to be updated.

### Steps

1. **Load JSON Data**: Reads the JSON file and loads its data.
2. **Clear Specific Fields**: Iterates through the JSON data and sets specific fields to empty strings if they have "X" values.
3. **Read Excel File**: Loads the Excel file from the `EXCEL-HERE` folder.
4. **Process Excel Data**: Cleans and processes the Excel data.
5. **Update JSON Data**: Updates the JSON data based on the content of the Excel file.
6. **Save Updated JSON**: Writes the updated JSON data back to the file.

### Key Code Sections

- **Clearing Specific Fields**:
  ```python
  for key in ["Drop-In Tutoring", "Appointment-Based Tutoring", "TRIO SSS", "eTutoring", "Supplemental Instruction", "Peer-Led Team Learning"]:
      if entry[key] == "X":
          entry[key] = ""
  ```

- **Reading and Processing Excel File**:
  ```python
  df = pd.read_excel(excel_file_path)
  df.fillna("", inplace=True)
  df.columns = df.columns.str.strip()
  df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
  ```

- **Updating JSON Data**:
  ```python
  for _, row in df.iterrows():
      subject = row['Subject']
      number = row['Number']
      for entry in json_data:
          if entry["Subject"].strip() == subject and entry["Number"] == number:
              for key in ["Drop-In Tutoring", "Appointment-Based Tutoring", "TRIO SSS", "eTutoring", "Supplemental Instruction", "Peer-Led Team Learning"]:
                  if row[key] == "X":
                      entry[key] = "X"
  ```

## Running the Script

1. Place the JSON file in the `JSON-HERE` folder.
2. Place the Excel file in the `EXCEL-HERE` folder.
3. Run the script:

   ```bash
   python data-script.py
   ```

4. The script will print "JSON data has been updated." when finished.

## Notes

- Ensure the JSON and Excel files are formatted correctly.
- Adjust folder paths as needed.
- Only one Excel file should be present in the `EXCEL-HERE` folder.

Feel free to modify the script as needed to suit your specific use case.