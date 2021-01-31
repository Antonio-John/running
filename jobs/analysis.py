# plans
# per month/day/week
# target for 2020 km
# moving average
# summary stata
from configparser import ConfigParser
from datetime import datetime
import pandas as pd
from analysis_tools import month_barchart
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
    monthly_barchart_dist = month_barchart(df, "sum")
    plt.savefig(directory+"\monthly_barchart_distance.png")

    # monthly activity
    monthly_barchart_act = month_barchart(df, "count")
    plt.savefig(directory+"\monthly_barchart_activity.png")

if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    now = datetime.today().strftime("%Y%m%d")
    analysis(config, now)
