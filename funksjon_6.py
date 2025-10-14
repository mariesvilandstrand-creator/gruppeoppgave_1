#Lagre emnene og studieplanen til fil. Lag ei eller flere tekstfiler med denne
#informasjonen, det er opp til dere å finne ut hvilket format denne fila skal ha

def lagre_emne_studieplan_fil():
    with open ("studieplan_fil.csv", "a", encoding="UTF-8") as fila:
        for i in len(studieplan_liste):
            fila.write(f"{studieplan_liste[i]}, {emnekode_liste[i]}, {studiepoeng_liste[i]}")