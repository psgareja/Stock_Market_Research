import csv
import json

# Function to clean up the CSV data and remove unwanted characters
def clean_data(data):
    cleaned_data = []
    for row in data:
        cleaned_row = {}
        for key, value in row.items():
            # Remove unwanted characters from keys (like BOM and quotes)
            cleaned_key = key.replace('\u00ef\u00bb\u00bf', '').replace('"', '').strip()
            cleaned_row[cleaned_key] = value.strip() if isinstance(value, str) else value
        cleaned_data.append(cleaned_row)
    return cleaned_data

# Function to convert CSV to JSON
def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Open the CSV file and read it
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:  # Using utf-8-sig to handle BOM
        csv_reader = csv.DictReader(csv_file)
        
        # Convert each row of the CSV to a dictionary and append to data list
        for row in csv_reader:
            data.append(row)

    # Clean the data
    cleaned_data = clean_data(data)

    # Write the cleaned data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(cleaned_data, json_file, indent=4)

# Example usage
csv_to_json('input.csv', 'output_data.json')
