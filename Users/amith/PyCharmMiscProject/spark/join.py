from pyspark.sql import SparkSession
import re

def spark_join():

    spark = SparkSession.builder \
        .appName("CSV Join Example") \
        .master("local[*]") \
        .getOrCreate()

    spark.conf.set("spark.sql.debug.maxToStringFields", 1000)

    sales_items = spark.read.csv(
        r"C:\Users\amith\Downloads\Sales_feb-2.txt",
        header=True,
        inferSchema=True
    )

    sales_summary = spark.read.csv(
        r"C:\Users\amith\Downloads\sales_jan-1.txt",
        header=True,
        inferSchema=True
    )

    sales_items = sales_items.toDF(*[c.strip().replace(" ", "_") for c in sales_items.columns])
    sales_summary = sales_summary.toDF(*[c.strip().replace(" ", "_") for c in sales_summary.columns])

    print(sales_items.columns)
    print(sales_summary.columns)

    joined_df = sales_items.join(
        sales_summary,
        "Patient_Mobile",
        "inner"
    )

    joined_df.show(100,truncate=False)

    not_regular = sales_items.join(
        sales_summary,
        sales_items["Patient_Mobile"] == sales_summary["Patient_Mobile"],"left_anti")
    not_regular.show(100,truncate=False)

    spark.stop()
