<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) <br>

<br>

## *Airflow 依賴位置*

```bash
- docker/config   用途：存放 Airflow 的配置文件（例如 airflow.cfg），這是 Airflow 的核心配置文件，定義了整個系統的行為和設置。
                    內容：
                        資料庫連接信息
                        任務執行者（Executor）設置（如 LocalExecutor 或 CeleryExecutor）
                        日誌設置、排程頻率等參數
- docker/dags     用途：存放所有的工作流定義檔案（DAGs，Directed Acyclic Graphs）。
- docker/logs     用途：存放任務執行時的日誌檔案，便於問題排查與監控。
- docker/plugins  用途：存放自定義的 Airflow 擴展，如：
                          Operator, Hook, Macro, Executor
```

| 目錄 | 代表意義 | 主要功能 |
| :--: | :-- | :-- |
| config | 配置文件| 定義 Airflow 行為與設置 |
| dags | 工作流定義| 存放 DAG 腳本 |
| log | 日誌文件| 存放 DAG 執行過程中的詳細日誌 |
| plugins |自定義功能與擴展| 用於添加自定義 Operator,Hook, Macro, Executor等 |

<br>

## *Pycharm 設置*

1. 啟動本專案的 `docker/docker-compose.yaml` 服務 -> `docker compose up`
2. 在 Pycharm 中設置遠端執行環境
    - `File` -> `Settings` -> `Project: CAED` -> `Python Interpreter`
    - 點選右上角的齒輪 -> `Add` -> `On Docker Compose`
    - 在 Configuration file 中選擇 `docker/docker-compose.yaml`
    - `Service` 選擇 `airflow-python`，`Python Interpreter`
    - 按下 `Next` -> `OK`
    - ![參考圖片](https://airflow.apache.org/docs/apache-airflow/stable/_images/add_container_python_interpreter.png)
    - 回到預 Debug 的腳本, 點選右鍵開啟執行前設定黨
    - interpreter 選擇 airflow-python, 加入 exec 在 docker-compose/command
    - ![參考圖片](https://airflow.apache.org/docs/apache-airflow/stable/_images/docker-compose-pycharm.png)
    - 接下來對於 DAG 的開發就可以直接在 Pycharm 中進行了

<br>

## *Reference*
-  ### [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)