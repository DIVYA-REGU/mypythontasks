import threading
import time
import requests

# List of URLs to download
urls = [
    'https://example.com/file1.txt',
    'https://example.com/file2.txt',
    'https://example.com/file3.txt',
    # Add more URLs as needed
]

# Shared resource: List to store downloaded file contents
downloaded_files = []
lock = threading.Lock()  # Lock to prevent race conditions

# Function to download a file
def download_file(url):
    response = requests.get(url)
    with lock:  # Acquiring lock to safely append to the shared list
        downloaded_files.append(response.content)
    print(f'Finished downloading {url}')

# Measure time for single-threaded download
def single_threaded_download():
    start_time = time.time()
    for url in urls:
        download_file(url)
    end_time = time.time()
    print(f'Single-threaded download took {end_time - start_time:.2f} seconds')

# Multi-threaded download function
def multi_threaded_download():
    threads = []
    start_time = time.time()
    
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f'Multi-threaded download took {end_time - start_time:.2f} seconds')

if __name__ == "__main__":
    # Run single-threaded download
    print("Starting single-threaded download...")
    single_threaded_download()
    
    # Clear the downloaded files list for a fair comparison
    downloaded_files.clear()
    
    # Run multi-threaded download
    print("Starting multi-threaded download...")
    multi_threaded_download()

    # Output the performance comparison
    print(f"Total files downloaded: {len(downloaded_files)}")
