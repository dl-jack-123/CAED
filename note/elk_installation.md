# ElasticSearch + Logstash + Kibana (ELK Stack)
是一款強大的文本搜尋工具可以應用於:

- 網站搜索
- 日誌分析
- 地理空間分析處理等
- 其他

功能:
1. ElasticSearch: 搜尋引擎
2. Logstash: log 資料收集
3. Kibana: 資料視覺化
## 安裝方式

```base
cd elk; # 進入 elk 目錄
docker-compose up -d;
```

#### 進入 http://127.0.0.1:5601/ 
畫面如下:
![img.png](../sample/elastic_home.png)


#### Airflow 設定

1. 進入 Airflow 管理介面
2. 點選 Admin -> Connections
3. 點選 Create
4. 設定 Connection Id: elasticsearch_default
5. 設定 Connection Type: elasticsearch
6. 設定 Host: [ip]
7. 設定 Port: 9200
8. 點選 Save


##### 參考

https://gary840227.medium.com/elasticsearch-%E6%95%99%E5%AD%B8-fdbb9fdf3225