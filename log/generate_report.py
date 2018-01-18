#!/usr/bin/env python3

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from datetime import datetime as dt


def fetch_data(yr = '*', mnth = '*'):
    conn = sqlite3.connect('log.db')
    cmd = ("SELECT * FROM log WHERE "
            "Year = ? AND Month = ?;")
    return pd.read_sql_query(cmd, conn, params = [yr, mnth])
    conn.close()


def hourly_x_daily(df):
    sns.jointplot("Day", "Hour", data = df, stat_func = None,
            ylim = (24, 0), xlim = (1, 31),
            kind = "hex")
    plt.show()


def hourly_x_weekday(df):
    sns.jointplot("Weekday", "Hour", data = df, stat_func = None,
            ylim = (24, 0), xlim = (0, 6), color = "orange")
    plt.show()


def hourly(df):
    sns.distplot(df["Hour"]).set(xlim=(0,24))
    plt.show()


def top_terms(df):
    srch = pd.DataFrame(df["Phrase"].value_counts().head(10))
    srch.columns = ["Count"]
    ax = sns.barplot(srch.index, srch.Count)
    ax.set(xlabel = "Search Terms",
            ylabel = "Times Searched")
    ax.yaxis.set_major_locator(MaxNLocator(integer = True))
    plt.show()


def main():
    sns.set()
    d = dt.today()
    df = fetch_data(d.year, d.month)
    top_terms(df)


if __name__ == "__main__":
    main()

