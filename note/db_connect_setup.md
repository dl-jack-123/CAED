
# 修改 Postgres 設定

* 設定連接 port，兩個 5432，代表 docker 容器外和容器內的 port
![img.png](../sample/db_connect_setup_0.png)
## 重新 Build Postgres 的服務
```text
docker-compose up -d --no-deps --build postgres
```

- Connection Id(要在airflow中使用的id): ps(postgresql)
- HOST(連接的主機): [ipv4 address]
- Connection Type(連接的資料庫類型): Postgres
- Database(連接的db名稱): JB(初始化建立的db)
- Login 和 Password 都是 airflow
![img.png](../sample/db_connect_setup_1.png)
- 填完後, 可從 Pycharm Data Source 設定連接
- ![img.png](../sample/db_connect_setup_4.png)
- 上述設定完後到 DAG 執行 postgres_operator_dag
- ![img.png](../sample/db_connect_setup_5.png)
- 完成

