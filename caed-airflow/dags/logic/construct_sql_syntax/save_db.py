"""
    說明: 關於 crawler 存 db 的 SQL 語法 和欄位格式統一在此定義
    邏輯: 儲存數據進入 TABLE 的 SQL 語法, 用 jinja2 模板
"""

def t_job_insert(**kwargs):
    table_name = kwargs['table_name']
    rows = kwargs['ti'].xcom_pull(task_ids=kwargs['task_ids'], key=kwargs['key'])

    if not rows:
        raise ValueError(f'No data found in XCom for key {table_name}')

    values = ",\n".join(
        f"('{row['jobNo']}', '{row['report_date']}', '{row['source_type']}', '{row['company']}', '{row['title']}', '{row['state']}', '{row['company_type']}')"
        for row in rows
    )
    sql_syntax = f"""
        INSERT INTO {table_name} (job_no, report_date, source_type, company, title, state, company_type)
        VALUES {values};
        """

    kwargs['ti'].xcom_push(key='construct_sql_syntax', value=sql_syntax)