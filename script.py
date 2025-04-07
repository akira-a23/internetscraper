import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes(soup):
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    data = []
    for quote, author in zip(quotes, authors):
        data.append({
            'Quote': quote.text.strip(),
            'Author': author.text.strip()
        })
    return data

def scrape_headings(soup):
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    data = [{'Heading': heading.text.strip()} for heading in headings]
    return data

def scrape_links(soup):
    links = soup.find_all('a', href=True)
    data = [{'Link Text': link.text.strip(), 'URL': link['href']} for link in links]
    return data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def scrape_data(url, data_type):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        if data_type == 'quotes':
            data = scrape_quotes(soup)
            save_to_csv(data, 'quotes.csv')
        elif data_type == 'headings':
            data = scrape_headings(soup)
            save_to_csv(data, 'headings.csv')
        elif data_type == 'links':
            data = scrape_links(soup)
            save_to_csv(data, 'links.csv')
        else:
            print("Invalid option. Please choose 'quotes', 'headings', or 'links'.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Main function to prompt user for data type and start the scraping process
if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    print("What would you like to scrape?")
    print("Options: quotes, headings, links")
    data_type = input("Choose one (quotes, headings, links): ").lower().strip()

    scrape_data(url, data_type)
