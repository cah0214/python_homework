from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time

# 1. Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Open the OWASP top 10 page
driver.get("https://owasp.org/www-project-top-ten/")
time.sleep(5)

# 3. Find all top‑10 links using XPath
vuln_elements = driver.find_elements(
    By.XPATH,
    "//a[contains(@href,'/Top10/2025/')]"
)

# 4. Extract titles and links
owasp_list = []
for v in vuln_elements:
    title = v.text
    link = v.get_attribute("href")
    owasp_list.append({"Title": title, "Link": link})

# 5. Print to verify
print(owasp_list)

# 6. Save to CSV
df = pd.DataFrame(owasp_list)
df.to_csv("owasp_top_10.csv", index=False)

# 7. Save to JSON
with open("owasp_top_10.json", "w") as f:
    json.dump(owasp_list, f, indent=4)

# 8. Clean up
driver.quit()
