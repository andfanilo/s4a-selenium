import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
XPATH = "//*[@class='ui-mainview-block eventpath-wrapper']"
TIMEOUT = 20

# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk("/home/appuser/.conda/"):
    st.markdown('Found directory: %s' % dirName)
    for fname in fileList:
        st.markdown('\t%s' % fname)

st.title("Test Selenium")
st.markdown("You should see some random Football match text below in about 21 seconds")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
driver = webdriver.Firefox(options=firefoxOptions, executable_path='/home/appuser/.conda/lib/python3.7/site-packages/selenium/webdriver')
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
