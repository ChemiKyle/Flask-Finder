# Flask Finder  
Inventory search for laboratories, developed for use in a large R1 state 
university teaching lab. Intended to be used as a search kiosk on a 
raspberry pi. Includes toggles for searching chemicals, stock, and
equipment separately. 
Written using flask, pandas, and sqlite3. Can be hosted locally or on the web.

![In action](/img/example.png "Use example")

## Preparation
If installing on a fresh pi, open a terminal and enter `sudo apt-get install python3-scipy && pip install flask`, then go get a coffee because that'll take a while.  
Fill in inventories in the .csv files in `/db` (more verbose instructions located in the `/db` folder), then run the `update_all.sh` script to fill sqlite database. No knowledge of SQL needed!

## Use
1. Open a terminal session in the folder where the program has been downloaded
2. Enter `python3 flask_finder.py`
3. Open the web browser and point it at the address flask runs the web app on (typically `127.0.0.1:5000`). 

## TODO: 
- [x] Add logging of queries
- [ ] use ~R~ Python with `Seaborn` to generate monthly reports of search terms and times
