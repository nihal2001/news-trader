import os
import requests
from bs4 import BeautifulSoup

def get_urls_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    list_elements = soup.find_all('li', class_='js-stream-content Pos(r)')
    urls = []
    for element in list_elements:
        a_tags = element.find_all('a', href=True)
        for a_tag in a_tags:
            href = a_tag['href']
            if href.startswith('https://finance.yahoo.com'):
                urls.append(href)
    return urls

def extract_paragraphs_to_file(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        with open(output_file, 'w', encoding='utf-8') as file:
            for p in paragraphs:
                file.write(p.get_text() + '\n\n')
        print(f"Successfully saved the content to {output_file}")
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    url = 'https://finance.yahoo.com/topic/stock-market-news/'
    urls = get_urls_from_page(url)
    for url in urls:
        file_name = url.split("/")[-1] + ".txt"
        file_path = os.path.join("/shared", file_name)
        extract_paragraphs_to_file(url, file_path)
    
    with open('/shared/scraper_done.txt', 'w') as f:
        f.write('Scraping done')