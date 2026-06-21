from pyspark.sql import SparkSession
import time

spark = SparkSession \
    .builder \
    .appName('standalone_pyspark') \
    .getOrCreate()

schema = 'ID INTEGER, COUNTRY STRING, HIT LONG'
df = spark.createDataFrame(data=[(1,'Korea',120),(2,'USA',80),(3,'Japan',40)], schema=schema)
df.count()

# sleep 10 minute
time.sleep(60*10)