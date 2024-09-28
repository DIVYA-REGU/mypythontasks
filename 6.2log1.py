import re
from datetime import datetime
from collections import Counter

class LogFileAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.errors = []  # Stores tuples of (timestamp, message)
        self.ip_addresses = []  # Stores extracted IP addresses

    def read_log_file(self):
        """Reads the log file and extracts error messages and IP addresses."""
        try:
            with open(self.log_file, 'r') as file:
                content = file.readlines()  # Read all lines for debugging
                print("Log File Content:")
                print(''.join(content))  # Print the content of the log file

                for line in content:
                    # Updated regex to correctly capture severity and IP address
                    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|ERROR|WARNING): (.+) from (\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
                        severity = match.group(2)  # Extract severity
                        message = match.group(3)  # Message without severity
                        ip_address = match.group(4)
                        # Store the complete error message with severity and IP address
                        self.errors.append((timestamp, f"{severity}: {message} from {ip_address}"))
                        self.ip_addresses.append(ip_address)
                        print(f"Extracted Error: {severity}: {message} from {ip_address} at {timestamp}")
                        print(f"Extracted IP Address: {ip_address}")
        except FileNotFoundError:
            print(f"Error: The file {self.log_file} was not found.")
        except Exception as e:
            print(f"An error occurred while reading the log file: {e}")

    def summarize_errors(self):
        """Summarizes the total number of errors."""
        total_errors = len(self.errors)
        print(f"Total number of errors: {total_errors}")
        for timestamp, message in self.errors:
            print(f"{timestamp} - {message}")

    def summarize_ip_addresses(self):
        """Summarizes the frequency of IP addresses."""
        ip_count = Counter(self.ip_addresses)
        print("IP Address Frequencies:")
        for ip, count in ip_count.items():
            print(f"{ip}: {count}")

    def filter_logs(self, start_date=None, end_date=None, severity=None):
        """Filters logs by date range and severity."""
        filtered_errors = []

        for timestamp, message in self.errors:
            if (start_date and timestamp < start_date) or (end_date and timestamp > end_date):
                continue
            if severity and severity not in message:
                continue
            filtered_errors.append((timestamp, message))

        return filtered_errors


if __name__ == "__main__":
    log_analyzer = LogFileAnalyzer('server.log')
    log_analyzer.read_log_file()
    log_analyzer.summarize_errors()
    log_analyzer.summarize_ip_addresses()

    # Adjust filtering criteria to ensure matching logs
    start_date = datetime(2024, 1, 1)  # Start date
    end_date = datetime(2024, 1, 3)    # End date
    severity = None                     # Set to None to include all messages

    filtered_logs = log_analyzer.filter_logs(start_date, end_date, severity)

    print("\nFiltered Logs:")
    for timestamp, message in filtered_logs:
        print(f"{timestamp} - {message}")
