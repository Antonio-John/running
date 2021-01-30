import matplotlib.pyplot as plt
import pandas as pd



def month_barchart(df):

    df["month_year"] = df["month_year"].astype(str)
    df_group_month = df.groupby(["month_year"]).sum()

    monthly_bar_time = plt.bar(df_group_month.index, df_group_month["distance"], align='center', alpha=0.5)
    plt.xticks(rotation='vertical')
    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=6)

    return monthly_bar_time









