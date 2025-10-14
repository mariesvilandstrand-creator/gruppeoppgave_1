import csv



with open("studieplan_fil.csv", "r") as fila:
    csvreader = csv.reader(fila)
    
    for row in csvreader:
        print(row[1])