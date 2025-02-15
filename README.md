<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> 
<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/dl-jack-123/7b40f4b7a8ef0f41258dd5343a77e1a9/raw/CAED_clone.json&logo=github](https://github.com/Junwu0615/How-To-Use-Clone-Shields'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 

<br>

# ⭐ CAED ⭐
## *A.　Current progress*
| 項目 | 內容 | 負責人 | 完成時間 |
| :--: | :--: | :--: |:--:|
| 爬蟲主題方向 | 人力銀行職缺相關內容 | - | 2025-01-14 |
| 架設 Airflow 服務 | 以 `Docker compose` 啟動 | PC / DL | 2025-01-16 |
| [104](https://www.104.com.tw/) 爬蟲實作 | 簡易版 | PC | 2025-01-26 |
| [Cake](https://www.cake.me/) 爬蟲實作 | 簡易版 | PC | 2025-01-26 |
| README: 筆記圖書館 | `D. Note Library` | PC | 2025-01-26 |
| 資料庫定義 | `sql/CreateDB.sql` | DL | 2025-02-10 |
| 資料表定義 | `sql/Job.sql` | DL | 2025-02-10 |
| 資料存取設置 | `note/db_connect_setup.md` | DL | 2025-02-10 |
| 資料表建立 | `dags/create_job_table.py` | DL | 2025-02-10 |
| 順利以 PostgreSQL 儲存資料 | `construct_sql_syntax/save_db.py` | PC / DL | 2025-02-15 |
| ELK Stack | `note/elk_installation.md` | DL | 2025-02-15 |
| [Yourator](https://www.yourator.co/) 爬蟲實作 | 簡易版 | PC | 2025-02-15 |
| UI 介面瀏覽 SQL 數據 | `note/ui_operations.md` | PC | - |
| 專案初版完成 | 至少 `3` 個人力網站 | - | 2025-02-15 |
| Public Clouds | *如何上傳 | PC / DL | - |

<br>

## *B.　Summary*
- ### *a.　Crawler + Airflow + ELK Stack + Docker*
  - #### *Crawler :* 撰寫爬蟲邏輯，並基於 ETL 流程實作
  - #### *Airflow :* 使用其框架管理工作流
  - #### *ELK Stack*
    - #### 部署 ELK 監控 Airflow 的任務執行情況和爬蟲日誌
    - #### 配置 Logstash，將 Airflow 和爬蟲日誌導入 Elasticsearch
    - #### 使用 Kibana 可視化日誌，方便追蹤問題與錯誤
  - #### *Docker :* 將數個服務容器化，統一管理
- ### *b.　PostgreSQL*
  - #### 定義資料庫規範
  - #### 測試 CRUD 標準操作
- ### *c.　Deployed on 3 Major Public Clouds*
  - #### Amazon Web Services
  - #### Google Cloud Platform
  - #### Microsoft Azure

<br>

## *C.　Showcase Results*
```commandline
# airflow:airflow
http://localhost:8080/
```
![00.jpg](sample/home_00.jpg)
![01.jpg](sample/home_01.jpg)
![02.jpg](sample/home_02.jpg)

<br>

## *D.　Note Library*
-  ### [*⭐ Airflow Installation ⭐*](./note/installation.md)
-  ### [*⭐ Airflow Common Operations ⭐*](./note/common_operations.md)
-  ### [*⭐ Airflow Local Development ⭐*](./note/local_dev.md)
-  ### [*⭐ Airflow UI Operations ⭐*](./note/ui_operations.md)
-  ### [*⭐ Database Connection Setup (PostgreSQL) ⭐*](./note/db_connect_setup.md)
-  ### [*⭐ ELK Stack ⭐*](./note/elk_installation.md)