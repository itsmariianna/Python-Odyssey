# Write a function that reads a JSON file containing a list of dictionaries. The function should process the data (e.g., find all entries with a specific attribute) and write the results to a new JSON file.
import json

def filter_json(input_file, output_file, attribute, value):
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    filtered_data = [entry for entry in data if entry.get(attribute) == value]

    with open(output_file, 'w') as outfile:
        json.dump(filtered_data, outfile, indent=4)

    print(f"Filtered data in {output_file}")

input_file = 'data.json'
output_file = 'filtered_data.json'
attribute = 'name'
value = 'Ann'

filter_json(input_file, output_file, attribute, value)
