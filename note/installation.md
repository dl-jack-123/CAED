<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) <br>

<br>

## *Airflow 安裝*

### *建立資料夾*
```text
./dags - you can put your DAG files here.

./logs - contains logs from task execution and scheduler.

./config - you can add custom log parser or add airflow_local_settings.py to configure cluster policy.

./plugins - you can put your custom plugins here.
```

### *設定變數*
- 設定 AIRFLOW_UID 
    ```bash
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```
- 或手動建立 .env 填入
    ```text
    AIRFLOW_UID=50000
    ```

### *初始化資料庫與建立帳號*
```text
docker compose up airflow-init
```

### *執行*
```text
docker compose up
```

![img.png](../sample/img.png)