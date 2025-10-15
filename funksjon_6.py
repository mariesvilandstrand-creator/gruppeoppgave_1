#Lagre emnene og studieplanen til fil. Lag ei eller flere tekstfiler med denne
#informasjonen, det er opp til dere å finne ut hvilket format denne fila skal ha
import csv

def lagre_emne_studieplan_fil(studieplan_liste, studiepoeng_liste):
    with open ("studieplan_fil.csv", "a", encoding="UTF-8") as fila:
        skriver=csv.writer(fila)
        for i in range(len(studieplan_liste)):
            fila.write(f"1, {str(studieplan_liste[i][0])}, {str(studiepoeng_liste[i][0])}\n")
            fila.write(f"2, {str(studieplan_liste[i][1])}, {str(studiepoeng_liste[i][1])}\n")       
            fila.write(f"3, {str(studieplan_liste[i][2])}, {str(studiepoeng_liste[i][2])}\n")
            fila.write(f"4, {str(studieplan_liste[i][3])}, {str(studiepoeng_liste[i][3])}\n")
            fila.write(f"5, {str(studieplan_liste[i][4])}, {str(studiepoeng_liste[i][4])}\n")
            fila.write(f"6, {str(studieplan_liste[i][5])}, {str(studiepoeng_liste[i][5])}\n")