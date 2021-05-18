import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/Users/sahil/Downloads/project/chromedriver')
driver.get('https://summerofcode.withgoogle.com/projects/')
names = []
project_name = []
org_name = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.find_all(attrs='project-card__right-header-content'):
  name = a.find('h2')
  if name not in names:
    names.append(name.text)

df = pd.DataFrame({'Names': names})
df.to_csv('gsoc_data.csv', index=False, encoding='utf-8')

