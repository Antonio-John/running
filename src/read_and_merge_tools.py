import pandas as pd


def read_file(config):
    """
    :param config file that is used in the project
    :return: the latest running data with pandas
    reads in running files and return dataframe
    """
    file_path = config.get("raw", "running")
    df = pd.read_excel(file_path,
                       usecols=list(range(8)))

    return df

def get_dates_df(end_date):
    """
    :param end date is the
    :return: df_dates a dataframe with all dates
    from when running started
    """
    df_dates = pd.DataFrame(pd.date_range(start='10/12/2019',
                                       end=end_date),
                                       columns = ["date"])

    return df_dates


def merge(raw_df, df_date):

    merge = df_date.merge(raw_df, how="left", on="date")

    return merge