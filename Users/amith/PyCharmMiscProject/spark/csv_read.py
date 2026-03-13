from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("CSV Example") \
    .master("local[*]") \
    .getOrCreate()
def spark_new():
    df = spark.read.csv(r"C:\Users\amith\Downloads\sales1.csv", header=True, inferSchema=True)
    df.show()
    df.printSchema()

    df = df.toDF(*[c.strip() for c in df.columns])

    df = df.toDF(*[c.strip().replace(" ", "_") for c in df.columns])



    df.filter(col("AMOUNT") > 1000) .select("ITEM_NAME", "AMOUNT") .withColumn("GST", col("AMOUNT") * 0.18) .show()
    df.groupBy("COMPANY").count().show()
    spark.stop()