from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from logic.crawler.crawler_104 import crawler, log
from logic.construct_sql_syntax.save_db import t_job_insert

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

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

with (DAG(
        'crawler_104',
        default_args=default_args,
        schedule='@daily',
        start_date=datetime(2025, 1, 1),
        catchup=False,
) as dag):
    task1 = PythonOperator(
        task_id='1.crawler',
        python_callable=crawler,
        provide_context=True,
    )
    task2 = PythonOperator(
        task_id='2.log',
        python_callable=log,
        op_kwargs={
            'task_ids': 'crawler',
            'key': 'crawler_data',
        },
        provide_context=True,
    )
    task3 = PythonOperator(
        task_id='3.construct_sql_syntax-insert',
        python_callable=t_job_insert,
        op_kwargs={
            'task_ids': '1.crawler',
            'key': 'crawler_data',
            'table_name': 't_job',
        },
        provide_context=True,
    )
    task4 = PostgresOperator(
        task_id='4.store-postgres',
        postgres_conn_id='ps', # You need to set up a connection for PostgreSQL
        sql="{{ ti.xcom_pull(task_ids='3.construct_sql_syntax-insert', key='construct_sql_syntax') }}",
    )

    task1 >> task2 >> task3 >> task4