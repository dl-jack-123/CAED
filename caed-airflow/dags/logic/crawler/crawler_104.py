"""
Author: PC
    目的: 爬蟲 104 人力資源網職缺訊息
    功能:
        - 最新職缺: 社群行銷 / 軟體工程 / 金融保險 / 業務銷售 / 專案管理
            - https://www.104.com.tw/jobs/main/newestjob/?jobsource=index_hot_c&utm_medium=cweb_keyword&utm_source=104&tab=job_1

"""
import time, json, requests

def crawler():
    url = 'https://www.104.com.tw/jobs/main/newestjob/?jobsource=index_hot_c&utm_medium=cweb_keyword&utm_source=104&tab=job_1'
    print(url)



if __name__ == "__main__":
    crawler()
