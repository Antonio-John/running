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

    # monthly barchart
    monthly_barchart = month_barchart(df)
    plt.savefig(directory+"\monthly_barchart.png")


if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    now = datetime.today().strftime("%Y%m%d")
    analysis(config, now)
