#!/usr/bin/env python3

import seaborn
import sqlite3
from datetime import datetime as dt

conn = sqlite3.connect('db/log.db')
c = conn.cursor()
