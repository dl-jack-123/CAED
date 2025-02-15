from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.elasticsearch.hooks.elasticsearch import ElasticsearchPythonHook, ElasticsearchSQLHook

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

CONN_ID = "elasticsearch_default"

"""
https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html
None: 不進行調度，僅用於「外部觸發」DAG
@once: 僅運行一次
@hourly: 每小時運行一次
@daily: 每天一次
@weekly: 每週週日早上午夜運行一次
@monthly: 每月第一天午夜運行一次
@yearly: 每年 1 月 1 日午夜運行一次
"""

def use_elasticsearch_hook():
    """
    Use ElasticSearchPythonHook to print results from a local Elasticsearch
    """
    es_hosts = ["http://192.168.31.177:9200"]
    es_hook = ElasticsearchPythonHook(hosts=es_hosts)
    query = {"query": {"match_all": {}}}
    result = es_hook.search(query=query)
    print(result)
    return True


def show_tables():
    """
    show_tables queries elasticsearch to list available tables
    """
    # [START howto_elasticsearch_query]
    es = ElasticsearchSQLHook(elasticsearch_conn_id=CONN_ID)

    es_connection = es.get_conn()
    response = es_connection.execute_sql("SHOW TABLES")

    for row in response["rows"]:
        print(f"row: {row}")


    return True

with DAG(
        'test_elk',
        default_args=default_args,
        schedule='@daily',
        start_date=datetime(2025, 1, 1),
        catchup=False,
) as dag:

    test1 = PythonOperator(
        task_id='show_tables',
        python_callable=show_tables,
        provide_context=True,
    )
    test2 = PythonOperator(
        task_id='use_elasticsearch_hook',
        python_callable=use_elasticsearch_hook,
        provide_context=True,
    )


    test1 >> test2