from pyspark.sql import SparkSession
import os

def spark_call(app_name):

    os.environ["HADOOP_HOME"] = "C:\\hadoop"
    os.environ["spark.hadoop.io.native.lib.available"] = "false"

    spark = SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.driver.extraJavaOptions","-Dio.native.lib.available=false") \
        .config("spark.executor.extraJavaOptions","-Dio.native.lib.available=false") \
        .config("spark.hadoop.tmp.dir", "C:\\tmp\\hadoop")\
        .getOrCreate()

    return spark