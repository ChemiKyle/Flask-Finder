#!/usr/bin/env python3

__author__	= "Kyle Chesney"

from flask import *
import sqlite3
import pandas as pd

app = Flask(__name__)
conn = sqlite3.connect('db/inv.db', check_same_thread = False)
c = conn.cursor()


def chem_search(phrase):
    results = []
    cmd = ("SELECT Name, "
    "Quantity, "
    "Unit, "
    "Location, "
    "Sublocation "
    "FROM chem "
    "WHERE Name LIKE ?")
    # Sanitize sql queries
    for result in c.execute(cmd, ['%' + phrase + '%']):
        results.append(result)
    return pd.DataFrame(results,
            columns=["Name", "Quantity", "Unit", "Location", "Shelf"])

@app.route("/")
def main():
    return render_template('view.html')

@app.route("/", methods=['POST'])
def do_search():
    option = str(request.form['sub_db'])
    phrase = str(request.form['phrase'])
    df = chem_search(phrase)
    ### Styling effects
    # df.set_index(['Name'], inplace=True)
    # df.index.name = None
    ###
    return render_template('view.html', tables = [df.to_html()])

if __name__ == "__main__":
    app.run(debug=True)
