"""
Author: PC
    目的: 爬蟲 104 人力資源網職缺訊息
    功能:
        - 最新職缺: 社群行銷 / 軟體工程 / 金融保險 / 業務銷售 / 專案管理
            - https://www.104.com.tw/jobs/main/newestjob/?jobsource=index_hot_c&utm_medium=cweb_keyword&utm_source=104&tab=job_1
"""
import urllib.parse
import pandas as pd
import time, json, requests
from datetime import datetime
from bs4 import BeautifulSoup

# import sys
# sys.path.append('/opt/airflow/')
# sys.path.append('/opt/airflow/dags/')
# sys.path.append('/opt/airflow/dags/logic/')
# sys.path.append('/opt/airflow/dags/logic/crawler/')

# import pdb
# pdb.set_trace()

# import pydevd_pycharm
# pydevd_pycharm.settrace('host.docker.internal', port=5678, stdoutToServer=True, stderrToServer=True)

def crawler(**kwargs):
    pre_data = {}
    session = requests.Session()
    todo = {
        '社群行銷': 1,
        '軟體工程': 2,
        '金融保險': 3,
        '業務銷售': 4,
        '專案管理': 5
    }
    for key, idx in todo.items():
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'referer': f'https://www.104.com.tw/jobs/main/newestjob/?jobsource=index_hot_c&utm_medium=cweb_keyword&utm_source=104&tab=job_{idx}',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'x-kl-ajax-request': 'Ajax_Request',
            'cookie': '_gcl_au=1.1.1162782756.1737816715; c_job_algo_exp_poc=A; c_job_algo_exp_date_poc=E; _ga=GA1.1.1292653715.1737816715; _ga=GA1.4.1292653715.1737816715; dcard-adkt-device=9c82e490-366d-49ca-8496-8c7513c49ca9; _clck=576anq%7C2%7Cfsv%7C0%7C1851; _fbp=fb.2.1737816716006.688102270379204693; _hjSessionUser_3218023=eyJpZCI6IjhiZGM2NTIyLThmN2UtNWUyYi04ODFmLTI1MGViYTc1ZjUyNSIsImNyZWF0ZWQiOjE3Mzc4MTY3MTYwOTAsImV4aXN0aW5nIjpmYWxzZX0=; luauid=1110688308; dtCookie=v_4_srv_1_sn_649EE1F6F5429EBA91E376E5C00F2BAF_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0; _hjSession_601941=eyJpZCI6ImEzOGQ4YmVmLWQ0OTEtNGNkNi1iYzljLTdjYTkxOGQ1MTY2NCIsImMiOjE3Mzc4MTY3MjIwNzIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; lup=1110688308.4507568175053.4730906474341.1.4640712161167; lunp=4730906474341; _hjSessionUser_601941=eyJpZCI6IjNiYzUwYjI5LWM5NmYtNTkzZi05NjNiLWY2MmRkOTMwOTg4NSIsImNyZWF0ZWQiOjE3Mzc4MTY3MjIwNzEsImV4aXN0aW5nIjp0cnVlfQ==; _clsk=sonbzr%7C1737818571632%7C7%7C1%7Cb.clarity.ms%2Fcollect; _ga_FJWMQR9J2K=GS1.1.1737816715.1.1.1737818571.60.0.0; _ga_W9X1GB1SVR=GS1.1.1737816714.1.1.1737818571.60.0.0; _ga_WYQPBGBV8Z=GS1.4.1737816715.1.1.1737818961.60.0.0',
        }
        order = 30
        url = (f"https://www.104.com.tw/jobs/search/list?hotJob=0&"
               f"jobcat=2007001004%2C2013001006%2C2007001006&"
               f"keyword={urllib.parse.quote(key)}&"
               f"order={order}")

        res = session.get(url, headers=headers)
        loader = json.loads(res.text)
        for i in loader['data']['list']:
            # print(i)
            key = i['jobNo']
            report_date = datetime.strptime(f"{i['appearDate'][:4]}-{i['appearDate'][4:6]}-{i['appearDate'][6:]}", '%Y-%m-%d')
            pre_data[key] = {
                'jobNo': key,
                'report_date': str(report_date)[:10],
                'source_type': '104',
                'pay': i['salaryDesc'],
                'state': i['applyDesc'],
                'company': i['custNameRaw'],
                'title': i['jobName'],
                'company_type': i['coIndustryDesc'],
                'area': i['jobAddrNoDesc'],
                'condition_1': i['optionEdu'],
                'condition_2': '工作經歷' + i['periodDesc'],
                'link': 'https://' + i['link']['job'],
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