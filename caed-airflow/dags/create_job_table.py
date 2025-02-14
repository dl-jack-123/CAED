from __future__ import annotations

import datetime
import os

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

# [START postgres_sql_execute_query_operator_howto_guide]


# create_pet_table, populate_pet_table, get_all_pets, and get_birth_date are examples of tasks created by
# instantiating the Postgres Operator

DAG_ID = "create_postgres_job_table"


with DAG(
    dag_id=DAG_ID,
    start_date=datetime.datetime(2020, 2, 2),
    schedule="@once",
    catchup=False,
) as dag:
    # [START postgres_sql_execute_query_operator_howto_guide_create_pet_table]
    drop_table = SQLExecuteQueryOperator(
        task_id="drop_table",
        conn_id="ps",
        sql="drop table if exists t_job;",
    )

    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="ps",
        sql="sql/Job.sql",
    )

    drop_table >> create_table