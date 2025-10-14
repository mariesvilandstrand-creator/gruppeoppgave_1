#Sjekk om studieplanen er gyldig eller ikke. En studieplan er bare gyldig hvis hvert av de
#seks semestrene inneholder 30 studiepoeng emner. Er ikke studieplanen gyldig, skriv ut
#hvilke semestre som ikke er gyldige og hvor mange studiepoeng emner det er i det
#semesteret.

from funksjon_4 import skriv_ut_studieplan

def sjekk_studieplan_gyldig():
    gyldig = True
    for i, sem in enumerate(skriv_ut_studieplan, start=1):
        total_sp = sum(e["studiepoeng"] for e in sem)
        if total_sp != 30:
            print(f"Semester {i} har {total_sp} studiepoeng (skal være 30).")
            gyldig = False
    if gyldig:
        print("Studieplanen er gyldig")

