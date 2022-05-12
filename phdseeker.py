#!/usr/bin/env python

# import libraries
import requests
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup as bs

# Turns off some warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# field of study you want to pursue for your PhD + presets
keywords = ['Computer Science', 'Machine Learning', 'Deep Learning',]

title_list = []
country_list = []
link_list = []

# www.scolarshipdb.net
fields='+'.join([f"\"{item.replace(' ', '+')}\""for item in keywords])
config = {'scholarshipdb': {
            'url': 'https://scholarshipdb.net/scholarships/Program-PhD?page={page}&q={fields}',
            'title': 'h4 a', "country": '.list-unstyled a.text-success', 'link': ".list-unstyled h4 a",
            'dl': "https://scholarshipdb.net",
            },
        'findaphd': {
            'url': 'https://www.findaphd.com/phds/non-eu-students/?01w0&Keywords={fields}&PG={page}',
            'title': "h4 text-dark mx-0 mb-3", 'country': "country-flag img-responsive phd-result__dept-inst--country-icon",
            'link': "h4 text-dark mx-0 mb-3",
            'dl': "https://www.findaphd.com"
            },
        }

for i in ['scholarshipdb', 'findaphd']: #
    for page in range(1,3):
        url = config[i]['url'].format(fields=fields, page=page)
        response = requests.get(url, headers = {'User-agent': 'your bot 0.1'}, verify=False)
        soup = bs(response.text, "html.parser")
        titles,countries, links  = [ soup.select(item) if i=='scholarshipdb' else soup.find_all(class_=item)
                                    for item in (config[i]['title'],config[i]['country'], config[i]['link']) ]
        for title, country, link in zip(titles, countries, links):
            title_list.append((title.text).strip().replace('"', ''))
            country_list.append(country.text if i=='scholarshipdb' else country['title'])
            link_list.append(config[i]['dl']+link['href'])

# Creates excel/csv files based on all revceived data
positions = {
    "Country": country_list,
    "Title": title_list,
    "Link": link_list
}

file_name = 'PhD_Positions_'+str(date.today())

data = pd.DataFrame.from_dict(positions, orient='index').transpose()
data.sort_values(by=['Country','Title'], inplace=True)

data.to_csv(f'{file_name}.csv', index=False)
data.to_excel(f'{file_name}.xlsx', index=False)
