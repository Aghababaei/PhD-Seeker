#!/usr/bin/env python

# import libraries
import re
import requests
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup as bs

# Turns off some warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Config:
    config = {'scholarshipdb': {
                'query': 'https://scholarshipdb.net/scholarships/Program-PhD?page={page}&q={fields}',
                'title': 'h4 a',
                'country': '.list-unstyled a.text-success',
                'link': ".list-unstyled h4 a",
                },
            'findaphd': {
                'query': 'https://www.findaphd.com/phds/non-eu-students/?01w0&Keywords={fields}&PG={page}',
                'title': "h4 text-dark mx-0 mb-3",
                'country': "country-flag img-responsive phd-result__dept-inst--country-icon",
                'link': "h4 text-dark mx-0 mb-3",
                },
            }

    def __init__(self, repo='scholarshipdb'):
        self.repo = repo

    @property
    def query(self):
        return Config.config[self.repo]['query']

    @property
    def title(self):
        return Config.config[self.repo]['title']

    @property
    def link(self):
        return Config.config[self.repo]['link']

    @property
    def country(self):
        return Config.config[self.repo]['country']

    @property
    def baseURL(self):
        return next(re.finditer(r'^.+?[^\/:](?=[?\/]|$)', Config.config[self.repo]['query'])).group()


class PhDSeeker:
    def __init__(self, keywords: str, repos: str='scholarshipdb, findaphd', maxpagenumber: int=10):
        self.repos = map(str.strip, repos.split(',')) # 'scholarshipdb, findaphd'
        self.fields='+'.join([f"\"{item.replace(' ', '+')}\""
                                for item in map(str.strip, keywords.split(','))])
        self.titles = []
        self.countries = []
        self.links = []
        self.maxpagenumber = maxpagenumber+1
        self.file_name = 'PhD_Positions_'+str(date.today())

    def prepare(self):
        for repo in self.repos:
            c = Config(repo)
            for page in range(1,self.maxpagenumber):
                try:
                    query = c.query.format(fields=self.fields, page=page)
                    response = requests.get(query, headers = {'User-agent': 'your bot 0.1'}, verify=False)
                    soup = bs(response.text, "html.parser")
                    titles, countries, links  = [ soup.select(item) if repo=='scholarshipdb' else soup.find_all(class_=item)
                                                for item in (c.title, c.country, c.link) ]
                    assert titles!=[]
                    for title, country, link in zip(titles, countries, links):
                        self.titles.append((title.text).strip().replace('"', ''))
                        self.countries.append(country.text if repo=='scholarshipdb' else country['title'])
                        self.links.append(c.baseURL+link['href'])
                except Exception as e:
                    break
                finally:
                    print(f"\r{page} pages have been fetched from {c.baseURL}!", end="")
            print()

    @property
    def positions(self,):
        self.prepare()
        return { "Country": self.countries, "Title": self.titles, "Link": self.links }

    def save(self):
        # Creates excel/csv files based on all revceived data
        data = pd.DataFrame.from_dict(self.positions, orient='index').transpose()
        data.sort_values(by=['Country','Title'], inplace=True)
        data.to_csv(f'{self.file_name}.csv', index=False)
        data.to_excel(f'{self.file_name}.xlsx', index=False)


def main():
    # Comma seperated list of keywords for the field of desired PhD career + presets
    keywords = 'Computer Science, Machine Learning, Deep Learning'

    ps = PhDSeeker(keywords)
    ps.save()

if __name__=="__main__":
    main()