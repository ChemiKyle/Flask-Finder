#!/usr/bin/env python3

import seaborn as sns
import pandas as pd
import sqlite3
from datetime import datetime as dt


def fetch_data(yr = '*', mnth = '*'):
    conn = sqlite3.connect('log.db')
    cmd = ("SELECT * FROM log WHERE "
            "Year = ? AND Month = ?;")
    return pd.read_sql_query(cmd, conn, params = [yr, mnth])
    conn.close()

def hourly_x_daily(df):
    sns.jointplot("Hour", "Day", data = df, kind = 'hex')
