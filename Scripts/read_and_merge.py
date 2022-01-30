"""
This is the Script and main entry point to read the raw data in and then
merge with the dates dataframe.
Functions
*read_merge_with_dates
"""
from configparser import ConfigParser
from datetime import datetime
import pandas as pd
import sys
sys.path.append("../src")

from read_and_merge_tools import read_file, get_dates_df, merge


def read_merge_with_dates(conf:dict, now_date:str)->pd.core.frame.DataFrame:
    """
    :param config: Config file used with files paths
    :param now_date: Todays date
    This will read in the raw file, created the dated dataframe and then
    merge and save this
    """
    raw_df = read_file(conf)
    date_df = get_dates_df(now_date)
    merged_df = merge(raw_df, date_df)

    merged_df.to_csv(config.get("merged","running_merged"))

    return merged_df


if __name__ == "__main__":
    config = ConfigParser()
    config.read('../config/config.properties')
    now = datetime.today().strftime("%m/%d/%Y")
    read_merge_with_dates(config, now)
