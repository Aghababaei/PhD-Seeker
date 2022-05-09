# import libraries
import requests
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup as bs



# field of study you want to pursue for your PhD + presets
keywords = ['Data', 'Geosciences']



title_list = []
country_list = []
link_list = []



# www.scolarshipdb.net
fields=''
for keyword in keywords:
    fields += '{keyword}'.format(keyword=keyword)
    if keywords.index(keyword)<len(keywords)-1:
        fields += '+'

for page in range(1,3):
    url = 'https://scholarshipdb.net/scholarships/Program-PhD?page={page}&q={fields}'.format(page=page, fields=fields)
    response = requests.get(url, headers = {'User-agent': 'your bot 0.1'}, verify=False)
    soup = bs(response.text, "html.parser")
    
    titles = soup.select('h4 a')
    for title in titles:
        title_list.append((title.text).strip())


    countries = soup.select('.list-unstyled a.text-success')
    for country in countries:
        country_list.append(country.text)

    links = soup.select('.list-unstyled h4 a')
    for link in links:
        link = 'https://scholarshipdb.net'+link['href']
        link_list.append(link)




# www.findaphd.com
fields=''
for keyword in keywords:
    fields += '{keyword}'.format(keyword=keyword)
    if keywords.index(keyword)<len(keywords)-1:
        fields += '+'

for page in range(1,3):
    url = 'https://www.findaphd.com/phds/non-eu-students/?01w0&Keywords={fields}&PG={page}'.format(page=page, fields=fields)
    response = requests.get(url, headers = {'User-agent': 'your bot 0.1'}, verify=False)
    soup = bs(response.text, "html.parser")
    
    titles = soup.find_all(class_='h4 text-dark mx-0 mb-3')
    for title in titles:
        title_list.append((title.text).strip())


    countries = soup.find_all(class_='country-flag img-responsive phd-result__dept-inst--country-icon')
    for country in countries:
        country_list.append(country['title'])

    links = soup.find_all(class_='h4 text-dark mx-0 mb-3')
    for link in links:
        link = 'https://www.findaphd.com'+link['href']
        link_list.append(link)



# create excel file based on all revceived data
positions = {
    "Title": title_list,
    "Country": country_list,
    "Link": link_list
}

data = pd.DataFrame.from_dict(positions, orient='index')
data = data.transpose()

file_name = 'PhD_Positions_'+str(date.today())+'.xlsx'

writer = pd.ExcelWriter(file_name)
data.to_excel(writer, index=False)
writer.save()



