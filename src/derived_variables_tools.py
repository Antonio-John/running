import pandas as pd
import numpy as np
import re

def add_cumulatives_cols(df):
    """
    :param df: takes the merged df
    :return: adds in extra cumulative columns
    """

    df["cumulative_distance"] = np.nancumsum(df["distance"])
    df["cumulative_time"] = np.nancumsum(df["time"])
    df["cumulative_hours"] = np.nancumsum(df["time" ] /60)
    df["%_of_10000"] = df["%_of_10000"].ffill()

    return df

def add_month_variable(df):
    """
    gets month variable added in

    """
    df["month"] = pd.DatetimeIndex(df['date']).month

    # this is adds a 0 in before number e.g Feb goes from month to 02
    i = 0
    for month in df["month"]:
        if month < 10:
            month_str = str(month)
            replace = re.sub(month_str, "0"+month_str, month_str)
            df["month"].iloc[i] = replace
        i = i + 1

    return df

def add_month_year(df):

    df["year"] = pd.DatetimeIndex(df['date']).year

    df["month_year"] = df["year"].astype(str)  + df["month"].astype(str)

    return df

def add_dayofweek(df):

    df["dayofweek"] = pd.DatetimeIndex(df['date']).dayofweek

    return df

def add_no_week(df):

    df["week"] = 0 * len(df)
    week = 1
    i = 2
    for i in range(2, len(df)):
        if df["dayofweek"][i] == 0:
            week = week + 1
        df["week"][i] = week
        i = i + 1

    return df

def add_km(df):

    df["distance_km"] = df["distance"]/1000
    df["cumulative_distance_km"] = df["cumulative_distance"] / 1000

    return df

