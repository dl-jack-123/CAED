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
    # sql_syntax = f"""
    #     INSERT INTO {table_name} (job_no, report_date, source_type, company, title, state, company_type)
    #     VALUES {values};
    #     """

    sql_syntax = f"""
        INSERT INTO {table_name} (job_no, report_date, source_type, company, title, state, company_type)
        VALUES {values}
        ON CONFLICT (job_no) DO UPDATE
        SET 
            report_date = EXCLUDED.report_date,
            source_type = EXCLUDED.source_type,
            company = EXCLUDED.company,
            title = EXCLUDED.title,
            state = EXCLUDED.state,
            company_type = EXCLUDED.company_type;
    """

    # sql_syntax = f"""
    #     MERGE INTO {table_name} AS target
    #     USING (VALUES {values}) AS source (job_no, report_date, source_type, company, title, state, company_type)
    #     ON target.job_no = source.job_no
    #     WHEN MATCHED THEN
    #         UPDATE SET
    #             report_date = source.report_date,
    #             source_type = source.source_type,
    #             company = source.company,
    #             title = source.title,
    #             state = source.state,
    #             company_type = source.company_type
    #     WHEN NOT MATCHED THEN
    #         INSERT (job_no, report_date, source_type, company, title, state, company_type)
    #         VALUES (source.job_no, source.report_date, source.source_type, source.company, source.title, source.state, source.company_type);
    # """

    kwargs['ti'].xcom_push(key='construct_sql_syntax', value=sql_syntax)