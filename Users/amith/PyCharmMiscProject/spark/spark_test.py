from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark Test").master("local[*]").getOrCreate()

data = [("Alice",25),("Bob",30),("C",20),("Dog",15),("Me",40)]
nameDf = spark.createDataFrame(data, ["Name","Age"])
nameDf.show()
nameDf.filter(nameDf.Age > 26).select(nameDf.Name).show()
nameDf.createTempView("nameTable")
spark.sql("select * from nameTable where Name = 'Me'").show()

spark.stop()