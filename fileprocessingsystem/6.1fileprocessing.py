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
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                if 'value' in row and condition(row):  # Check if 'value' key exists
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



def process_xml(input_file, output_file, output_format='dict'):
    
    """Read an XML file and write its contents to another XML file or return the data in the specified format."""
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()

        if output_format == 'dict':
            data = []
            for child in root:
                item = {subchild.tag: subchild.text for subchild in child}
                data.append(item)
            return data

        elif output_format == 'custom':
            # Implement your custom data structure here
            pass

        else:
            raise ValueError(f"Invalid output format: {output_format}")

        # Write the original XML content to the output file
        tree.write(output_file)

    except ET.ParseError as e:
        raise ValueError(f"Error parsing XML: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {input_file}")


def main():
    
    csv_input = input("Enter the path to the input CSV file: ")
    csv_output = input("Enter the path to the output CSV file: ")
    json_input = input("Enter the path to the input JSON file: ")
    json_output = input("Enter the path to the output JSON file: ")
    xml_input = input("Enter the path to the input XML file: ")
    xml_output = input("Enter the path to the output XML file (for XML): ")

    # Call the process_xml function with an additional output_format argument
    output_format = 'dict'  # or 'custom', depending on your desired output format

    process_xml(xml_input, xml_output, output_format)

if __name__ == "__main__":
    main()
