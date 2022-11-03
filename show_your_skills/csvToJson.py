import csv
import json

# Open up the CSV File
with open("filename.output.csv", "r") as f:
    reader = csv.reader(f)
    # Ignore the headers as an individual row
    next(reader)

    data = []
    # Iterate across the reader object
    for row in reader:
        # Append to the empty data list
        data.append(
            {
                "Series Number": row[0],
                "Filename": row[1],
                "Name": row[2],
                "Description": row[3],
                "Gender": row[4],
                "Attributes": row[5],
                "UUID": row[6],
                "Hash": row[7],
            }
        )

# Create a new json file called "hngi9_json_file.json"
with open("filename.output.json", "w") as f:
    # Dump our data into the newly created json file
    json.dump(data, f, indent=4)
