
import os
import shutil

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@st.cache_resource(show_spinner=False)
def get_logpath():
    return os.path.join(os.getcwd(), 'selenium.log')


@st.cache_resource(show_spinner=False)
def get_chromedriver_path():
    return shutil.which('chromedriver')


@st.cache_resource(show_spinner=False)
def get_webdriver_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    return options


def get_webdriver_service(logpath):
    service = Service(
        executable_path=get_chromedriver_path(),
        log_output=logpath,
    )
    return service


def delete_selenium_log(logpath):
    if os.path.exists(logpath):
        os.remove(logpath)


def show_selenium_log(logpath):
    if os.path.exists(logpath):
        with open(logpath) as f:
            content = f.read()
            st.code(body=content, language='log', line_numbers=True)
    else:
        st.warning('No log file found!')


def run_selenium(logpath):
    name = str()
    with webdriver.Chrome(options=get_webdriver_options(), service=get_webdriver_service(logpath=logpath)) as driver:
        url = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
        driver.get(url)
        xpath = '//*[@class="ui-mainview-block eventpath-wrapper"]'
        # Wait for the element to be rendered:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_elements(by=By.XPATH, value=xpath))
        name = element[0].get_property('attributes')[0]['name']
    return name


if __name__ == "__main__":
    logpath=get_logpath()
    delete_selenium_log(logpath=logpath)
    st.set_page_config(page_title="Selenium Test", page_icon='✅',
        initial_sidebar_state='collapsed')
    st.title('🔨 Selenium on Streamlit Cloud')
    st.markdown('''This app is only a very simple test for **Selenium** running on **Streamlit Cloud** runtime.<br>
        The suggestion for this demo app came from a post on the Streamlit Community Forum.<br>
        <https://discuss.streamlit.io/t/issue-with-selenium-on-a-streamlit-app/11563><br><br>
        This is just a very very simple example and more a proof of concept.<br>
        A link is called and waited for the existence of a specific class to read a specific property.
        If there is no error message, the action was successful.
        Afterwards the log file of chromium is read and displayed.
        ''', unsafe_allow_html=True)
    st.markdown('---')

    st.balloons()
    if st.button('Start Selenium run'):
        st.warning('Selenium is running, please wait...')
        result = run_selenium(logpath=logpath)
        st.info(f'Result -> {result}')
        st.info('Successful finished. Selenium log file is shown below...')
        show_selenium_log(logpath=logpath)
"""
import streamlit  as st
from selenium import webdriver
import matplotlib.pyplot as plt
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import csv 
import re
import sys 
from pathlib import Path
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from os.path import dirname, abspath
from selenium.webdriver.firefox.options import Options
import streamlit  as st
st.title('Google Tool')
    
@st.cache_resource
def get_driver():
    return webdriver.Firefox()
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
driver = get_driver()
wait =  WebDriverWait(driver, 12);
st.code(driver.page_source)
days_back_then =  7
base="light"
st.title('Google Tool')
st.subheader("Damn")
driver.get('https://trends.google.pl/trends/trendingsearches/daily?geo=PL')
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cookieBarConsentButton")))
element.click()


import streamlit  as st
from selenium import webdriver
import matplotlib.pyplot as plt
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import csv 
import re
import sys 
from pathlib import Path
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from os.path import dirname, abspath
from selenium.webdriver.firefox.options import Options


options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')


days_back_then =  7
base="light"
st.title('Google Tool')
st.subheader("Damn")

#initialize driver

wait =  WebDriverWait(driver, 12);

#open site 
driver.get('https://trends.google.pl/trends/trendingsearches/daily?geo=PL')

#define timeframe we want to scrap -  days_back_then 


#close popup with cookies
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cookieBarConsentButton")))
element.click()



#main loop 
for i in range(0,days_back_then):
    #time.sleep(3) # in case of slow internet connection
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "feed-load-more-button")))
    element.click()
#class_objects= wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'content-header-title')))
class_objects  = driver.find_elements(By.CLASS_NAME, 'content-header-title')
#collect data 

items  = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "feed-item-header")))
items  = driver.find_elements(By.CLASS_NAME,  "feed-item-header")

items_count = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-count-title"))) 
items_count = driver.find_elements(By.CLASS_NAME,"search-count-title") 

items_string = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary-text")))
items_string = driver.find_elements(By.CLASS_NAME,"summary-text")

items_source = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "source-and-time")))
items_source = driver.find_elements(By.CLASS_NAME,"source-and-time" )

# printing dates 
dates = [ class_object.text for class_object in class_objects ]

for d in dates:
    print(d)


def return_mnoz(string):
    if "tys." in string:
        return 1000
    if "mln" in string:
        return 1000000

#transformation and extraction data

items_list = [  item.get_attribute('target-id')[10:] for item in items]

count_list = [ int(str(re.findall(r'\d+', count.text)[0]))*return_mnoz(count.text)  for count in items_count]

i_s = [c.text for c  in items_string]
i_c = [c.text for c  in items_source]

#data to dataframe 
google_dict = {}
df = pd.DataFrame()
df["Trend"] = items_list
df["Value"] = count_list
df["Trend description"] = i_s
df["Source"] = [a[:-11] for a in  i_c]
#print(df)
st.dataframe(df)

#addition of values if we have douplicates in trends  (same trend in 2 or more days)

for i in range(0,len(items_list)):
    
    if items_list[i] not in google_dict.keys():
        google_dict[items_list[i]] = count_list[i] 
    else : 
        google_dict[items_list[i]] += count_list[i]
 
#bardzo brzydko, nie robić takiego nazewnictwa ale działa i nie ruszałem 
dict_google = google_dict
dict_google = dict(sorted(dict_google.items(), key=lambda item: item[1]))
names = list(dict_google.keys())[-22:]
values = list(dict_google.values())[-22:]

#saving data, top 22 in another csv and all scraped data to other file 
#data_folder = Path(dname) / "data"
#file_top = data_folder / "top_google_trends.csv"
#with open(file_top, 'w') as f:
#    writer = csv.writer(f)
#    writer.writerows(zip(names, values))
#
#file_dataframe = data_folder / "trends_dataframe.csv"
#df.to_csv(file_dataframe)

driver.close()


#os.system(f"python3 {Path(dname)}/monitorowane/GT_filter_and_plot.py")
#sometimes usefull
#plt.barh(range(len(values)), values, tick_label=names)
#plt.show()


"""