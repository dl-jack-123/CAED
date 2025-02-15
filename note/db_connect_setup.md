<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> 
<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/dl-jack-123/7b40f4b7a8ef0f41258dd5343a77e1a9/raw/CAED_clone.json&logo=github](https://github.com/Junwu0615/How-To-Use-Clone-Shields'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 

<br>

## *⭐ Database Connection Setup (PostgreSQL) ⭐*

### *I.　設定連接 port，兩個 `5432`，代表 docker 容器外和容器內的 port*
![png](../sample/db_connect_setup_0.png)

<br>

### *II.　重新 Build Postgres 的服務*
```bash
docker-compose up -d --no-deps --build postgres
```

<br>

### *III.　Airflow UI 介面設定*
- Connection Id ( SQL 在 Airflow 中使用的 ID ): `ps` ( postgreSQL )
- HOST ( 連接主機IP ): `Your ipv4 address`
- Connection Type ( 連接資料庫類型 ): `Postgres`
- Database ( 連接的db名稱 ): `JB` ( 初始化建立的db )
- Login 和 Password 皆是 `airflow`
- ![png](../sample/db_connect_setup_1.png)
- 填完後, 可從 Pycharm Data Source 設定連接
- ![png](../sample/db_connect_setup_4.png)
- 上述設定完後到 DAG 執行 create_postgres_job_table
- ![png](../sample/db_connect_setup_5.png)
- Done !

### *IV.　數據成功餵入 DB 後，Refresh 即可看到數據*
- <img alt="png" width='500' height='480' src="https://github.com/dl-jack-123/CAED/blob/main/sample/db_connect_setup_6.png"/>
- <img alt="png" width='450' height='500' src="https://github.com/dl-jack-123/CAED/blob/main/sample/db_connect_setup_7.png"/>
[//]: # (- ![png]&#40;../sample/db_connect_setup_6.png&#41;)
[//]: # (- ![png]&#40;../sample/db_connect_setup_7.png&#41;)

