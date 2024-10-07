# Author: Shriyans Bahuguna

from selenium import webdriver
import time


def get_drvier():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.timeanddate.com/worldclock/")
    return driver


def clean_text(input_text):
    lines = input_text.strip().split('\n')
    cleaned_data = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Check if the line contains a city name (non-numeric)
        if not line.isdigit() and line:
            city = line
            time_info = lines[i + 1].strip().replace(
                "", "")  # Removing the special character if any
            cleaned_data.append(f"{city}\n{time_info}")
            i += 2  # Skip to the next city block
        else:
            i += 1  # Skip numeric lines

    # Join the cleaned data with double newlines for formatting
    return '\n\n'.join(cleaned_data)


def main():
    driver = get_drvier()
    time.sleep(2)
    element = driver.find_element(
        by="xpath", value='/html/body/div[5]/section[1]/div/div[1]/div[1]/div')
    return clean_text(element.text)


print(main())
