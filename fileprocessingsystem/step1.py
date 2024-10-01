import csv
import json
import xml.etree.ElementTree as ET

class FileProcessingError(Exception):
    """Custom exception for file processing errors."""
    pass

def process_csv(input_file, output_file, filter_condition):
    """Reads a CSV file, processes it, and writes the results to a new CSV file."""
    try:
        with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Write header to output file
            header = next(reader)
            writer.writerow(header)

            # Process rows based on filter condition
            for row in reader:
                if filter_condition(row):
                    writer.writerow(row)

    except FileNotFoundError:
        raise FileProcessingError(f"The file {input_file} was not found.")
    except Exception as e:
        raise FileProcessingError(f"An error occurred while processing the CSV file: {e}")

def filter_condition(row):
    """Example condition: Filter rows where the value in the second column is greater than 50."""
    return int(row[1]) > 50

def process_json(input_file, output_file, filter_condition):
    """Reads a JSON file, processes it, and writes the results to a new JSON file."""
    try:
        with open(input_file, mode='r') as infile:
            data = json.load(infile)

        filtered_data = [item for item in data if filter_condition(item)]

        with open(output_file, mode='w') as outfile:
            json.dump(filtered_data, outfile, indent=4)

    except FileNotFoundError:
        raise FileProcessingError(f"The file {input_file} was not found.")
    except json.JSONDecodeError:
        raise FileProcessingError("Error decoding JSON.")
    except Exception as e:
        raise FileProcessingError(f"An error occurred while processing the JSON file: {e}")

def filter_condition_json(item):
    """Example condition for JSON: Filter items where the 'value' key is greater than 50."""
    return item['value'] > 50  # Assuming each item is a dictionary with a 'value' key

def process_xml(input_file, output_file, filter_condition):
    """Reads an XML file, processes it, and writes the results to a new XML file."""
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
        filtered_data = []

        for elem in root.findall('item'):  # Assuming 'item' is the XML element of interest
            value = int(elem.find('value').text)  # Adjust according to your XML structure
            if filter_condition(value):
                filtered_data.append(ET.tostring(elem, encoding='unicode'))

        with open(output_file, mode='w') as outfile:
            outfile.write('<items>\n')
            outfile.writelines(filtered_data)
            outfile.write('</items>\n')

    except FileNotFoundError:
        raise FileProcessingError(f"The file {input_file} was not found.")
    except ET.ParseError:
        raise FileProcessingError("Error parsing XML.")
    except Exception as e:
        raise FileProcessingError(f"An error occurred while processing the XML file: {e}")

def filter_condition_xml(value):
    """Example condition for XML: Filter items where the value is greater than 50."""
    return value > 50

if __name__ == "__main__":
    try:
        # Process CSV
        process_csv('file1.csv', 'fileoutput.csv', filter_condition)

        # Process JSON
        process_json('file.json', 'fileoutput.json', filter_condition_json)

        # Process XML
        process_xml('file.xml', 'fileoutput.xml', filter_condition_xml)

        print("File processing completed successfully.")
    except FileProcessingError as e:
        print(e)
