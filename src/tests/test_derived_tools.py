import pandas as pd

from src.derived_variables_tools import (add_cumulatives_cols,
                                         add_month_variable,
                                         add_month_year,
                                         add_dayofweek,
                                         add_no_week,
                                         add_km)

def test_add_cumuluative_cols():

    input_df=pd.DataFrame({"distance":[1,2,3],
                           "time":[10,30,40],
                           "%_of_10000":[0.1, None, 0.3]})

    expected_df=pd.DataFrame({"distance":[1,2,3],
                              "time":[10,30,40],
                              "%_of_10000":[0.1, 0.1, 0.3],
                              "cumulative_distance":[1,3,6],
                              "cumulative_time":[10,40,80],
                              "cumulative_hours":[10/60, 40/60, 80/60]})

    result=add_cumulatives_cols(input_df)

    pd.testing.assert_frame_equal(expected_df, result)

def test_add_month_variable():

    input_df=pd.DataFrame({"date":[pd.to_datetime("05/10/2021"),
                                   pd.to_datetime("05/11/2021")]})

    expected_df=pd.DataFrame({"date":[pd.to_datetime("05/10/2021"),
                                    pd.to_datetime("05/11/2021")],
                              "month":["05","05"]})

    result=add_month_variable(input_df)

    pd.testing.assert_frame_equal(expected_df, result)

def test_add_month_year():

    input_df = pd.DataFrame({"date": [pd.to_datetime("05/10/2021"),
                                      pd.to_datetime("05/11/2021")],
                             "month": ["05", "05"]})

    expected_df = pd.DataFrame({"date": [pd.to_datetime("05/10/2021"),
                                      pd.to_datetime("05/11/2021")],
                                "month": ["05", "05"],
                                "year":["2021","2021"],
                                "month_year":["202105","202105"]})

    result=add_month_year(input_df)

    pd.testing.assert_frame_equal(expected_df, result)

def test_add_dayofweek():

    input_df = pd.DataFrame({"date": [pd.to_datetime("05/10/2021"),
                                      pd.to_datetime("05/11/2021")]})

    expected_df = pd.DataFrame({"date": [pd.to_datetime("05/10/2021"),
                                         pd.to_datetime("05/11/2021")],
                                "dayofweek":[0,1]})

    result=add_dayofweek(input_df)

    pd.testing.assert_frame_equal(expected_df,result, check_dtype=False)

def test_add_no_week():

    input_df = pd.DataFrame({"dayofweek": [5,6,0,1,2,3,4,5,6,0,1,2,]})

    expected_df = pd.DataFrame({"dayofweek": [5,6,0,1,2,3,4,5,6,0,1,2,],
                             "week": [1,1,2,2,2,2,2,2,2,3,3,3]})

    result=add_no_week(input_df)

    pd.testing.assert_frame_equal(result, expected_df)

def test_add_km():

    input_df = pd.DataFrame({"distance": [10003,10006,16701],
                             "cumulative_distance":[10003,20009,36710]})

    expected_df = pd.DataFrame({"distance": [10003,10006,16701],
                               "cumulative_distance":[10003,20009,36710],
                                "distance_km":[10.003,10.006,16.701],
                               "cumulative_distance_km":[10.003,20.009,36.71]})

    result=add_km(input_df)

    pd.testing.assert_frame_equal(result, expected_df)
