"""
This is the Script and main entry point to add in the extra derived variables
that will be used in analysis.
Functions
*derived_variables
"""
from configparser import ConfigParser
import pandas as pd
import sys
import os
src_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from derived_variables_tools import (add_cumulatives_cols, add_month_variable, add_month_year,
                                         add_dayofweek, add_no_week, add_km)


def derived_variables(conf):
    """
    :param conf where all the file paths/settings are

    """
    # read file in
    file_path=conf.get("merged", "running_merged")
    merged_df = pd.read_csv(file_path)

    # add in extra variables
    cumulative_cols = add_cumulatives_cols(merged_df)
    time_df = add_month_variable(cumulative_cols)
    month_year_df = add_month_year(time_df)
    dayofweek_df = add_dayofweek(month_year_df)
    no_week_df = add_no_week(dayofweek_df)
    with_km_df = add_km(no_week_df)

    # save file out
    output_path=config.get("processed", "running_processed")
    with_km_df.to_csv(output_path)


if __name__ == "__main__":
    config = ConfigParser()
    con_path=os.path.realpath(os.path.join(os.path.dirname(__file__), 
                                           '..', 
                                           'config',
                                           'config.properties'))
    config.read(con_path)
    derived_variables(config)
