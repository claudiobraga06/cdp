from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName("CreateTable").enableHiveSupport().getOrCreate()   
spark.sql("DROP TABLE IF EXISTS u00389026727.tbl1")
spark.sql("DROP TABLE IF EXISTS u00389026727.tbl2")
spark.sql("DROP TABLE IF EXISTS u00389026727.tbl3")
