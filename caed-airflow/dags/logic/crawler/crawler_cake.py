"""
Author: PC
    目的: 爬蟲 cake 人力資源網職缺訊息
    功能:
        - Cake 找工作: https://www.cake.me/companies?location_list%5B0%5D=%E5%8F%B0%E7%81%A3
"""
import urllib.parse
import time, json, requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

def crawler(**kwargs):
    pre_data = {}
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'Referer': 'https://www.cake.me/',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    x_algolia_api_key = 'YTVlZTJmYjk2ZjIxZTVlYjc3ZTMyOWVlNDgwM2M0YTVkYTI2Y2Y1YzA3YjE0NTAwZmY5MmU2NGQ3YTlhNWFlZHZhbGlkVW50aWw9MTc0MDE1MzExNiZyZXN0cmljdEluZGljZXM9Sm9iJTJDSm9iX29yZGVyX2J5X2NvbnRlbnRfdXBkYXRlZF9hdCUyQ0pvYl9wbGF5Z3JvdW5kJTJDUGFnZSUyQ1BhZ2Vfb3JkZXJfYnlfY29udGVudF91cGRhdGVkX2F0JmZpbHRlcnM9YWFzbV9zdGF0ZSUzQSslMjJjcmVhdGVkJTIyK0FORCtub2luZGV4JTNBK2ZhbHNlJmhpdHNQZXJQYWdlPTEwJmF0dHJpYnV0ZXNUb1NuaXBwZXQ9JTVCJTIyZGVzY3JpcHRpb25fcGxhaW5fdGV4dCUzQTgwJTIyJTVEJmhpZ2hsaWdodFByZVRhZz0lM0NtYXJrJTNFJmhpZ2hsaWdodFBvc3RUYWc9JTNDJTJGbWFyayUzRQ'
    x_algolia_application = '966RG9M3EK'
    url = (
        f'https://{x_algolia_application.lower()}-1.algolianet.com/1/indexes/*/queries?'
        f'x-algolia-api-key={x_algolia_api_key}&'
        f'x-algolia-application-id={x_algolia_application}'
    )
    payload = {
        "requests": [
            {
                "indexName": "Page",
                "params": "analyticsTags=[\"next\",\"company_search\"]&clickAnalytics=true&facetFilters=[[\"location_list:台灣\"]]&facets=[\"location_list\",\"number_of_employees\",\"sector\",\"tech_labels\"]&highlightPostTag=__/ais-highlight__&highlightPreTag=__ais-highlight__&maxValuesPerFacet=200&page=0&query="
            }
        ]
    }
    res = session.post(url, json=payload, headers=headers)
    loader = json.loads(res.text)

    for _ in loader['results']:
        # print(_.keys())
        # print(_['hits'])
        for i in _['hits']:
            for job in i['created_jobs_limited']:
                title = job['title']
                key = f"{i['name']}_{title}"
                pre_data[key] = {
                    'jobNo': key,
                    'report_date': None,
                    'source_type': 'cake',
                    'title': title,
                    'company': i['name'],
                    'state': None,
                    'company_type': i['sector_i18n'],
                    'scale': i['number_of_employees'],
                    'jobs_count': i['created_jobs_count'],
                }

    # TODO 需要轉成像[{}, {}] 的寫法
    datum = []
    for k, v in pre_data.items():
        datum.append({
            'jobNo': v['jobNo'],
            'report_date': v['report_date'],
            'source_type': v['source_type'],
            'company': v['company'],
            'title': v['title'],
            'state': v['state'],
            'company_type': v['company_type'],
        })

    # return pre_data
    kwargs['ti'].xcom_push(key=kwargs['key'], value=datum)

# def log(pre_data):
def log(**kwargs):
    pre_data = kwargs['ti'].xcom_pull(task_ids=kwargs['task_ids'], key=kwargs['key'])

    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(pre_data).T
    print(df)
    # print(pre_data)

# if __name__ == "__main__":
#     pre_data = crawler()
#     log(pre_data)