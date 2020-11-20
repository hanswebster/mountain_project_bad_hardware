# Mountain Project Bad Hardware Finder
This project scrapes outdoor rock climbing routes or areas from mountainproject.com and determines if they have fixed hardware that is broken or in need of repair. Data is stored locally in a sqlite3 database.

### Requirements
* [Python 3.5 or greater](https://www.python.org/downloads/)
* [NLTK](https://pypi.org/project/nltk/)
* [Requests](https://pypi.org/project/requests/)
* [Beautiful Soup 4](https://pypi.org/project/bs4/)

### How to Run Locally
* Install Python3
* Install project requirements
* Download various packages as needed for nltk: 'ntlk.download ...' Python console makes this easy
* python3 menu.py

### Tests
* test_text_miner.py - tests sets of 1-2 sentences against text mining algorithm
* test_one_route.py - tests one route at a time 

### Further Development
* Input validation
* Text mining refinement to fix false positives (see test_one_route.py)