from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName("CreateTable").enableHiveSupport().getOrCreate()  
spark.sql("use u00389026727") 
spark.sql("create table tbl2 using iceberg as select * from tbl1 where origin = 'EWR' limit 5")
