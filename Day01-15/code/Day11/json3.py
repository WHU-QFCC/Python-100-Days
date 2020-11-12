"""
json应用

Version: 0.1
Author: strongpu
Date: 2020-11-11
"""

import requests
import json


def main():
    url = 'http://api.tianapi.com/txapi/tiangou/index?key=MYKEY'
    resp = requests.get(url)
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['content'])


if __name__ == '__main__':
    main()