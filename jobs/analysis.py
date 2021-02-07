# plans
# per month/day/week
# target for 2020 km
# moving average
# summary stata
from configparser import ConfigParser
from datetime import datetime
import pandas as pd
from analysis_tools import barchart, rolling_average, histo, line_plot
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
    monthly_barchart_dist = barchart(df, "sum", "month_year", category="distance_km")
    plt.savefig(directory+"\monthly_barchart_distance.png")
    # monthly activity
    monthly_barchart_act = barchart(df, "count", "month_year", category="distance_km")
    plt.savefig(directory+"\monthly_barchart_activity.png")
    monthly_barchart_avg = barchart(df, "average", "month_year", category="distance_km")
    plt.savefig(directory+"\monthly_barchart_average_activity.png")


    # day of the week
    dayofweek__barchart_dist = barchart(df, "sum", "dayofweek", category="distance_km")
    plt.savefig(directory+"\dayofweek_barchart_distance.png")
    dayofweek__barchart_act = barchart(df, "count", "dayofweek", category="distance_km")
    plt.savefig(directory+"\dayofweek_barchart_activity.png")
    dayofweek__barchart_avg = barchart(df, "average", "dayofweek", category="distance_km")
    plt.savefig(directory+"\dayofweek_barchart_average_activity.png")

    # per week
    week_over_time_barchart_dist = barchart(df, "sum", "week", category="distance_km")
    plt.savefig(directory+"\weekly_barchart_distance.png")
    print(week_over_time_barchart_dist)


    rolling_average_df_30=rolling_average(df, 30)
    rolling_average_df_14 = rolling_average(df, 14)
    rolling_average_df_10 = rolling_average(df, 10)
    rolling_average_df_7 = rolling_average(df, 7)

    histogram_dist = histo(df, "distance")

    lineplot = line_plot(df, "cumulative_distance_km")
    plt.savefig(directory + "\km_overtime.png")


if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    now = datetime.today().strftime("%Y%m%d")
    analysis(config, now)

