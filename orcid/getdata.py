from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a WebDriver instance (e.g. Chrome or Firefox)
driver = (
    webdriver.Firefox()
)  # You may need to download and install a driver for your specific browser

# Navigate to the webpage that requires JavaScript
url = "https://orcid.org/0000-0003-1452-609X"
driver.get(url)

works = driver.find_elements(By.CSS_SELECTOR, "app-work-stack.ng-star-inserted")

# save title, journal, year, doi, authors
title = []
journal = []
date = []
doi = []
authors = []
work_type = []

works_text = [w.text.split("\n") for w in works]

for wt in works_text:
    title.append(wt[0])
    journal.append(wt[1])
    date.append(wt[2].split("|")[0])
    work_type.append(wt[2].split("|")[1])
    doi.append(wt[3].split(": ")[1])
    authors.append([e for e in wt if re.match(r"CONTRIBUTORS: ", e)][0].split(": ")[1])

# Close the WebDriver instance

driver.quit()


#### funcs

import re

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_works_from_orcid(url):
    # Create a WebDriver instance (e.g. Chrome or Firefox)
    driver = (
        webdriver.Firefox()
    )  # You may need to download and install a driver for your specific browser

    # Navigate to the webpage that requires JavaScript
    driver.get(url)

    works = driver.find_elements(By.CSS_SELECTOR, "app-work-stack.ng-star-inserted")

    # save title, journal, year, doi, authors
    title = []
    journal = []
    date = []
    doi = []
    authors = []
    work_type = []

    works_text = [w.text.split("\n") for w in works]

    for wt in works_text:
        title.append(wt[0])
        journal.append(wt[1])
        date.append(wt[2].split("|")[0])
        work_type.append(wt[2].split("|")[1])
        doi.append(wt[3].split(": ")[1])
        authors.append(
            [e for e in wt if re.match(r"CONTRIBUTORS: ", e)][0].split(": ")[1]
        )

    # Close the WebDriver instance
    driver.quit()

    # Return the scraped data as a dictionary
    scraped_data = {
        "title": title,
        "journal": journal,
        "date": date,
        "work_type": work_type,
        "doi": doi,
        "authors": authors,
    }

    return scraped_data


# Example usage:
url = "https://orcid.org/0000-0003-1452-609X"
result = scrape_works_from_orcid(url)
print(result)
result = scrape_works_from_orcid(url)
print(result)
