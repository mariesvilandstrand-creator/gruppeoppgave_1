#Skriv ut studieplanen med hvilke emner som er i hvert semester



def skriv_ut_studieplan(studieplan_liste):
    t=1
    for i in range(len(studieplan_liste)):
        emner = ", ".join(studieplan_liste[i])
        print(f"Semester {t} = {emner}")
        t=t+1
