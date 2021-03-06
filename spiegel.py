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
driver.get("https://www.spiegel.de/")

#time.sleep(10)
#driver.switch_to.frame("sp_message_iframe_541484")
#driver.find_element(By.XPATH, '//button[@title="Accept and continue"]').click()


#driver.switch_to.default_content()
time.sleep(3);
field = driver.find_elements(By.XPATH, '//article')

print("start")

corona_matches = ["Corona", "Virus", "Pandemie", "Lockdown", "Impfen", "biontech", "Inzidenz", "Infiziert","Virologe", "Impfpflicht", "Impf", "2G", ]
numberOfArticles=0
numberOfCoronaArticles=0

for x in field:
    value1 = x.text
    if len(value1)>10:
        numberOfArticles=numberOfArticles+1
        if any(x in value1 for x in corona_matches):
            numberOfCoronaArticles=numberOfCoronaArticles+1
            print(value1)

print("Results")
print("Number of Corona Articles: ", numberOfCoronaArticles)
print("Number of Articles: ", numberOfArticles)
print("Percentage of Corona Articles: ", numberOfCoronaArticles/numberOfArticles)

resp = requests.get(url)

content = resp.json()

data = ["SPIEGEL", numberOfArticles, numberOfCoronaArticles, numberOfCoronaArticles/numberOfArticles, date.today(), content['weekIncidence'], content['r']['value'], content['casesPer100k'], content['casesPerWeek']]

with open('data.csv', 'a', newline='') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerow(data)


ukraine_matches = ["Ukraine", "Russland", "Putin", "Russischer", "Russische", "Ostukraine", "Kiew", "Mariopol", "Butcha", "Selenskyj", "Kharkiv", "Donbass", "Donetsk", "Luhansk ", "Odessa", "Russe", "Selenskyjs ", "Zeitenwende",]
numberOfArticlesU=0
numberOfUkraineArticles=0

for x in field:
    value1 = x.text
    if len(value1)>10:
        numberOfArticlesU=numberOfArticlesU+1
        if any(x in value1 for x in ukraine_matches):
            numberOfUkraineArticles=numberOfUkraineArticles+1
            print(value1)

print("Results - Ukraine")
print("Number of Ukraine Articles: ", numberOfUkraineArticles)
print("Number of Articles: ", numberOfArticlesU)
print("Percentage of Ukraine Articles: ", numberOfUkraineArticles/numberOfArticlesU)

dataUkraine = ["SPIEGEL", numberOfArticlesU, numberOfUkraineArticles, numberOfUkraineArticles/numberOfArticlesU, date.today()]

with open('dataUkraine.csv', 'a', newline='') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerow(dataUkraine)

driver.quit()

