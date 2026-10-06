from pyspark.sql.functions import *

def get_trip_duration_mins(spark,df,start_col,end_col,output_col):
    df = df.withColumn(output_col,
                      (unix_timestamp(to_timestamp(end_col)) - unix_timestamp(to_timestamp(start_col))) / 60)
    return df