from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import csv

 

options = Options()

options.headless = True

options.add_argument("--window-size=1400,900")

 

driver = webdriver.Chrome(options=options)

 

driver.get('https://wonder.cdc.gov/controller/saved/D176/D364F710')

 

import time

 

try:

    # Wait for the 'I Agree' button to be clickable and click it

    button = WebDriverWait(driver, 10).until(

        EC.element_to_be_clickable((By.NAME, 'action-I Agree'))

    )

    button.click()

 

    # Wait for the 'Send' button to be clickable and click it

    button = WebDriverWait(driver, 10).until(

        EC.element_to_be_clickable((By.NAME, 'action-Send'))

    )

    button.click()

 

    # Allow time for the CDC Wonder report to load

    time.sleep(2)

 

    # Find the table element by class name 'response-form'

    table = driver.find_element(By.CLASS_NAME, 'response-form')

 

    # Extract rows from the data table

    table_rows = table.find_elements(By.TAG_NAME, 'tr')

 

    # Create list for export to .csv

    data = []

 

    # Iterate through rows, extract text from each cell

    for row in table_rows:

        cells = row.find_elements(By.TAG_NAME, 'th' or 'td')

        row_data = []

        for cell in cells:

            row_data.append(cell.text)  # Append cell text to row_data

        data.append(row_data)

 

    import os

 

    # Get the user's desktop path

    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

 

    # Name .csv export on the desktop

    csv_file = os.path.join(desktop_path, 'active_cdcwonderscrape_1.csv')

 

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerows(data)

 

    print(f'Data has been saved to {csv_file}')

 

except Exception as e:

    print(f"Error encountered during scraping: {e}")

 

finally:

    # Keep the browser open for manual interaction

    driver.quit()
