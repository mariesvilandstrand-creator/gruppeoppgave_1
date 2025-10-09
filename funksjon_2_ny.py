#Legg til et emne i studieplanen: En studieplan består av seks semester nummeret 1-6
#hvor semester 1, 3 og 5 er høstsemester og semester 2, 4 og 6 er vårsemestre. Hvert
#semester kan representeres som ei liste med indekser inn i emne-listene. Dere skal også
#sjekke at et emne er lovlig i det semesteret brukeren prøver å legge det inn i. Det
#involverer følgende:
#o Sjekk at emnet ikke allerede er med i studieplanen. Et emne skal bare kunne
#legges til en gang.
#o Sjekk at emnet legges til i et gyldig semester. Høstemner skal bare kunne legges
#til i semester 1, 3 eller 5. Våremner skal bare kunne legges til i semester 2, 4 eller
#6.
#o Sjekk at det er plass i semesteret til emnet. Et semester skal inneholder
#maksimalt 30 studiepoeng med emner

def funksjon_2_ny(studieplan_liste, semester_liste, emnekode_liste, studiepoeng_sum, studiepoeng_liste):
    print(emnekode_liste)
    while True:
        try:
            hvilket_emne=int(input("Hvilket emne vil du legge inn i studieplanen din?(skriv inn tallet i rekken som emnet ditt er i): "))-1
            if hvilket_emne>len(emnekode_liste):
                print("feil")
                continue
            break
        except ValueError:
            print("FEIL")
    hvilket_semester=semester_liste[x]
    studieplan_liste[hvilket_semester].append(emnekode_liste[hvilket_emne])
    studiepoeng_sum[hvilket_semester].append(studiepoeng_liste[hvilket_emne])
    if sum(studiepoeng_sum[hvilket_semester])>30:
        print("Du har lagt til for mange studiepoeng! Jeg fjerner de fra listen")
        studieplan_liste[hvilket_semester].remove(emnekode_liste[hvilket_emne])
        studiepoeng_sum[hvilket_semester].remove(studiepoeng_liste[hvilket_emne])
    else:
        print(f"Dette er din foreløpige studieplan: {studieplan_liste}")