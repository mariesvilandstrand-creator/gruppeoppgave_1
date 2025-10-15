import csv

def lagre_emne_studieplan_fil(studieplan_liste, studiepoeng_sum):
    with open ("studieplan_fil.csv", "a", newline="", encoding="UTF-8") as fila:
        skriver=csv.writer(fila)
        for i in range(len(studieplan_liste)):
            fila.write(f"{(studieplan_liste[i][0])},{(studiepoeng_sum[i][0])}\n")
            fila.write(f"{(studieplan_liste[i][1])},{(studiepoeng_sum[i][1])}\n")
            fila.write(f"{(studieplan_liste[i][2])},{(studiepoeng_sum[i][2])}\n")
            fila.write(f"{(studieplan_liste[i][3])},{(studiepoeng_sum[i][3])}\n")
            fila.write(f"{(studieplan_liste[i][4])},{(studiepoeng_sum[i][4])}\n")
            fila.write(f"{(studieplan_liste[i][5])},{(studiepoeng_sum[i][5])}\n")