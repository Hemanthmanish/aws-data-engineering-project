# AWS Data Engineering Project

This project demonstrates an end-to-end data engineering pipeline built using AWS services. The pipeline ingests raw data, processes it using AWS Glue, and enables analytics using Amazon Athena and QuickSight.

## Architecture

Data Source → Amazon S3 → AWS Glue ETL → Glue Data Catalog → Amazon Athena → Amazon QuickSight

## Technologies Used

- Amazon S3
- AWS Glue
- AWS Glue Data Catalog
- Amazon Athena
- Amazon QuickSight
- Python
- SQL

## Project Workflow

1. Raw dataset is uploaded to Amazon S3.
2. AWS Glue ETL jobs process and transform the data.
3. The transformed data is stored back in Amazon S3.
4. AWS Glue Data Catalog stores metadata for querying.
5. Amazon Athena is used to run SQL queries on the processed data.
6. Amazon QuickSight creates dashboards and visualizations for analytics.

## Key Features

- End-to-end AWS data pipeline
- Serverless data processing using AWS Glue
- Query large datasets using Athena
- Data visualization with QuickSight
- Scalable cloud architecture

## Sample Analytics Query

```sql
SELECT region,
SUM(sales) AS total_sales
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;
