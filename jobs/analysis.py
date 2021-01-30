# plans
# per month/day/week
# target for 2020 km
# moving average
# summary stata
from configparser import ConfigParser
from datetime import datetime
import pandas as pd

def analysis(config, now):

    df = pd.read_csv(config.get("processed","running_processed"))

    print(df)

if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    now = datetime.today().strftime("%m/%d/%Y")
    analysis(config, now)