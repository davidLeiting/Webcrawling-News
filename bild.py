import time
import csv
from datetime import date
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://api.corona-zahlen.org/germany"

s=Service("C:\selenium browser driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.bild.de/")

time.sleep(5)
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="SP Consent Message"]'))
driver.find_element(By.XPATH, '//button[@title="Alle akzeptieren"]').click()

driver.switch_to.default_content()
time.sleep(3);
field = driver.find_elements(By.XPATH, '//article')

print("start")

corona_matches = ["Corona", "Virus", "Pandemie", "Lockdown", "Impfen", "biontech", "Inzidenz", "Infiziert","Virologe", "Impfpflicht", "Impf", "2G", ]
numberOfArticles=0
numberOfCoronaArticles=0

for x in field:
    value1 = x.text
    value2 = "Heute ist Corona Virus Tag"
    if len(value1)>10:
        numberOfArticles=numberOfArticles+1
        if any(x in value1 for x in corona_matches):
            numberOfCoronaArticles=numberOfCoronaArticles+1
            print(value1)

print("Results")
print("Number of Corona Articles: ",  numberOfCoronaArticles)
print("Number of Articles: ",  numberOfArticles)
print("Percentage of Corona Articles: ", numberOfCoronaArticles/numberOfArticles)

resp = requests.get(url)

content = resp.json()

data = ["BILD", numberOfArticles, numberOfCoronaArticles, numberOfCoronaArticles/numberOfArticles, date.today(), content['weekIncidence'], content['r']['value'], content['casesPer100k'], content['casesPerWeek']]

with open('../data.csv', 'a', newline='') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerow(data)

driver.quit()

