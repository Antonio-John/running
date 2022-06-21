"""
This is the read and merge tools module. This contains all functionality
which is used for reading in the raw data and merging it in.
Functions
*read_file
*rolling_averag
*get_dates_df
*merge
"""
import pandas as pd


def read_file(config:dict) -> pd.core.frame.DataFrame:
    """
    :param Config file used in the project
    :return: the latest running data with pandas
    reads in running files from paths from config and return dataframe
    """
    file_path = config.get("raw", "running")
    cols_to_keep=["date","activity", "distance","time","cumulative_distance",
                  "cumulative_time","cumulative_hours","%_of_10000"]

    df = pd.read_excel(file_path,
                       usecols=cols_to_keep)

    return df

def get_dates_df(end_date:str)->pd.core.frame.DataFrame:
    """
    :param end date is the
    :return: df_dates a dataframe with all dates
    from when running started
    """
    df_dates = pd.DataFrame(pd.date_range(start='10/12/2019',
                                       end=end_date),
                                       columns = ["date"])

    return df_dates

def merge(raw_df:pd.core.frame.DataFrame, df_date:str) -> pd.core.frame.DataFrame:
    """
    :param raw_df: Raw pandas dataframe to be merged
    :param df_date: Dates df which is to be merged into
    :return:
    """
    raw_df.date.astype('datetime64[ns]')
    df_date.date.astype('datetime64[ns]')
    merged = df_date.merge(raw_df, how="left", on="date")

    return merged
