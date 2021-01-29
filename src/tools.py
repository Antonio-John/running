from configparser import ConfigParser
import pandas as pd

def read(config):
    """
    :param config file that is used in the project
    :return: the latest running data with pandas
    """
    file_path = config.get("io", "running")
    df = pd.read_excel(file_path,
                       usecols=9)

    return df




if __name__ == "__main__":
    config = ConfigParser()
    config.read('C:\Running\config\config.properties')
    read(config)
