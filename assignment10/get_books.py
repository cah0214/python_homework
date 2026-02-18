from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the Durham Library search page
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

# Wait a few seconds to make sure the page loads
time.sleep(5)

# Find all li elements for search results
search_results = driver.find_elements(By.CLASS_NAME, "cp-search-result-item")
print(f"Found {len(search_results)} search results")

# Create an empty list to hold the results
results = []

# Loop through each search result
for book in search_results:
    # Extract title
    title_element = book.find_element (By.CSS_SELECTOR, "span.title-content")
    title = title_element.text

    # Extract author
    author_elements = book.find_elements (By.CSS_SELECTOR, "a.author-link")
    authors = "; ".join([author.text for author in author_elements])

    # Extract format and year
    format_year_element = book.find_element (By.CSS_SELECTOR, "span.display-info-primary")
    format_year = format_year_element.text
    
    # Store in a dictionary
    book_dict = {
        "Title": title,
        "Authors": authors,
        "Format_Year": format_year
    }

    # Append the dictionary to the results list
    results.append(book_dict)

    # Convert results to a DataFrame and print it 
    df = pd.DataFrame(results)
    print(df)

# Save results to a JSON file
df.to_csv("get_books.csv", index=False)
with open("get_books.json", "w") as f:
    json.dump(results, f, indent=4)

# Close the driver
driver.quit()

