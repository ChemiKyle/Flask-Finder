backup=false

if $backup; then
    cp chem_inv.csv chem_inv_$(date +%Y-%m-%d).csv
    cp equipment_inv.csv equipment_inv_$(date +%Y-%m-%d).csv
    cp stock_inv.csv stock_inv_$(date +%Y-%m-%d).csv
fi

# Chemical
sqlite3 inv.db <<EOF
DROP TABLE chem;
DROP TABLE equip;
DROP TABLE stock;
.mode csv
.import chem_inv.csv chem
.import equipment_inv.csv equip
.import stock_inv.csv stock
.exit
EOF

