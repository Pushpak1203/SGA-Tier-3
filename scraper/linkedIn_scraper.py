import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from typing import Dict

def init_selenium_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver

def scrape_linkedin_profile(profile_url: str, headless=True) -> Dict:
    """
    Extract public info from a LinkedIn profile using Selenium and BeautifulSoup.
    """
    driver = init_selenium_driver(headless)

    try:
        driver.get(profile_url)
        time.sleep(5)  # wait for dynamic content

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        name = soup.find("h1")
        headline = soup.find("div", class_="text-body-medium break-words")
        location = soup.find("span", class_="text-body-small inline t-black--light break-words")

        # Education and Skills (Optional Enhancements)
        education = soup.find("span", string="Education")
        skills = soup.find_all("span", class_="pv-skill-category-entity__name-text")

        profile_data = {
            "name": name.get_text(strip=True) if name else "",
            "headline": headline.get_text(strip=True) if headline else "",
            "location": location.get_text(strip=True) if location else "",
            "skills": [skill.get_text(strip=True) for skill in skills] if skills else []
        }

        return profile_data

    except Exception as e:
        print(f"[LinkedIn Scraper Error] {e}")
        return {
            "error": str(e),
            "name": "",
            "headline": "",
            "location": "",
            "skills": []
        }

    finally:
        driver.quit()

# Example CLI usage
if __name__ == "__main__":
    url = input("Enter public LinkedIn profile URL: ")
    result = scrape_linkedin_profile(url, headless=False)
    print(result)
