from pyspark.sql.functions import sum, avg, max
from pyspark.sql import SparkSession

def spark_agg():

    spark = SparkSession.builder .appName("CSV Example") .master("local[*]") .getOrCreate()

    df = spark.read.csv(r"C:\Users\amith\Downloads\sales1.csv",header=True,inferSchema=True)

    df = df.toDF(*[c.strip().replace(" ", "_") for c in df.columns])

    df.groupBy("COMPANY") .agg(sum("AMOUNT").alias("total_Amt"),avg("AMOUNT").alias("avg_Amt"), max("AMOUNT").alias("max_Amt") ) .show()

    spark.stop()
