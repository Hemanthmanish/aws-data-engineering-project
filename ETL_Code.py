from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

sales_df = spark.read.csv("s3://data-bucket/sales.csv", header=True, inferSchema=True)

clean_df = sales_df.dropna()

aggregated_df = clean_df.groupBy("region").sum("revenue")

aggregated_df.write.mode("overwrite").parquet("s3://processed-data/sales_summary")
