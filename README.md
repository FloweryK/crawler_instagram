# 인스타그램 크롤러

[English translation](README-eng.md)

인스타그램을 크롤링해주는 봇입니다. 

현재 구현된 기능은 다음과 같습니다:

(1) 원하는 태그를 지정해 최근 포스트부터 크롤링 하기



추가 될 기능들:

(1) 원하는 지역을 위도, 경도로 지정하여 지역 내 인스타그램 포스트를 크롤링하기





## 시작하기에 앞서

#### 요구사항

본 프로젝트는 python3 와 아래 라이브러리로 쓰여졌습니다. 

```
beautifulsoup4==4.9.0
soupsieve==2.0
```



#### (선택) 가상환경 사용하기

원한다면 가상환경을 만들어 실행할 수 있습니다. 깔끔한 라이브러리 관리가 가능하므로, 가상환경을 사용하시는 걸 추천드립니다!

```bash
$ virtualenv venv -p python3
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```





## 사용하는 법

예를 들어 'coffee'라는 태그를 가진 포스트들을 크롤링해보려고 한다면, 다음과 같이 실행하면 됩니다. 

```bash
(venv) $ python3 tag_cralwer --tag coffee
(coffee) opening url: https://www.instagram.com/explore/tags/coffee/
(coffee) 72 posts to be added (merged_results: 0)
...
```

 크롤링 시작 직후부터 `result/` 디렉토리에 `coffee.json` 파일이 생성됩니다. 만약 크롤링을 도중에 중단 한 뒤, 나중에 다시 시작한다면 현재까지 저장된 포스트를 읽어 크롤링을 알아서 다시 이어하게 됩니다. 

 `coffee.json`  파일은 각 포스트의 고유한 id를 key로, 포스트의 내용과 관련된 메타데이터를 value로 가지며, 메타데이터는 다시 종류별로 각각 key와 value를 가집니다. 아래는 `coffee.json` 을 열어 본 것입니다. 

![](C:\Users\MinsangYu\Desktop\pycharm\crawler_instagram\_src\img\json.PNG)

| Key                | Value                                    |
| ------------------ | ---------------------------------------- |
| id                 | 포스트가 갖는 고유한 id                  |
| owner              | 포스트를 올린 사람의 고유한 id           |
| taken_at_timestamp | 포스트를 올린 시간의 타임스탬프          |
| shortcode          | 포스트 주소                              |
| text               | 내용                                     |
| caption            | 댓글                                     |
| is_video           | 올린 것이 비디오면 True, 아니면 False    |
| display_url        | 처음으로 보여지는 대표 이미지/비디오 url |



## Arguments

```bash
$ python tag_crawler.py -h
usage: tag_crawler.py [-h] --tag TAG [--limit LIMIT]

optional arguments:
  -h, --help     show this help message and exit
  --tag TAG      An Instagram tag to crawl
  --limit LIMIT  Post number limit (default=1000). 0 for no limit.
```

