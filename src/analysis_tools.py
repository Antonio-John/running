import matplotlib.pyplot as plt
import pandas as pd



def month_barchart(df, type):

    plt.figure()
    df["month_year"] = df["month_year"].astype(str)
    if type=="sum":
        df_group_month = df.groupby(["month_year"]).sum()
    elif type=="count":
        df_group_month = df.groupby(["month_year"]).count()

    #print(df_group_month["distance"])
    monthly_bar_time = plt.bar(df_group_month.index, df_group_month["distance"], align='center', alpha=0.5)
    plt.xticks(rotation='vertical')
    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=6)
    plt.xlabel("Month")
    plt.ylabel("Totals")
    plt.title(type+' Per Month')
    plt.tight_layout()


    return monthly_bar_time









