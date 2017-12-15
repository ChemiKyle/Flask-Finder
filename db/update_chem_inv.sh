cp chem_inv.csv chem_inv_$(date +%m-%d).csv

sqlite3 inv.db <<EOF
DROP TABLE chem;
.mode csv
.import chem_inv.csv chem
.exit
EOF
