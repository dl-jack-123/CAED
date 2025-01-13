# <p class="rainbow-animation">⭐ CAED ⭐<p>

## <c1>*Summary*<c1>
- ### <c3>*A.　Crawler + Airflow*<c3>
  - #### Crawler: 撰寫爬蟲邏輯 ( 資料抓取 / 資料驗證 )
  - #### Airflow: 使用其管理工作流 ( 定時排程 / 通知 /...等 )
- ### <c3>*B.　MongoDB*<c3>
  - #### 定義資料庫規範
  - #### 測試基本的資料寫入、查詢與驗證
- ### <c3>*C.　ELK Stack*<c3>
  - #### 部署 ELK 監控 Airflow 的任務執行情況和爬蟲日誌
  - #### 配置 Logstash，將 Airflow 和爬蟲日誌導入 Elasticsearch
  - #### 使用 Kibana 可視化日誌，方便追蹤問題與錯誤
- ### <c3>*D.　Docker*<c3>
  - #### Airflow、MongoDB、ELK 等服務容器化，統一管理
  - #### 設定 Docker Compose 方便本地和伺服器環境可一鍵部署
  - #### 透過 Grafana、Prometheus 管理 Docker 服務
- ### <p class="rainbow1">*E.　Deployed on 3 Major Public Clouds*<p>
  - #### Amazon Web Services
  - #### Google Cloud Platform
  - #### Microsoft Azure


<style>
c1 { color: rgb(255, 85, 160) }
c3 { color: Orange }
c3 { color: rgb(20, 180, 230) }
c4 { color: rgb(255, 155, 255) }
.rainbow1 {
  font-size: 18px;
  font-weight: bold;
  background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.rainbow-animation {
  font-size: 32px;
  font-weight: bold;
  background: linear-gradient(90deg, red, orange, yellow, green, indigo, violet);
  background-size: 400%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: rainbow 5s linear infinite;
}
@keyframes rainbow {
  100% { background-position: 100%; }
  100% { background-position: -200%; }
}
</style>