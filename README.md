# Instagram tag Crawler

## Getting Started

#### Prerequisites 

```
beautifulsoup4==4.9.0
soupsieve==2.0
```



#### (Optional) Virtual environment setting

```bash
$ virtualenv venv -p python3
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```



## Running the tests

```bash
(venv) $ python3 tag_cralwer --tag coffee
(coffee) opening url: https://www.instagram.com/explore/tags/coffee/
(coffee) 72 posts to be added (merged_results: 0)
...
```

You may find the result in `coffee.json` .

#### 

## Arguments

```bash
$ python tag_crawler.py -h
usage: tag_crawler.py [-h] --tag TAG [--limit LIMIT]

optional arguments:
  -h, --help     show this help message and exit
  --tag TAG      An Instagram tag to crawl
  --limit LIMIT  Post number limit (default=1000). 0 for no limit.
```

