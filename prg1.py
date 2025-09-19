from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName("CreateTable").enableHiveSupport().getOrCreate()  
spark.sql("use u00389026727") 
spark.sql("create table tbl1 using iceberg as select * from fl_parq where origin = 'EWR' limit 10")
print("tudo funcionou corretamente")

