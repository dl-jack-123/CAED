-- create  table

CREATE TABLE IF NOT EXISTS t_job (
  "job_no" varchar PRIMARY KEY,
  "report_date" varchar ,
  "source_type" varchar,
  "company" varchar ,
  "title" varchar ,
  "state" varchar,
  "company_type" varchar
                               );