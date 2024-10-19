from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set the correct path to ChromeDriver
service = Service("C:/Users/PC/Downloads/chromedriver-win64 (2)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the target website
driver.get("https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_ads")

while True:
    try:
        # Click the 'View' button
        view_button = driver.find_element(By.XPATH, '//*[@id="viewAdsTOffers1"]/tbody/tr/td[4]/div/a[1]/span/input')
        view_button.click()

        # Wait 10 seconds for the ad in the new tab
        time.sleep(10)

        # Close the new tab if it opened
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()

        # Switch back to the main tab
        driver.switch_to.window(driver.window_handles[0])

        # Wait 5 seconds for the page to refresh
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}. Retrying...")
        time.sleep(5)  # Wait before retrying
