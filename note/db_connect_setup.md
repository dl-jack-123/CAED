<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> 
<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/dl-jack-123/04f0f768feebd9f972d884fd1aae2114/raw/CAED_clone.json&logo=github](https://github.com/Junwu0615/How-To-Use-Clone-Shields'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 

<br>

## *⭐ Database Connection Setup (PostgreSQL) ⭐*

#### I.　設定連接 port，兩個 `5432`，代表 docker 容器外和容器內的 port
![png](../sample/db_connect_setup_0.png)

#### II.　重新 Build Postgres 的服務
```bash
docker-compose up -d --no-deps --build postgres
```
- Connection Id (要在airflow中使用的id): `ps` (postgresql)
- HOST (連接的主機): `Your ipv4 address`
- Connection Type (連接的資料庫類型): `Postgres`
- Database (連接的db名稱): `JB` (初始化建立的db)
- Login 和 Password 都是 `airflow`
- ![png](../sample/db_connect_setup_1.png)
- 填完後, 可從 Pycharm Data Source 設定連接
- ![png](../sample/db_connect_setup_4.png)
- 上述設定完後到 DAG 執行 postgres_operator_dag
- ![png](../sample/db_connect_setup_5.png)
- Done !

