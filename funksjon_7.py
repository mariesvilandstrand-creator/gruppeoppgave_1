#Les inn emnene og studieplanen fra fil. Denne skal lese samme fil som bel skrevet i
#punkt 6.

import csv

with open("studieplan_fil.csv", "r") as fila:
    csvreader = csv.reader(fila)
    
    for row in csvreader:
        if not row:
            continue
        print(row)
