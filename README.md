# PhD-Seeker 🎓

PhD Seeker is a python web scraper to search for fully funded doctorate positions, advertised on well-known academic position websites.

If nowadays you are actively seeking a PhD position to pursue your studies, you must have realized that the process of searching for relevant vacancies is not straight forward. Visiting a large number of position advertising websites and encountering irrelevant commercials are two of the most common problems.

Simply modify the keywords and you will receive a CSV/XLSX file containing the last two pages from the most popular advertisers.

# Sources 📚
- [www.scholarshipdb.net](http://www.scholarshipdb.net  "www.scholarshipdb.net")
- [www.findaphd.com](http://www.findaphd.com "www.findaphd.com")


# Next Goals 🎯
- [ ] Expanding the academic position advertising source
- [ ] Adding databases of different universities
- [ ] Finding and removing overlapped positions
- [ ] Adding LinkedIn search to get informed directly from university professors
- [X] Getting the keywords from command line instead of hard-coding the source
- [X] Fetching pages simultaneously
- [ ] GUI support

# Usage
```
python phdseeker-cli -k 'Computer Science, Machine Learning'
```

# Requirements
```
pip install docopt http3 httpx brotlipy
```
