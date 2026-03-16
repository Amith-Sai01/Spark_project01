from pyspark import SparkContext
from pyspark.context import SparkContext

sc = SparkContext("local[*]", "Spark")
numbers = sc.parallelize([10, 20, 30, 40, 50])
divide = numbers.map(lambda x: x/10)
print(divide.collect())
