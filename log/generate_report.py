#!/usr/bin/env python3

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from datetime import datetime as dt


def fetch_data(yr = dt.today().year, mnth = dt.today().month):
    conn = sqlite3.connect('log.db')
    cmd = ("SELECT * FROM log WHERE "
            "Year = ? AND Month = ?;")
    return pd.read_sql_query(cmd, conn, params = [yr, mnth])
    conn.close()


def hourly_x_daily(df):
    sns.jointplot("Day", "Hour", data = df, stat_func = None,
            ylim = (24, 0), xlim = (1, 31),
            kind = "hex")


def hourly_x_weekday(df):
    cmap = plt.cm.viridis
    h_x_w = sns.jointplot("Weekday", "Hour", data = df, stat_func = None,
            ylim = (24, 0), xlim = (0, 6), alpha = 0.3, cmap = cmap,
            kind = "hex",
            marginal_kws = dict(bins = 7, rug = True),
            joint_kws = dict(gridsize = 6))
    plt.figure()


def hourly(df):
    sns.distplot(df["Hour"]).set(xlim=(0,24))


def top_terms(df):
    srch = pd.DataFrame(df["Phrase"].value_counts().head(10))
    srch.columns = ["Count"]
    trms = sns.barplot(srch.index, srch.Count)
    trms.set(xlabel = "Search Terms",
            ylabel = "Times Searched")
    trms.yaxis.set_major_locator(MaxNLocator(integer = True))
    trms.set_xticklabels(trms.get_xticklabels(),
            rotation = 30)
    plt.figure()


def main():
    sns.set()
    d = dt.today()
    df = fetch_data()
    hourly_x_weekday(df)
    top_terms(df)
    plt.show()


if __name__ == "__main__":
    main()

