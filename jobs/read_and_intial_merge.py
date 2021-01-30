from read_in_and_merge_tools import read_file, get_dates_df, merge
from configparser import ConfigParser
from datetime import datetime


def read_merge_with_dates(config, now_date):
    """
    :param config:
    :param now_date:
    :return:
    """
    raw_df = read_file(config)
    date_df = get_dates_df(now_date)

    merged_df = merge(raw_df, date_df)

    merged_df.to_csv(config.get("merged","running_merged"))

    return merged_df

# TODO schedule this

if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    now = datetime.today().strftime("%m/%d/%Y")
    read_merge_with_dates(config, now)