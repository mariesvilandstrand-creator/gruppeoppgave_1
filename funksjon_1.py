#Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
#eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
#semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
#listene representerer samme emne




semester_liste=[]
emnekode_liste=[]
liste=[]
emnekode=input("Hva er emnekoden?")
while emnekode = 8:

semester=input("Er det på høst eller vår? host/vaar: ").lower()
while semester!= "host" and semester!= "vaar":
    print("IKKE GYLDIG. husk å skrive host eller vaar")
    semester=input("Er det på høst eller vår?")
if semester=="host":
    semester_liste.append("host")
if semester=="vaar":
    semester_liste.append("vaar")
