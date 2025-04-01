# auto_fiscal_downloader

An automation tool that logs into a tax/fiscal reporting website, navigates through company listings, downloads reports for each company, and renames the files according to the company name.

## Description

This project automates the tedious process of:
1. Logging into a fiscal reporting portal
2. Navigating through multiple pages of company listings
3. Downloading PDF reports for each company
4. Automatically renaming the downloaded files based on company names

This saves significant time for accountants and financial professionals who need to process reports for multiple companies.

## Features

- Automated login to secure portals
- Batch processing of multiple companies
- Automated file downloads
- Intelligent file renaming
- Pagination support for handling large datasets

## Requirements

- Python 3.6+
- Required libraries:
  - selenium
- Chrome WebDriver

## Installation

```bash
pip install selenium
```

You'll also need to install the Chrome WebDriver appropriate for your Chrome version. Visit the [Chrome WebDriver download page](https://chromedriver.chromium.org/downloads) for more information.

## Configuration

Before running the script, update the following:

1. Set your download directory in the `chrome_options.add_experimental_option` section
2. Update the directory path in the `diretorio` variable inside the `baixar_relatorios_das_empreas` function

## Usage

Run the script:

```bash
python app.py
```

The script will:
1. Open the browser and navigate to the login page
2. Log in with the provided credentials
3. Download files for each company listed
4. Rename each file according to the company name
5. Continue to the next page until all companies are processed

## Important Notes

- The code in this repository is a simplified demonstration model
- The URL used in this code (`https://consulta-empresa.netlify.app/`) is a fictional placeholder for privacy reasons
- Login credentials shown in the code are examples and should be replaced with real credentials
- Personal and private information from the original request has been removed


## Disclaimer

This tool is provided as-is without any warranties. Always ensure you have proper authorization to access and download files from the systems you're automating.
