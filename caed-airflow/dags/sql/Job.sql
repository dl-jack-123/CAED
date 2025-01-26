-- create  table

CREATE TABLE IF NOT EXISTS t_job (
  "id" integer PRIMARY KEY,
  "report_date" Date UNIQUE,
  "source_type" varchar UNIQUE,
  "company" varchar UNIQUE,
  "title" varchar UNIQUE,
  "state" int,
  "company_type" varchar
                               );