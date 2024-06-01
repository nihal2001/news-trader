from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# URL of the news article
url = "https://www.reuters.com/markets/us/nasdaq-sp-500-futures-pop-nvidia-fuels-chip-stocks-rally-2024-05-23/"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get(url)

# Give the page some time to load
driver.implicitly_wait(10)  # Adjust the wait time as necessary

# Get the page source
html_content = driver.page_source

# Print the HTML content
print(html_content)

# Close the browser
driver.quit()
