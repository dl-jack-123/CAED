from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from logic.crawler.crawler_104 import crawler, log
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
# DAG settings
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


with DAG(
        'crawler_104',
        default_args=default_args,
        schedule='@daily',
        start_date=datetime(2025, 1, 1),
        catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id='crawler',
        python_callable=crawler,
    )
    task2 = PythonOperator(
        task_id='log',
        python_callable=log,
    )

    # 存去 TABLE 的 SQL 語法, 用 jinja2 模板
    insert_sql = """
INSERT INTO t_job (job_no, report_date, source_type, company, title, state, company_type)
VALUES 
    {% for row in ti.xcom_pull(task_ids='crawler', key='104_data')  %}
    ('{{ row.jobNo }}', '{{ row.report_date }}', '{{ row.source_type }}', '{{ row.company }}', '{{ row.title }}', '{{ row.state }}', '{{ row.company_type }}'){% if not loop.last %}, {% endif %}
    {% endfor %}
"""


    store_in_postgres = PostgresOperator(
        task_id='store_in_postgres',
        postgres_conn_id='ps',  # You need to set up a connection for PostgreSQL
        sql=insert_sql,
        dag=dag,
    )


    task1 >> task2 >> store_in_postgres