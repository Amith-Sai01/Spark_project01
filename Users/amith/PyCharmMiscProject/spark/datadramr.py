from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("create").getOrCreate()
data =[("apple", 50), ("banana", 20), ("orange", 30), ("grape", 15)]
df = spark.createDataFrame(data, ["fruit", "quantity"])
df.show()
df.createOrReplaceTempView("fruit")
result = spark.sql("SELECT * FROM fruit WHERE Quantity > 25")
result.show()
spark.stop()
