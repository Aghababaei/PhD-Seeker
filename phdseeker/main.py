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
                'sought#': 'h1.title',
                'query': 'https://scholarshipdb.net/scholarships/Program-PhD?page={page}&q={fields}',
                'title': 'h4 a',
                'country': '.list-unstyled a.text-success',
                'date': '.list-unstyled span.text-muted',
                'link': ".list-unstyled h4 a",
                },
            'findaphd': {
                'sought#': 'h4.course-count.d-none.d-md-block.h6.mb-0.mt-1',
                'query': 'https://www.findaphd.com/phds/non-eu-students/?01w0&Keywords={fields}&PG={page}',
                'title': "h4 text-dark mx-0 mb-3",
                'country': "country-flag img-responsive phd-result__dept-inst--country-icon",
                'date': "apply py-2 small",
                'link': "h4 text-dark mx-0 mb-3",
                },
            }

    def __init__(self, repo='scholarshipdb'):
        self.repo = repo

    @classmethod
    def repos(cls):
        return ','.join([repo for repo in cls.config])

    @property
    def query(self):
        return Config.config[self.repo]['query']

    @property
    def sought(self):
        return Config.config[self.repo]['sought#']

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
    def date(self):
        return Config.config[self.repo]['date']

    @property
    def baseURL(self):
        return next(re.finditer(r'^.+?[^\/:](?=[?\/]|$)', Config.config[self.repo]['query'])).group()


class PhDSeeker:
    def __init__(self, keywords: str, repos: str='scholarshipdb, findaphd', maxpage: int=10):
        self.repos = map(str.strip, repos.split(',')) # 'scholarshipdb, findaphd'
        self.keywords = keywords
        self.fields='%20'.join([f"\"{item.replace(' ', '%20')}\""
                                for item in map(str.strip, keywords.split(','))])
        self.titles = []
        self.countries = []
        self.dates = []
        self.links = []
        self.maxpage = maxpage+1
        self.file_name = 'PhD_Positions_'+str(date.today())
        self.sought_number = 0

    def __str__(self):
        if self.sought_number:
            s = ('='*80+'\n#') + 'Sought Ph.D. Positions'.center(78) + ('#\n'+'='*80+'\n')
            return s + self.df.to_csv(index=False)

    def prepare(self):
        headers = {'user-agent': 'curl/7.83.0', 'accept': '*/*', 'scheme': 'https'}
        for repo in self.repos:
            c = Config(repo)
            print(f"{repo.center(80, '-')}")
            for page in range(1,self.maxpage):
                try:
                    query = c.query.format(fields=self.fields, page=page)
                    # print(query)
                    response = requests.get(query, headers = headers, verify=False)
                    soup = bs(response.text, "html.parser")
                    if page==1: # get the number of sought positions
                        if (n:= soup.select_one(c.sought)) is not None:
                            self.sought_number = int(re.search('(\d+)', n.text).group(1))
                        print(f"{self.sought_number} positions found in '{self.keywords}'")
                    titles, countries, dates, links  = [ soup.select(item) if repo=='scholarshipdb' else soup.find_all(class_=item)
                                                for item in (c.title, c.country, c.date, c.link) ]
                    assert titles!=[], 'No titles found'
                    for title, country, date, link in zip(titles, countries, dates, links):
                        self.titles.append((title.text).strip())
                        self.countries.append(country.text if repo=='scholarshipdb' else country['title'])
                        self.dates.append(date.text.replace('\n', ''))
                        self.links.append(c.baseURL+link['href'])
                except AssertionError:
                    break
                except Exception as e:
                    print(e)
                    break
                finally:
                    if self.sought_number:
                        print(f"\r{page} pages have been fetched from {c.baseURL}!", end="")
            print()

    @property
    def positions(self,):
        self.prepare()
        positions = { "Country": self.countries, "Date": self.dates, "Title": self.titles, "Link": self.links }
        self.df = pd.DataFrame.from_dict(positions, orient='index').transpose()
        self.df.sort_values(by=['Country','Title'], inplace=True)
        return self.df

    def save(self, output='both'):
        # Creates excel/csv files based on all revceived data
        df = self.positions
        if output in ('csv', 'both'):
            df.to_csv(f'{self.file_name}.csv', index=False)
        if output in ('xlsx', 'both'):
            df.to_excel(f'{self.file_name}.xlsx', index=False)


def main():
    # Comma seperated list of keywords for the field of desired PhD career + presets
    keywords = 'Computer Science, Machine Learning, Deep Learning'

    ps = PhDSeeker(keywords, maxpage=10)
    ps.save()

if __name__=="__main__":
    main()