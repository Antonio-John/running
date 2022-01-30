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
import sys
sys.path.append("../src")

from analysis_tools import barchart, rolling_average, histo, line_plot, goal_for_year


def analysis(conf, today):
    """
    :param config:
    :param now:
    Saves all the analysis and visualisations needed
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
    
    # time per month
    barchart(df, "sum", "month_year", category="time")
    plt.savefig(directory+r"/monthly_barchart_time.png")


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
    


    # rolling average
    time_period=[30,14,10,7]
    for time in time_period:
        rolling_average(df, time)
        plt.savefig(directory + r"/rolling_average_"+str(time)+".png")


    # histogram
    histo(df, "distance")
    plt.savefig(directory + r"/Histogram_Distance.png")


    line_plot(df, "cumulative_distance_km")
    plt.savefig(directory + r"/km_overtime.png")

    goal_for_year(df, 2021)
    plt.savefig(directory+r"/goals_2021.png")



if __name__ == "__main__":
    config = ConfigParser()
    config.read('../config/config.properties')
    now = datetime.today().strftime("%Y%m%d")
    analysis(config, now)
