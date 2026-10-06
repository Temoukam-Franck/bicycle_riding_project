import datetime
from src.citybike.citybike_utils import get_trip_duration_mins


def test_get_trip_duration_mins():
    data = [
        (datetime.datetime(2026,10,5,10,0,0), datetime.datetime(2026,10,5,10,10,0)), # 10minutes
        (datetime.datetime(2026,10,5,10,0,0), datetime.datetime(2026,10,5,10,30,0))  # 30minutes
    ]  
    schema = "start_time timestamp, end_time timestamp"
    df = spark.createDataFrame(data, schema=schema)

    result_df = get_trip_duration_mins(spark,df,"start_time","end_time","duration_minutes")

    result = result_df.select("duration_minutes").collect()

    assert result[0]["duration_minutes"] == 10
    assert result[1]["duration_minutes"] == 30

