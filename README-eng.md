# Instagram Crawler

This is a Instagram crawler which can:

(1) crawl posts with target tag

(2) crawl posts with target location ID (see below to get the location ID of a specific location)



## Getting Started

#### Prerequisites 

This is a python3 project.

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

#### (1) Crawling with Tag

If you want to crawl Instagram posts with '#cofeee' tag, you may follow: 

```bash
$ python crawler.py --mode tag --target coffee
(tags/coffee) opening url: https://www.instagram.com/explore/tags/coffee/
(tags/coffee) 70 posts to be added (merged_results: 0)
...
```

 You'll get `coffee.json` at `result/tags` right after crawling started. If you abort in the middle of crawling and resume later, the crawler automatically find where you aborted and restart from that point. 

`coffee.json` is a json dictionary with post ID as a key, and metadata as value for each Instagram post. the metadata is also a dictionary containing following keys and values:

![](C:/Users/MinsangYu/Desktop/pycharm/crawler_instagram/_src/img/json.PNG)

| Key                | Value                                |
| ------------------ | ------------------------------------ |
| id                 | a unique ID for a post               |
| owner              | a unique ID for the post owner       |
| taken_at_timestamp | timestamp of uploaded time           |
| shortcode          | abbreviated post url                 |
| text               | text                                 |
| caption            | captions                             |
| is_video           | If video, True. else False           |
| display_url        | The representative image of the post |



#### (2) Crawling with location ID

Each Instagram location has a unique location ID, and you can also crawl posts which have geo-tagged information on the location IDs. 

If you want to crawl the posts geo-tagged as 'Hapjeong station' (합정역), you may first find the location ID of the station as follows:

![Inkedlocaion_guide_01](C:/Users/MinsangYu/Desktop/pycharm/crawler_instagram/_src/img/Inkedlocaion_guide_01.jpg)



![Inkedlocaion_guide_02](C:/Users/MinsangYu/Desktop/pycharm/crawler_instagram/_src/img/Inkedlocaion_guide_02.jpg)



Numbers in the blue circle indicate the locationID we wanted. Now, you can start crawling in the similar way you crawled with tag. The results are saved in `result/locations`, and have the same format as above.

```bash
$ python crawler.py --mode location --target 251020013
(locations/251020013) opening url: https://www.instagram.com/explore/locations/2
51020013/
(locations/251020013) 24 posts to be added (merged_results: 0)
...
```



## Arguments

```bash
$ python crawler.py -h
usage: crawler.py [-h] --mode MODE --target TARGET [--limit LIMIT]

optional arguments:
  -h, --help       show this help message and exit
  --mode MODE      crawling mode among: tag, locationid
  --target TARGET  crawling target
  --limit LIMIT    Post # limit (default=1000). 0 for no limit.
```

