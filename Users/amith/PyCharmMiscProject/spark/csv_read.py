from pyspark.sql.functions import col
from utils.read_utils import get_read_csv
from utils.spark_session import spark_call
from utils.write_utils import write_results

# Create Spark session
spark = spark_call("csv_example")

def spark_new():

    # Read file
    df = get_read_csv(spark, r"C:\Users\amith\Downloads\sales_jan-1.txt")

    df.show()
    df.printSchema()

    # Clean column names (remove spaces)
    df = df.toDF(*[c.strip().replace(" ", "_") for c in df.columns])

    # Check columns after cleaning
    print(df.columns)

    # Filter rows and calculate GST
    result = df.filter(col("Sell_Amount") > 1000) \
               .select("Items", "Sell_Amount") \
               .withColumn("GST", col("Sell_Amount") * 0.18)

    print("result show")
    result.show()

    # Group by patient name
    grouped = df.groupBy("Patient_Name").count()

    print("grouped show")
    grouped.show()

    # Write results
    write_results(
        result,
        grouped,
        r"C:\Users\amith\PyCharmMiscProject\data\output_filtered",
        r"C:\Users\amith\PyCharmMiscProject\data\output_grouped"
    )
    spark.stop()