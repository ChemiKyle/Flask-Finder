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
    for result in c.execute(cmd, ['%' + phrase + '%']):
        results.append(result)
    return pd.DataFrame(results,
            columns=["Name", "Quantity", "Unit", "Location", "Shelf"])

@app.route("/")
def main():
    return render_template('view.html')

@app.route("/", methods=['POST'])
def do_search():
    phrase = str(request.form['phrase'])
    # TODO: Use radio buttons to select which table to search from
    # option = str(request.form['sub_db']) # Currently throws bad request error
    df = chem_search(phrase)
    return render_template('view.html', tables = [df.to_html()])

if __name__ == "__main__":
    app.run(debug=True)
