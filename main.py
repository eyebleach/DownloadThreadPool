import os
import requests
from concurrent.futures import ThreadPoolExecutor

# class ParallelDownloader:
#     def __init__(self):
#         pass

def download_file(url):
    filename = os.path.basename(url)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")
    else:
        print(f"Downloaded {url}")


def main():
    # Specify the file containing URLs
    urls_file = "urls.txt"

    # Read the file and extract the URLs
    with open(urls_file, 'r') as file:
        urls = file.read().splitlines()

    # Download files using parallel threads
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_file, urls)


if __name__ == '__main__':
    main()

