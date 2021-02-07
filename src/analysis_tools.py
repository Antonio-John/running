import matplotlib.pyplot as plt
import pandas as pd



def barchart(df, type, time_period, category):
    """
    df is the dataframe and type is count or sum per month
    """

    if time_period=="week":
        df["week"] = df["week"].astype(int)
    else:
        df[time_period] = df[time_period].astype(str)


    plt.figure()

    if type=="sum":
        df_group = df.groupby([time_period]).sum()
    elif type=="count":
        df_group = df.groupby([time_period]).count()
    elif type=="average":
        df_group = df.groupby([time_period]).mean()

    if time_period == "week":
        df_group=df_group.sort_index()

    bar_time = plt.bar(df_group.index, df_group[category], align='center', alpha=0.5)
    plt.xticks(rotation='vertical')
    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=6)
    plt.xlabel(time_period)
    plt.ylabel("Totals")
    plt.title(type+' Per '+time_period)
    plt.tight_layout()

    return df_group

def rolling_average(df, t):
    """
    
    """
    plt.figure()
    df['distance'] = df['distance'].fillna(0)
    df['rolling_average_'+str(t)+'_day'] = df.iloc[:, 4].rolling(window=t).sum()
    rolling_avg_30 = plt.plot(df["date"], df['rolling_average_'+str(t)+'_day'])

def histo(df, type):
    """
    plot histogram
    """
    plt.figure()
    plt.hist(df[type], bins=20, align="mid")



def line_plot(df, type):

    plt.figure()
    plt.plot(df.index, df[type])
    plt.tight_layout()


