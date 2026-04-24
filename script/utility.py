from selenium import webdriver
from selenium.webdriver.common.by import By

class Utility:
    """
    A utility class for many things.
    """

    @staticmethod
    def scrape_data(url: str, xpaths: list, browser_type="safari", wait_time=10):
        """
        Scrapes data from a webpage using the given list of XPaths.

        Parameters:
        - url (str): The webpage URL.
        - xpaths (list): A list of XPath selectors.
        - browser_type (str): The browser to use ('safari' or 'chrome'). Default is 'safari'.
        - wait_time (int): The implicit wait time for elements to load. Default is 10 seconds.

        Returns:
        - dict: A dictionary containing extracted texts or errors for each XPath.
        """
        # Decide which WebDriver to use
        if browser_type == "safari":
            browser = webdriver.Safari()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Run without opening the browser (optional)
            browser = webdriver.Chrome(options=options)    

        print(f"Using {browser_type.capitalize()} browser...")

        results = {}

        try:
            browser.get(url)                
            browser.implicitly_wait(wait_time)

            for i, xpath in enumerate(xpaths, start=1):
                try:
                    element = browser.find_element(By.XPATH, xpath)
                    results[xpath] = element#.text
                    print(f"XPath {i}: {xpath} -> Text: {element.text}")
                except Exception as e:
                    results[xpath] = f"Error: {e}"
                    print(f"XPath {i}: {xpath} -> Error: {e}")

        except Exception as e:
            print(f"General Error: {e}")
        
        finally:
            browser.quit()
        
        return results
    

# # execução    
# import os, sys; sys.path.append(os.path.abspath("../script"))
# import utility as util  # Importing utility.py as util


# url = "https://www.boxofficemojo.com/year/world/?ref_=bo_nb_bns_tab"
# xpaths = ["//*[@id=\"table\"]/div/table[1]"]
# data = util.Utility.scrape_data(url, xpaths, browser_type="safari", wait_time=10)