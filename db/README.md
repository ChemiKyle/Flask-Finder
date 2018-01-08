# Verbose instructions for new users

This program has been written with users with no programming experience in mind. Information is stored in the common `.csv` format for ease of use. Templates are provided that work with the included scripts to port them into the database.

Inventory is grouped into 3 categories:
1. Chemical - `chem_inv.csv`
   - Intended for chemical stock, includes optional space for MSDS and CAS information to expedite creation of reports for EH&S
2. Stock - `stock_inv.csv`
   - Intended for depletable, but non-chemical items (e.g. solder, pipette tips, gloves, etc.)
3. Equipment - `equipment_inv.csv`
   - Intended for non-depletable, non-chemical inventory (e.g. soldering irons, micropipettes, face shields, etc.)

After filling in information from your own laboratory and saving the `.csv` files, the `inv.db` file can be updated by running opening a terminal session in the `/db` folder and typing `bash update_all.sh`; this can also create a datestamped copy of each `.csv` which can be toggled by changing the first line from `backups=false` to `backups=true`.
