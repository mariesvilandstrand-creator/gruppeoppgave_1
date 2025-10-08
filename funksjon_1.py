#Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
#eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
#semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
#listene representerer samme emne




semester_liste=[]
emnekode_liste=[]
studiepoeng_liste=[]

def legg_til_nytt_emne():
    emnekode=input("Hva er emnekoden?")
    while len(emnekode) > 6 and len(emnekode)<6:
        emnekode=input("Hva er emnekoden?")
    emnekode_liste.append(emnekode)
    semester=input("Er det på høst eller vår? host/vaar: ").lower()
    while semester!= "host" and semester!= "vaar":
        print("IKKE GYLDIG. husk å skrive host eller vaar")
        semester=input("Er det på høst eller vår?")
    if semester=="host":
        semester_liste.append("host")
    if semester=="vaar":
        semester_liste.append("vaar")
    studiepoeng=int(input("Hvor mange studiepoeng?"))
    while studiepoeng>60 or studiepoeng<5:
        print("Ugyldig poengsum, prøv igjen")
        studiepoeng=int(input("Hvor mange studiepoeng?"))
    studiepoeng_liste.append(studiepoeng)
    print("du er gudd")