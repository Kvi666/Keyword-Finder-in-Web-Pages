#Keyword Finder in Web Pages

A Python script that scans a list of URLs to check for the presence of a specific keyword. This tool supports both `requests` and `Selenium` for scraping and outputs results in an HTML format for easy viewing.

## Features

- Scans a list of URLs for a specific word or keyword.
- Supports two methods for scraping:
  - `requests` and `BeautifulSoup` for quick, lightweight scraping.
  - `Selenium` for more dynamic or JavaScript-heavy websites.
- Outputs results in an HTML file with URLs marked if the keyword is found.

## Requirements

Python 3.6 or higher - Make sure Python is installed on your machine.
Libraries - Install the following Python libraries:
requests - for making HTTP requests.
beautifulsoup4 - for parsing HTML.
selenium - if you intend to use Selenium for JavaScript-heavy pages.
Chrome WebDriver - Required if using Selenium. Download the Chrome WebDriver version compatible with your Chrome browser, and update the Service path in check_for_word_selenium function to the WebDriver’s location on your machine.

## How to Install
Install the necessary libraries by running: pip install requests beautifulsoup4 selenium

## How to Use

To use the website_scan.py script, create a urls.txt file in the same directory, listing each URL on a new line. Run the script by typing python website_scan.py in your terminal, and when prompted, enter the keyword you want to search for within the URLs. The script will scan each page, using either requests or Selenium (if use_selenium=True is set in the code). The results, indicating which URLs contain the keyword (highlighted in red if found), will be saved in an output.html file, which you can open in a browser for easy viewing.
