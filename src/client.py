import mysql.connector
import pandas as pd

import database.db_access as db
import database.db_query as dbq

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
dfs = []

dfs.append(pd.read_sql(dbq.scenario_nbr(), conn))
dfs.append(pd.read_sql(dbq.total_car_nbr(), conn))
dfs.append(pd.read_sql(dbq.total_street_nbr(), conn))
dfs.append(pd.read_sql(dbq.total_intersection_nbr(), conn))
dfs.append(pd.read_sql(dbq.total_mean_speed(), conn))
dfs.append(pd.read_sql(dbq.total_max_distance(), conn))
dfs.append(pd.read_sql(dbq.total_mean_duration(), conn))
dfs.append(pd.read_sql(dbq.scenario_with_most_cars(), conn))

conn.close()

for df in dfs:
    df = spark.createDataFrame(df)
    df.show()