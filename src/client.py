import mysql.connector
import pandas as pd

import database.db_access as db

from pyspark.sql import SparkSession

app_name = "car_simulator"
master = "local"

spark = SparkSession.builder.appName(app_name).master(master).getOrCreate()

conn = mysql.connector.connect(user = db.DB_USER, 
                                password = db.DB_PASSWORD,
                                host = db.DB_HOST,
                                database = db.DB_DATABASE,
                                port = 3306
                                )

cursor = conn.cursor()
query = "SELECT * FROM car_state"
df = pd.read_sql(query, conn)
conn.close()

df = spark.createDataFrame(df)

df.show()