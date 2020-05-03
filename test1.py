from itertools import count

from bs4 import BeautifulSoup
import requests
with open("data_country.txt", "w") as file:

    response = requests.get('https://www.worldometers.info/coronavirus/')
    # print(response)https://www.worldometers.info/coronaviru
    print('response status code:', response.status_code)
    # print('text:',response.text)
    text_website = response.text
    # my_table = text_website.find('<table id ="main_table_countries')
    # print(my_table)
    html_doc = """
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
    # print(soup.prettify())
    soup.find_all('main_table_countries')
    table_list = soup.find_all('table', attrs={"id": "main_table_countries_today"})
    print("table list numbers: ", len(table_list))

    table = table_list[0]
    # print("table:",table)
    tbody = table.find('tbody')
    print("tbody", tbody)
    tr_list = tbody.find_all('tr')
    print("number of trs in table:", len(tr_list))
    print(tr_list[0])
    # first country in list
    tr = tr_list[0]
    td_list = tr.find_all('td')
    # print("North America tds:", td_list)

    td_list_text = []
    count = 0
    for this_td in td_list:
        this_td_text = this_td.text

        if count not in [0, 2, 6, 8, 11, 12]:
            this_td_text = this_td_text.replace(',', '')
            # this_td_text = float(this_td_text)

        if count == 11 & 12:
            this_td_text = this_td_text.replace('.', '')
            # this_td_text = int (this_td_text)

        td_list_text += [
            this_td_text
        ]

        count += 1
    print("td_list_text:", td_list_text)
    for i in td_list_text:
        file.write(str(i)+',')
    file.write('\n')
    # file.write(td_list_text)
    # first_td = td_list[0]
    # first_td_text = first_td.text
    # print("first_td_text:", first_td_text)
