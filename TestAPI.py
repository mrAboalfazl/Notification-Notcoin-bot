# #import Library
# import time
# import json
# import requests
# from datetime import datetime
# from urllib.parse import urlencode
# import urllib.parse




# # Function to make the HTTP request and return the response data
# def fetch_data():
#     url = 'https://clicker-api.joincommunity.xyz/auth/webapp-session'
#     headers = {
#         'accept': 'application/json',
#         'accept-language': 'en-US,en;q=0.9',
#         'content-type': 'application/json',
#         'origin': 'https://farm.joincommunity.xyz',
#         'priority': 'u=1, i',
#         'referer': 'https://farm.joincommunity.xyz/',
#         'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
#     }

#     data = {
#             "webAppData":"query_id=AAEfP1wsAgAAAB8_XCzu75hJ&user=%7B%22id%22%3A5039210271%2C%22first_name%22%3A%22PLATFORM%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22platform2019%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1722167048&hash=1d9dc8d39a57c286bf7eb00eebd2f8ddf1742a1c547494819a59558f4642faef"
#             }
#     response = requests.post(url, headers=headers, json=data)

    
#     # Print the received JSON response
#     response_json = response.json()
#     print(json.dumps(response_json, indent=4))
    
#     return response_json


# response_data = fetch_data()

###############################################################################
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url_main_page = "https://farm.joincommunity.xyz/benefits"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome()
driver.get()



time.sleep(5)
element = driver.find_element(By.CLASS_NAME, "_container_uk60i_1")
sub_elements = element.find_elements(By.CLASS_NAME, "_root_1xl6z_1")

print(f"Elemnt :{element}")
print()
print(f"SubElements : {sub_elements}")
active_name = []
for sub in sub_elements : 
    title = sub.find_element(By.CLASS_NAME, '_title_1xl6z_82')
    active_name.append(title.text)

print(active_name)


