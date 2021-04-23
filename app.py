import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
XPATH = "//*[@class='ui-mainview-block eventpath-wrapper']"
TIMEOUT = 20

st.title("Test Selenium")
st.markdown("You should see some random Football match text below in about 21 seconds")

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

try:
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                XPATH,
            )
        )
    )

except TimeoutException:
    st.warning("Timed out waiting for page to load")
    driver.quit()

time.sleep(10)
elements = driver.find_elements_by_xpath(XPATH)
st.write([el.text for el in elements])
driver.quit()
