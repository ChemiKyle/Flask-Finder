# Shell script to subdivide inventories for printing and posting

echo -n "Enter the location you want to inventory: "
read place
sqlite3 ../inv.db <<EOF

.headers on
.mode csv

.output post_$place.csv
.print $place
SELECT Name,
    Sublocation,
    Layer 
FROM stock
WHERE Location = '$place'
UNION
SELECT Name,
    Sublocation,
    Layer 
FROM equip
WHERE Location = '$place'
ORDER BY
    Sublocation,
    Layer;

.quit
EOF
