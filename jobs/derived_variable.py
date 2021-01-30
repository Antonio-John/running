from derived_variables_tools import add_cumulatives_cols, add_month_variable, add_month_year, add_dayofweek, add_no_week
from configparser import ConfigParser
import pandas as pd


def derived_variables(config):
    """
    :param config:
    :param now_date:
    :return:
    """
    # read file in
    file_path=config.get("merged", "running_merged")
    merged_df = pd.read_csv(file_path)

    # add in extra variables
    cumulative_cols = add_cumulatives_cols(merged_df)
    time_df = add_month_variable(cumulative_cols)
    month_year_df = add_month_year(time_df)
    dayofweek_df = add_dayofweek(month_year_df)
    no_week_df = add_no_week(dayofweek_df)

    # save file out
    output_path=config.get("processed", "running_processed")
    no_week_df.to_csv(output_path)


if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    derived_variables(config)