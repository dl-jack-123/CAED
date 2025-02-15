<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> 
<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/dl-jack-123/7b40f4b7a8ef0f41258dd5343a77e1a9/raw/CAED_clone.json&logo=github](https://github.com/Junwu0615/How-To-Use-Clone-Shields'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 

<br>

## *⭐ Airflow Installation ⭐*

### *I.　建立資料夾*
```commandline
cd caed-airflow
```
```commandline
md dags; md logs; md plugins; md config; md database; md .pycharm_helpers
```

<br>

### *II.　設定變數*
- 設定 AIRFLOW_UID 
    ```bash
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```
- 或手動建立 .env 填入
    ```bash
    AIRFLOW_UID=50000
    ```

<br>

### *III.　初始化服務*
```bash
docker compose up airflow-init -d
```

<br>

### *IV.　啟動 Python Debug 服務*
```bash
docker compose up airflow-python -d
```

<br>

### *V.　執行*
```bash
docker compose up -d
```
![jpg](../sample/installation_00.jpg)