from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

def scrape_and_parse(industry = None):
    '''
    Scrapes 10times.com/usa for upcoming industry events that align with the specifications in **industry**.

    Args:
        - industry (list)       :   industry argument to pass to the get request
    
    Returns:
        - E (pd.DataFrame)      :   df of scraped event data + urls
    '''

    # SCRAPING
    options = Options()
    options.add_argument('--headless')
    options.set_preference("dom.push.enabled", False)
    browser = webdriver.Firefox(options=options)

    url = "https://10times.com/usa" + f"/{industry}"

    browser.get(url)

    events = browser.find_elements(By.XPATH, '//tr[contains(@class, "event-card")]')
    E = []
    for e in events:
        l = e.get_attribute('onclick')
        l = l.split('\'')[1]

        elems = [e.text, l]
        E.append(elems)

    browser.quit()


    # PARSING
    df = pd.DataFrame(data=E, columns=['data', 'url'])
    return df