#!/usr/bin/env python3

__author__	= "Kyle Chesney"

from flask import *
import sqlite3
import pandas as pd
from datetime import datetime as dt
from log import generate_report as gr
from io import BytesIO
import base64

app = Flask(__name__)


def search(phrase, option):
    conn = sqlite3.connect('db/inv.db', check_same_thread = False)
    c = conn.cursor()
    results = []
    if option == "chemicals": 
        cmd = ("SELECT Name, "
        "Quantity, "
        "Unit, "
        "Location, "
        "Sublocation, "
        "Layer "
        "FROM chem "
        "WHERE Name LIKE ?")
        columns=["Name", "Quantity", "Unit", "Location", "Sublocation", "Shelf"]
    elif option == "stock":
        cmd = ("SELECT Name, "
        "Quantity, "
        "Form, "
        "Location, "
        "Sublocation, "
        "Layer "
        "FROM stock "
        "WHERE Name LIKE ?")
        columns = ["Name", "Quantity", "Form", "Location", "Sublocation",
        "Shelf"]
    elif option == "equipment":
        cmd = ("SELECT Name, "
        "Quantity, "
        "Location, "
        "Sublocation, "
        "Layer "
        "FROM equip "
        "WHERE Name LIKE ?")
        columns = ["Name", "Quantity", "Location", "Sublocation",
                "Shelf"]
    # Sanitize sql queries
    for result in c.execute(cmd, ['%' + phrase + '%']):
        results.append(result)
    return pd.DataFrame(results, columns=columns)

def log_query(phrase):
    conn = sqlite3.connect('log/log.db', check_same_thread = False)
    t = dt.now()
    stamp = [phrase, t.strftime("%w"), t.strftime("%Y-%m-%d %H:%M:%S")]
    cmd = ("INSERT INTO log "
            "(Phrase, Weekday, Datetime) "
            "VALUES "
            "(?, ?, ?)")
    conn.execute(cmd, stamp);
    conn.commit()

@app.route("/")
def main():
    return render_template('view.html')


@app.route("/", methods=['POST'])
def do_search():
    results = []
    options = request.form.getlist('sub_db')
    phrase = str(request.form['phrase'])
    log_query(phrase)
    for option in options:
        df = search(phrase, option)
        ### Styling effects
#        df.set_index(['Name'], inplace=True)
#        df.index.name = None
        ###
        if not df.empty:
            results.append("<h2>Results in {}:</h2>".format(option))
            results.append(df.to_html())
        else:
            results.append("<h2>No results in {} </h2><br>".format(option))
    return render_template('view.html',
            tables = results) # Presented as list to allow multisearch

@app.route("/", methods = ['POST'])
def generate_report():
    df = gr.fetch_data()
    img = BytesIO()
    gr.top_terms(df)
    gr.plt.savefig(img, format ='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue())

    return render_template('view.html', plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)

