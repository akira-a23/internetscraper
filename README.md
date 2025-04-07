# Web Scraping Tool

This Python web scraping tool allows users to extract different types of data from websites easily. It supports scraping **quotes**, **headings**, and **links** from web pages and saves the data in CSV format.

## Features
- Scrape **quotes** and authors from a webpage.
- Scrape all **headings** (h1, h2, h3, h4, h5, h6) from a webpage.
- Scrape **hyperlinks** (URLs and their associated link text) from a webpage.
- Save scraped data to CSV files for easy access and further analysis.

## Requirements

Before running the scraper, ensure you have Python and the required libraries installed. The following libraries are needed:

- `requests`: To send HTTP requests and fetch webpage content.
- `beautifulsoup4`: To parse the HTML content of the page.
- `pandas`: To store the extracted data and save it to CSV.

### Install Required Libraries

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 pandas
