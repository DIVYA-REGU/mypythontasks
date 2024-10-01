import csv
import json
import xml.etree.ElementTree as ET
import os
import logging

# Setup logging configuration
logging.basicConfig(
    filename='file_parser.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FileParser:
    def read_csv(self, file_path):
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                logging.info(f"Successfully read CSV file: {file_path}")
                return data
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            print(f"Error: File not found: {file_path}")
        except PermissionError:
            logging.error(f"Permission denied: {file_path}")
            print(f"Error: Permission denied: {file_path}")
        except csv.Error as e:
            logging.error(f"CSV error: {e}")
            print(f"Error: CSV error: {e}")
        return []  # Return an empty list on error

    def read_json(self, file_path):
        try:
            with open(file_path, mode='r') as file:
                data = json.load(file)
                logging.info(f"Successfully read JSON file: {file_path}")
                return data
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            print(f"Error: File not found: {file_path}")
        except PermissionError:
            logging.error(f"Permission denied: {file_path}")
            print(f"Error: Permission denied: {file_path}")
        except json.JSONDecodeError as e:
            logging.error(f"JSON error: {e}")
            print(f"Error: JSON error: {e}")
        return None  # Return None on error

    def read_xml(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = []
            for child in root:
                data.append({elem.tag: elem.text for elem in child})
            logging.info(f"Successfully read XML file: {file_path}")
            return data
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            print(f"Error: File not found: {file_path}")
        except PermissionError:
            logging.error(f"Permission denied: {file_path}")
            print(f"Error: Permission denied: {file_path}")
        except ET.ParseError as e:
            logging.error(f"XML error: {e}")
            print(f"Error: XML error: {e}")
        return []  # Return an empty list on error

    def process_csv_data(self, data):
        if not data:
            print("No data to process.")
            return

        numeric_columns = []
        for key, value in data[0].items():
            if isinstance(value, (int, float)):  # Check for numeric types directly
                numeric_columns.append(key)
            # You can add logic here to handle lists differently (e.g., sum list elements)

        print(f"Numeric columns found: {numeric_columns}")

        total_sum = 0
        for row in data:
            for column in numeric_columns:
                if isinstance(row[column], (int, float)):  # Check for numeric types again
                    total_sum += row[column]
        print(f"Total sum of numeric columns: {total_sum}")

    def is_numeric(self, value):
        if not isinstance(value, str):
            return False  # Not a string, not numeric
        try:
            float(value)
            return True
        except ValueError:
            return False

def main():
    parser = FileParser()

    # Specify the file paths
    csv_file_path = input("Enter the path to the CSV file: ")
    json_file_path = input("Enter the path to the JSON file: ")
    xml_file_path = input("Enter the path to the XML file: ")

    # Read and process CSV
    print("\nProcessing CSV file...")
    csv_data = parser.read_csv(csv_file_path)
    parser.process_csv_data(csv_data)

    # Read and process JSON
    print("\nProcessing JSON file...")
    json_data = parser.read_json(json_file_path)
    print(json_data)

    # Read and process XML
    print("\nProcessing XML file...")
    xml_data = parser.read_xml(xml_file_path)
    print(xml_data)

if __name__ == "__main__":
    main()
