# Flask Finder  
Inventory search for laboratories, developed for use in a large R1 state 
university teaching lab. Intended to be used as a search kiosk on a 
raspberry pi. Includes toggles for searching chemicals, stock, and
equipment separately. 
Written using flask, pandas, and sqlite3. Can be hosted locally or on the web.

## Preparation
Fill in inventories in a .csv file, in `/db` (more verbose insctructions located in the `/db` folder), run the `update_*.sh` scripts to store a dated copy of the current inventory and fill a sqlite database. No knowledge of SQL needed!

## Use
1. Open a terminal session in the folder where the program has been downloaded
2. Enter `python3 flask_finder.py`
3. Open the web browser and point it at the address flask runs the web app on (typically `127.0.0.1:5000`). 

## TODO: 
[ ] Flesh out `/db` README  
[ ] Add logging of queries, use R to generate monthly reports of search terms and times
