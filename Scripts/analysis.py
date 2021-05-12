"""
This is the Script and main entry point for al the analysis that takes place
Functions
*analysis
"""
from configparser import ConfigParser
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt

from src.analysis_tools import barchart, rolling_average, histo, line_plot


def analysis(conf, today):
    """
    :param config:
    :param now:
    Saves all the analysis and barcharts needed
    """

    # reads in file
    df = pd.read_csv(conf.get("processed","running_processed"))

    # sets up directory
    directory = conf.get("analysis", "folder_analysis") + today
    if not os.path.exists(directory):
        os.makedirs(directory)

    # monthly distance barchart
    barchart(df, "sum", "month_year", category="distance_km")
    plt.savefig(directory+r"/monthly_barchart_distance.png")
    # monthly activity
    barchart(df, "count", "month_year", category="distance_km")
    plt.savefig(directory+r"/monthly_barchart_activity.png")
    barchart(df, "average", "month_year", category="distance_km")
    plt.savefig(directory+r"/monthly_barchart_average_activity.png")


    # day of the week
    barchart(df, "sum", "dayofweek", category="distance_km")
    plt.savefig(directory+r"/dayofweek_barchart_distance.png")
    barchart(df, "count", "dayofweek", category="distance_km")
    plt.savefig(directory+r"/dayofweek_barchart_activity.png")
    barchart(df, "average", "dayofweek", category="distance_km")
    plt.savefig(directory+r"/dayofweek_barchart_average_activity.png")

    # per week
    barchart(df, "sum", "week", category="distance_km")
    plt.savefig(directory+r"/weekly_barchart_distance.png")

    rolling_average(df, 30)
    rolling_average(df, 14)
    rolling_average(df, 10)
    rolling_average(df, 7)

    histo(df, "distance")

    line_plot(df, "cumulative_distance_km")
    plt.savefig(directory + "r/km_overtime.png")


if __name__ == "__main__":
    config = ConfigParser()
    config.read(r'C:/Running/config/config.properties')
    now = datetime.today().strftime("%Y%m%d")
    analysis(config, now)
