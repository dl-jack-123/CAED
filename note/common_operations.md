<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> 
<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/dl-jack-123/7b40f4b7a8ef0f41258dd5343a77e1a9/raw/CAED_clone.json&logo=github](https://github.com/Junwu0615/How-To-Use-Clone-Shields'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 

<br>

## *⭐ Airflow Common Operations ⭐*

<br>

#### *重啟服務 ( 更新檔案後的重整 )*
```bash
docker-compose restart airflow-webserver
```

<br>

#### *完全重啟服務*
```bash
docker-compose down
```
```bash
docker-compose up -d
```

<br>

#### *移除服務步驟*
```bash
docker stop <airflow-python container id>
```
```bash
docker-compose down -v
```
```bash
docker system prune --all --volumes
```