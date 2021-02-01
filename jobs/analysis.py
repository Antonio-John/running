# plans
# per month/day/week
# target for 2020 km
# moving average
# summary stata
from configparser import ConfigParser
from datetime import datetime
import pandas as pd
from analysis_tools import barchart, rolling_average
import matplotlib.pyplot as plt
import os

def analysis(config, now):

    # reads in file
    df = pd.read_csv(config.get("processed","running_processed"))

    # sets up directory
    directory = config.get("analysis", "folder_analysis") + now
    if not os.path.exists(directory):
        os.makedirs(directory)

    # monthly distance barchart
    monthly_barchart_dist = barchart(df, "sum", "month_year")
    plt.savefig(directory+"\monthly_barchart_distance.png")

    # monthly activity
    monthly_barchart_act = barchart(df, "count", "month_year")
    plt.savefig(directory+"\monthly_barchart_activity.png")

    monthly_barchart_avg = barchart(df, "average", "month_year")
    plt.savefig(directory+"\monthly_barchart_average_activity.png")


    # day of the week
    dayofweek__barchart_dist = barchart(df, "sum", "dayofweek")
    plt.savefig(directory+"\dayofweek_barchart_distance.png")

    # monthly activity
    dayofweek__barchart_act = barchart(df, "count", "dayofweek")
    plt.savefig(directory+"\dayofweek__barchart_activity.png")

    dayofweek__barchart_avg = barchart(df, "average", "dayofweek")
    plt.savefig(directory+"\dayofweek__barchart_average_activity.png")


    rolling_average_df_30=rolling_average(df, 30)
    rolling_average_df_14 = rolling_average(df, 14)
    rolling_average_df_10 = rolling_average(df, 10)
    rolling_average_df_7 = rolling_average(df, 7)



if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    now = datetime.today().strftime("%Y%m%d")
    analysis(config, now)
