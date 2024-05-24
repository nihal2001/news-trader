import requests
from bs4 import BeautifulSoup

# Function to extract <p> tag content and save it to a file
def extract_paragraphs_to_file(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Raise an HTTPError for bad responses
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <p> tags
        paragraphs = soup.find_all('p')

        # Open a file in write mode
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write the text from each <p> tag to the file
            for p in paragraphs:
                file.write(p.get_text() + '\n\n')

        print(f"Successfully saved the content to {output_file}")

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")

# Example usage
url = 'https://www.reuters.com/markets/us/nasdaq-sp-500-futures-pop-nvidia-fuels-chip-stocks-rally-2024-05-23/'
file_path = 'tests/ReutersArticle.txt'
extract_paragraphs_to_file(url, file_path)