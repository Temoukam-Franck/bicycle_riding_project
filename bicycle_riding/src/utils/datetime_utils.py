from pyspark.sql.functions import *

def timestamp_to_date_col(spark, df, timestamp_col, output_col):
    df = df.withColumn(output_col, to_date(col(timestamp_col)))
    return df