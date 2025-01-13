<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) <br>


# ⭐ CAED ⭐

## *Current progress*
| 項目 | 內容 | 負責人 | 完成時間 |
| :--: | -- | :--: |:--:|
| 爬蟲主題方向 | 人力銀行職缺相關內容 | - | 待討論 |
| 爬蟲實作 | - | PC | - |
| 架設 Airflow | - | PC / DL | - |
| 資料表定義 | - | PC / DL | - |
| 資料庫底層撰寫 | - | DL | - |
| Docker | - | DL | - |
| Public Clouds | - | DL | - |

## *Summary*
- ### *A.　Crawler + Airflow*
  - #### Crawler: 撰寫爬蟲邏輯 ( 資料抓取 / 資料驗證 )
  - #### Airflow: 使用其管理工作流 ( 定時排程 / 通知 /...等 )
- ### *B.　MongoDB*
  - #### 定義資料庫規範
  - #### 測試基本的資料寫入、查詢與驗證
- ### *C.　ELK Stack*
  - #### 部署 ELK 監控 Airflow 的任務執行情況和爬蟲日誌
  - #### 配置 Logstash，將 Airflow 和爬蟲日誌導入 Elasticsearch
  - #### 使用 Kibana 可視化日誌，方便追蹤問題與錯誤
- ### *D.　Docker*
  - #### Airflow、MongoDB、ELK 等服務容器化，統一管理
  - #### 設定 Docker Compose 方便本地和伺服器環境可一鍵部署
  - #### 透過 Grafana、Prometheus 管理 Docker 服務
- ### *E.　Deployed on 3 Major Public Clouds*
  - #### Amazon Web Services
  - #### Google Cloud Platform
  - #### Microsoft Azure