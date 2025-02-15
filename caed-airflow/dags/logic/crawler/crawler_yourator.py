"""
Author: PC
    目的: 爬蟲 Yourator 人力資源網職缺訊息
    功能:
        - https://www.yourator.co/jobs
"""
import urllib.parse
import pandas as pd
import time, json, requests
from datetime import datetime
from bs4 import BeautifulSoup

def crawler(**kwargs):
    pre_data = {}
    session = requests.Session()

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.184 Safari/537.36 Edg/121.0.2277.128',
        'referer': 'https://www.yourator.co/jobs',
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    url = 'https://www.yourator.co/api/v4/jobs?negotiable=false&page=1&position[]=full_time&task_based=false'
    res = session.get(url, headers=headers)
    loader = json.loads(res.text)
    for i in loader['payload']['jobs']:
        print(i)
        key = i['id']
        # report_date = datetime.strptime(f'{i['appearDate'][:4]}-{i['appearDate'][4:6]}-{i['appearDate'][6:]}', '%Y-%m-%d')
        pre_data[key] = {
            'jobNo': key,
            'report_date': None,
            'source_type': 'yourator',
            'pay': i['salary'],
            'state': None,
            'company': i['company']['brand'],
            'title': i['name'],
            'company_type': None,
            'area': i['location'],
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