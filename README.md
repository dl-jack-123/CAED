<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) <br>


# ⭐ CAED ⭐

## *Current progress*
| 項目 | 內容 | 負責人 | 完成時間 |
| :--: | -- | :--: |:--:|
| 爬蟲主題方向 | 人力銀行職缺相關內容 | - | 2025-01-14 |
| 架設 Airflow | - | PC / DL | - |
| 爬蟲實作 | - | PC / DL | - |
| 資料表定義 | - | PC / DL | - |
| 資料庫底層撰寫 | - | DL | - |
| Docker | - | PC / DL | - |
| Add LLM | - | PC / DL | - |
| Public Clouds | - | PC / DL | - |

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


## airflow 安裝

### 建立資料夾
```text
./dags - you can put your DAG files here.

./logs - contains logs from task execution and scheduler.

./config - you can add custom log parser or add airflow_local_settings.py to configure cluster policy.

./plugins - you can put your custom plugins here.
```
設定 AIRFLOW_UID 
```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
或手動建立 .env 填入
```text
AIRFLOW_UID=50000
```

初始化資料庫與建立帳號
```text
docker compose up airflow-init
```

執行

```text
docker compose up
```

預期!!!

![img.png](img.png)

## airflow 依賴位置
```text
- resource/config   用途：存放 Airflow 的配置文件（例如 airflow.cfg），這是 Airflow 的核心配置文件，定義了整個系統的行為和設置。
                    內容：
                        資料庫連接信息
                        任務執行者（Executor）設置（如 LocalExecutor 或 CeleryExecutor）
                        日誌設置、排程頻率等參數
- resource/dags     用途：存放所有的工作流定義檔案（DAGs，Directed Acyclic Graphs）。
- resource/logs     用途：存放任務執行時的日誌檔案，便於問題排查與監控。
- resource/plugins  用途：存放自定義的 Airflow 擴展，如：
                          Operator, Hook, Macro, Executor
```
|目錄	|代表意義| 	主要功能                                    |
|--|--|------------------------------------------|
|config|	配置文件| 	定義 Airflow 行為與設置                        |
|dags|	工作流定義| 	存放 DAG 腳本                               |
|log|	日誌文件| 	存放 DAG 執行過程中的詳細日誌                       |
|plugins	|自定義功能與擴展| 	用於添加自定義 Operator,Hook, Macro, Executor等 |

## Pycharm 設置
![參考](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

1. 啟動本專案的 `resource/docker-compose.yaml` 服務 -> `docker compose up`
2. 在 Pycharm 中設置遠端執行環境
    - `File` -> `Settings` -> `Project: CAED` -> `Python Interpreter`
    - 點選右上角的齒輪 -> `Add` -> `On Docker Compose`
    - 在 Configuration file 中選擇 `resource/docker-compose.yaml`
    - `Service` 選擇 `airflow-python`，`Python Interpreter`
    - 按下 `Next` -> `OK`
    - ![參考圖片](https://airflow.apache.org/docs/apache-airflow/stable/_images/add_container_python_interpreter.png)
    - 回到預 Debug 的腳本, 點選右鍵開啟執行前設定黨
    - interpreter 選擇 airflow-python, 加入 exec 在 docker-compose/command
    - ![參考圖片](https://airflow.apache.org/docs/apache-airflow/stable/_images/docker-compose-pycharm.png)
    - 接下來對於 DAG 的開發就可以直接在 Pycharm 中進行了
    

接下來完成
1. 資料存取設定
2. 一個資料收集實作
3. 表格建立