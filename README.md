# scrapy
scrapy
- sudo pip install scrapy
- scrapy --help
- scrapy startproject ietf_scraper
- cd ietf_scraper/ietf_scraper/spiders
- scrapy genspider example example.com -> generates the ietf.py file
- scrapy runspider ietf.py
- scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10