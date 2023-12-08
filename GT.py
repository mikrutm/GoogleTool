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

with st.echo():
    from selenium import webdriver
    
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