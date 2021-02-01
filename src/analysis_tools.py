import matplotlib.pyplot as plt
import pandas as pd



def barchart(df, type, time_period):
    """
    df is the dataframe and type is count or sum per month
    """
    plt.figure()
    df[time_period] = df[time_period].astype(str)
    if type=="sum":
        df_group = df.groupby([time_period]).sum()
    elif type=="count":
        df_group = df.groupby([time_period]).count()
    elif type=="average":
        df_group = df.groupby([time_period]).mean()


    bar_time = plt.bar(df_group.index, df_group["distance"], align='center', alpha=0.5)
    plt.xticks(rotation='vertical')
    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=6)
    plt.xlabel(time_period)
    plt.ylabel("Totals")
    plt.title(type+' Per '+time_period)
    plt.tight_layout()

    return bar_time

def rolling_average(df, t):
    """
    
    """
    plt.figure()
    df['distance'] = df['distance'].fillna(0)
    df['rolling_average_'+str(t)+'_day'] = df.iloc[:, 4].rolling(window=t).sum()
    rolling_avg_30 = plt.plot(df["date"], df['rolling_average_'+str(t)+'_day'])
    plt.show()





