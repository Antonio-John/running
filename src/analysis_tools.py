"""
This is the analysis tools module. This creates all the charts associated with analysis
Functions
*barchart
*rolling_average
*histo
*line_plot
*goal_for_year
"""
import matplotlib.pyplot as plt
import pandas as pd


def barchart(df: pd.core.frame.DataFrame, by_stat: str, time_period: str, category: str):
    """
    :param df: Pandas dataframe which creates the barchart
    :param by_stat: By which stat e.g by sum/count/average
    :param time_period: Over which time period should the barhcart be (i.e X axis)
    :param category: Units of Y axis
    :return:
    Creates a barchart for data based on the arguments passed.
    """
    if time_period == "week":
        df["week"] = df["week"].astype(int)
    else:
        df[time_period] = df[time_period].astype(str)

    plt.figure()

    if by_stat == "sum":
        df_group = df.groupby([time_period]).sum()
    elif by_stat == "count":
        df_group = df.groupby([time_period]).count()
    elif by_stat == "average":
        df_group = df.groupby([time_period]).mean()

    if time_period == "week":
        df_group = df_group.sort_index()
        # TODO: tech debt
        sorted=df_group.sort_values("distance_km")
        sorted.to_csv("per_week.csv")

    plt.bar(df_group.index, df_group[category], align='center', alpha=0.5)
    plt.xticks(rotation='vertical')
    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=6)
    plt.xlabel(time_period)
    plt.ylabel("Totals")
    plt.title(by_stat + ' Per ' + time_period)
    plt.tight_layout()

def rolling_average(df:pd.core.frame.DataFrame, time_period):
    """
    :param df: Pandas dataframe used to create rolling average chart
    :param time_period: Time period used for the rolling average
    Creates a barchart of rolling average for data based on the arguments passed.
    """
    plt.figure()
    df['distance'] = df['distance'].fillna(0)
    df['rolling_average_'+str(time_period)+'_day'] = df.iloc[:, 4].rolling(window=time_period).sum()
    plt.plot(df["date"], df['rolling_average_'+str(time_period)+'_day'])
    plt.title("Rolling " + str(time_period) + " Average")
    plt.tight_layout()

def histo(df:pd.core.frame.DataFrame, by_stat:str):
    """
    :param df: Pandas dataframe used to create the histograms
    :param by_stat: by which stat e.g average, count
    Creates a histogram for data based on the arguments passed.
    """
    plt.figure()
    plt.hist(df[by_stat], bins=10, align="mid")

def line_plot(df:pd.core.frame.DataFrame, by_stat:str):
    """
    :param df: Pandas dataframe used to create the line plot
    :param by_stat: by which stat e.g average, count
    Creates a linechart for data based on the arguments passed.
    """
    plt.figure()
    plt.plot(df.index, df[by_stat])
    plt.tight_layout()

def goal_for_year(df:pd.core.frame.DataFrame, year)->pd.core.frame.DataFrame:
    """
    :param df: processed dataframe
    :param year: year i want to do the goal for
    Want to run 2021 km in 2021, this is the progress  track
    """

    days = range(0, 365)
    year_df=df[df["year"]==year]
    km_so_far=year_df["distance_km"].sum()
    row_count=len(year_df)
    current_avg_per_day=[km_so_far/row_count]

    time_series_per_day_current = [avg * day for day in days for avg in current_avg_per_day]

    goal_avg_per_day=[year/365]
    time_series_per_day_goal=[avg * day for day in days for avg in goal_avg_per_day]

    plt.figure()
    plt.plot(range(0,365), time_series_per_day_goal)
    plt.plot(range(0, 365), time_series_per_day_current)

