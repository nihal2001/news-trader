import requests
from bs4 import BeautifulSoup

# URL of the news article
url = "https://www.reuters.com/markets/us/nasdaq-sp-500-futures-pop-nvidia-fuels-chip-stocks-rally-2024-05-23/"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the content of the response
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Pretty print the HTML content (optional)
    pretty_html = soup.prettify()
    print(pretty_html)

    # If you want to extract specific information, for example, the article text
    article_text = soup.find('div', class_='article-body__content__3tV4E').get_text(strip=True)
    print(article_text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
