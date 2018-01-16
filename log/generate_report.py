#!/usr/bin/env python3

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
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
            ylim = (24, 0), xlim = (1, 31))
    plt.show()


def hourly_x_weekday(df):
    sns.jointplot("Weekday", "Hour", data = df, stat_func = None,
            ylim = (24, 0), xlim = (0, 6), color = "orange")
    plt.show()


def hourly(df):
    sns.distplot(df["Hour"]).set(xlim=(0,24))
    plt.show()


def top_terms(df):
    search_terms = df["Phrase"].value_counts().head()
    sns.barplot(search_terms)
    plt.show()


def main():
    d = dt.today()
    df = fetch_data(d.year, d.month)
    hourly_x_weekday(df)


if __name__ == "__main__":
    sns.set()
    main()

