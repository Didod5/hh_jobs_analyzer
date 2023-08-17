from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from config import *
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# options = webdriver.ChromeOptions()
# service = ChromeService(executable_path=driver_path)
# driver = webdriver.Chrome(service=service, options=options)
# driver.get(url=url)

# vacancies = driver.find_elements(By.CLASS_NAME, "serp-item__title")
# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# vacancies = soup.findAll('a', class_='serp-item__title')
# vacancies = [vac['href'] for vac in vacancies]

# result = []
# for ref in vacancies:
#     driver.get(ref)
#     driver.implicitly_wait(1)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     text = soup.findAll('span', class_="bloko-tag__section bloko-tag__section_text")
#     text = [el.text for el in text]
#     result.append(text)
#     # driver.close()
#     driver.implicitly_wait(5)

# with open('result.txt', 'w') as f:
#     f.write(','.join(','.join(sub_l) for sub_l in result))

with open('result.txt', 'r') as f:
    data = f.read()

data = data.split(',')
data = [el for el in data if el != '']

d = {}
for el in data:
    if not el in d:
        d[el] = 1
    else:
        d[el] += 1
print(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))

temp = 0
keys_to_del = []
for el in d:
    if 'django' in el.lower():
        temp += d[el]
        keys_to_del.append(el)
for key in keys_to_del:
    del d[key]
d['Django'] = temp

d_new = {k: v for k, v in d.items() if v > min_num_of_repeat}
labels = list(d_new.keys())
values = list(d_new.values())
plt.pie(values, labels=labels, autopct='%.2f')
plt.axis('equal')
plt.legend(labels, loc='upper left', bbox_to_anchor=(1.2, 1))
plt.savefig('skills_to_learning.png')