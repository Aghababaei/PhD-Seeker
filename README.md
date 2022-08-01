# PhD-Seeker 🎓

[![code size](https://img.shields.io/github/languages/code-size/Aghababaei/PhD-Seeker?style=social)](https://github.com/Aghababaei/PhD-Seeker/archive/master.zip)
[![GitHub forks](https://img.shields.io/github/forks/Aghababaei/PhD-Seeker?style=social)](https://github.com/Aghababaei/PhD-Seeker/network/members)
[![GitHub license](https://img.shields.io/github/license/Aghababaei/PhD-Seeker?style=social)](https://github.com/Aghababaei/PhD-Seeker/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Aghababaei/PhD-Seeker?style=social)](https://github.com/Aghababaei/PhD-Seeker/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Aghababaei/PhD-Seeker?style=social)](https://github.com/Aghababaei/PhD-Seeker/issues)


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
python phdseeker-cli.py

Usage:
    python phdseeker-cli.py -h
    python phdseeker-cli.py -V
    python phdseeker-cli.py [-k <keywords> --maxpage=<n> --output=<filetype(s)> -v]

options:
    -h --help                       Show this screen.
    -V --version                    Show version.
    -v --verbose                    Show the sought position on the terminal.
    -k <keywords>, --keywords=<keywords>    Declare desired keywords to seek. [default: Computer Science, Machine Learning, Deep Learning]
    -o <filetype(s)>, --output=<filetype(s)>     Set the output type csv/xlsx/both [default: both]
    --maxpage=<n>                   Maximum number of pages to fetch. [default: 10]
```
### usage example
```
python phdseeker-cli.py -k 'Computer Science, Machine Learning' --maxpage=1 -v

---------------------------------scholarshipdb----------------------------------
719 positions found in 'Computer Science, Machine Learning'                      
Page 1 has been fetched from https://scholarshipdb.net!
------------------------------------findaphd------------------------------------
64 positions found in 'Computer Science, Machine Learning'                      
Page 1 has been fetched from https://www.findaphd.com!
Elapsed time is 3.49 seconds.
┏━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    ┃ Country        ┃ Date               ┃ Title                             ┃
┡━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0  │ Australia      │                    │ Doctoral / Post-Doctoral Position │
│    │                │                    │ in Computer Science               │
│ 1  │ Belgium        │                    │ PhD Studentship in Computer       │
│    │                │                    │ Science                           │
│ 2  │ Canada         │ 10 days ago        │ Master’s and PhD students         │
│ 3  │ China          │                    │ Discovery of new materials for    │
│    │                │                    │ applications on glass using Deep  │
│    │                │                    │ Machine Learning and Data         │
│    │                │                    │ Analytics                         │
│ 4  │ China          │                    │ PhD in deep learning for          │
│    │                │                    │ biomedical images of the pelvic   │
│    │                │                    │ floor                             │
│ 5  │ China          │                    │ PhD opportunities in Computer     │
│    │                │                    │ Science at Brunel University      │
│    │                │                    │ London                            │
│ 6  │ China          │                    │ SFI Centre for Research Training  │
│    │                │                    │ in Machine Learning               │
│ 7  │ Cyprus         │                    │ SFI Centre for Research Training  │
│    │                │                    │ in Machine Learning               │
│ 8  │ Germany        │ about 17 hours ago │ PhD Position in Artificial        │
│    │                │                    │ Intelligence, Chair of            │
│    │                │                    │ Information Systems Research      │
│ 9  │ Germany        │ 6 days ago         │ PhD Student/Research Assistant at │
│    │                │                    │ Software Lab (SOLA)               │
│ 10 │ Germany        │                    │ Machine Learning Meets Sequential │
│    │                │                    │ Monte Carlo Methods               │
│ 11 │ Israel         │ 19 days ago        │ PhD student position              │
│ 12 │ Norway         │ 2 months ago       │ PhD Research Fellow in            │
│    │                │                    │ Informatics - Knowledge           │
│    │                │                    │ Representation and Machine        │
│    │                │                    │ Learning                          │
│ 13 │ Norway         │ 3 months ago       │ PhD Fellow in Computer Science -  │
│    │                │                    │ Efficient distributed machine     │
│    │                │                    │ learning                          │
│ 14 │ Poland         │                    │ The Constitutive Law              │
│    │                │                    │ Establishment of Advanced High    │
│    │                │                    │ Strength Steel based on Machine   │
│    │                │                    │ Learning                          │
│ 15 │ Spain          │ 4 days ago         │ CALL 41-2022-1 Researcher in the  │
│    │                │                    │ Sustainable Artificial            │
│    │                │                    │ Intelligence (SAI) research unit  │
│ 16 │ Sweden         │ about 15 hours ago │ PhD student in Computational      │
│    │                │                    │ Science and Engineering with      │
│    │                │                    │ focus on Optimization for         │
│    │                │                    │ Federated Machine Learning        │
│ 17 │ Switzerland    │ about 2 months ago │ PhD position in the field of      │
│    │                │                    │ Machine Learning (Graph-based     │
│    │                │                    │ High-dimensional generative       │
│    │                │                    │ models) with application to       │
│    │                │                    │ Medical Data Analysis at the      │
│    │                │                    │ Department of Computer Science    │
│ 18 │ United Kingdom │                    │ SFI Centre for Research Training  │
│    │                │                    │ in Machine Learning               │
│ 19 │ United Kingdom │                    │ Scholarship for the PhD in        │
│    │                │                    │ Medical Sciences in the fields of │
│    │                │                    │ Neuroscience and Biomedical       │
│    │                │                    │ Engineering for the PhD Research  │
│    │                │                    │ Project ‘Development of a         │
│    │                │                    │ closed-loop controller for        │
│    │                │                    │ automatic administration of       │
│    │                │                    │ anaesthetic and analgesic agents  │
│    │                │                    │ during surgery using machine      │
│    │                │                    │ learning methods’                 │
│ 20 │ United States  │ 19 days ago        │ Fully Funded PhD Positions in     │
│    │                │                    │ Artificial Intelligence, Machine  │
│    │                │                    │ Learning, Wireless Communication  │
│    │                │                    │ -- Mississippi State University   │
└────┴────────────────┴────────────────────┴───────────────────────────────────┘
                     All 21 found positions are shown here.
```

# Requirements
```
pip install docopt http3 httpx brotlipy
```
