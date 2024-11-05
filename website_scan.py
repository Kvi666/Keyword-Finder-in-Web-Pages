import requests;
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def read_urls(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

def check_for_word(url, word):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        return word.lower() in soup.text.lower()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return False

def check_for_word_selenium(url, word):
    service = Service(r'C:\\Users\\kawee\\Downloads\\Compressed\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    try:
        driver.get(url)
        page_content = driver.page_source
        return word.lower() in page_content.lower()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return False
    finally:
        driver.quit()

def save_results(results, output_file='output.html'):
    with open(output_file, 'w') as file:
        for url, found in results.items():
            if found:
                file.write(f'<span style="color:red">{url}</span><br>')
            else:
                file.write(f'{url}<br>')

def main(use_selenium=False):
    urls = read_urls('urls.txt')
    word_to_search = input("Enter the word you want to search for: ")  # Get word from user
    results = {}

    for url in urls:
        if not url:  # Skip empty lines
            continue

        if use_selenium:
            found = check_for_word_selenium(url, word_to_search)
        else:
            found = check_for_word(url, word_to_search)

        results[url] = found

    for url, found in results.items():
        print(f"{url}: {'Found' if found else 'Not found'}")

    save_results(results)  # Save results after checking all URLs

if __name__ == "__main__":
    main()  # Run the main function
