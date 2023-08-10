# Parallel File Downloader

![license MIT](https://badgen.net/github/license/eyebleach/DownloadThreadPool)

This script provides a simple way to download multiple files in parallel from a list of URLs. It leverages Python's `concurrent.futures.ThreadPoolExecutor` to download files concurrently, making the download process faster and more efficient.

## Requirements

- Python 3.x
- `requests` library

## Installation

```bash
pip install requests
```

## Usage

1. Create a text file named urls.txt in the same directory as the script, and add the URLs of the files you want to download, one URL per line.

2. Run the script:

```bash
python main.py
```

## Functionality

`download_file(url)`: Downloads a file from the given URL and saves it in the current working directory. If the download fails, an error message is printed.

`main()`: Reads the URLs from urls.txt, and downloads the files using parallel threads.
Contributing

Feel free to fork the repository and submit pull requests for any enhancements or bug fixes. If you encounter any issues, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details
