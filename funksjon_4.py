#Skriv ut studieplanen med hvilke emner som er i hvert semester


t=1
def skriv_ut_studieplan(studieplan_liste):
    for i in range(len(studieplan_liste)):
        print(f"Semester {t} = {studieplan_liste[i]}")
        t=t+1
