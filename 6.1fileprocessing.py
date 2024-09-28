import csv
import json
import xml.etree.ElementTree as ET
import os

class FileProcessingError(Exception):
    """Custom exception for file processing errors."""
    pass

def process_csv(input_file, output_file, condition):
    """Process CSV file and write results to a new CSV file."""
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            
            reader = csv.DictReader(infile)
            print("Column names:", reader.fieldnames)  # Print column names for debugging
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            
            for row in reader:
                if condition(row):  # Apply the condition to filter rows
                    writer.writerow(row)
    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {input_file}")
    except Exception as e:
        raise FileProcessingError(f"An error occurred: {str(e)}")

def process_json(input_file, output_file):
    """Read a JSON file and write its contents to another JSON file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = json.load(infile)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4)
    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {input_file}")
    except json.JSONDecodeError:
        raise FileProcessingError(f"Error decoding JSON from {input_file}")
    except Exception as e:
        raise FileProcessingError(f"An error occurred: {str(e)}")

def process_xml(input_file, output_file):
    """Read an XML file and write its contents to another XML file."""
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Example processing: Convert XML tree to a list of dictionaries
        data = []
        for child in root:
            item = {subchild.tag: subchild.text for subchild in child}
            data.append(item)

        # Writing to JSON format for the output
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4)
    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {input_file}")
    except ET.ParseError:
        raise FileProcessingError(f"Error parsing XML from {input_file}")
    except Exception as e:
        raise FileProcessingError(f"An error occurred: {str(e)}")

def main():
    csv_input = input("Enter the path to the input CSV file: ")
    csv_output = input("Enter the path to the output CSV file: ")
    json_input = input("Enter the path to the input JSON file: ")
    json_output = input("Enter the path to the output JSON file: ")
    xml_input = input("Enter the path to the input XML file: ")
    xml_output = input("Enter the path to the output JSON file (for XML): ")
    
    # Adjust the column name here based on your CSV file
    condition = lambda row: float(row['value']) > 10  # Ensure 'value' matches your CSV header

    # Process files
    process_csv(csv_input, csv_output, condition)
    process_json(json_input, json_output)
    process_xml(xml_input, xml_output)

if __name__ == "__main__":
    main()
