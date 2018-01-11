#!/usr/bin/env python3

import sqlite3
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def fetch_data(yr = '*', mnth = '*'):
    conn = sqlite3.connect('log.db')
    cmd = ("SELECT * FROM log WHERE "
            "Year = ? AND Month = ?;")
    return pd.read_sql_query(cmd, conn, params = [yr, mnth])
    conn.close()

def hourly_x_daily(df):
    sns.jointplot("Day", "Hour", data = df, kind = "hex")
    sns.plt.show()

def hourly_x_weekday(df):
    sns.jointplot("Weekday", "Hour", data = df, kind = "hex")
    sns.plt.show()

def hourly(df):
    sns.distplot(df["Hour"])
    sns.plt.show()

def main():
    d = dt.today()
    df = fetch_data(d.year, d.month)
    hourly(df)

if __name__ == "__main__":
    main()
