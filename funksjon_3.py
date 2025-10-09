#Skriv ut ei liste over alle registrerte emner



def skriv_ut_liste(emnekode_liste, semester_liste, studiepoeng_liste):
    for i in range(len(emnekode_liste)):
        print(f"Emnekoden = {emnekode_liste[i]:.2f}, Studiepoeng = {studiepoeng_liste[i]:.2f}, semester_liste = {semester_liste[i]:.2f}")
