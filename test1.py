from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.worldometers.info/coronavirus/')
# print(response)
print('response status code:', response.status_code)
print('text:',response.text)
# text_website=response.text
# my_table=text_website.find('<table id ="main_table_countries')
# print(my_table)
text_website = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(text_website, 'html.parser')
# print(soup.prittify())
table_list = soup.find_all('table',attrs={"id":"main_table_countries"})