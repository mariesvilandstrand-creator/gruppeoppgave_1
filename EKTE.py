#Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
#eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
#semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
#listene representerer samme emne


from funksjon_1 import*

from funksjon_2_ny import*

from funksjon_3 import*

from funksjon_4 import*

from funksjon_5 import*

from funksjon_6_ny import*

from funksjon_7 import*

def emne_i_studieplan(self):
    for i in range (6):
        print (f"\n semester 1: \n {self.emnekode[i]}")


class Emne():
    def __init__(self, navn, emnekode, semester, studiepoeng):
        self.navn = navn
        self.emmnekode = emnekode
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f"\n navn : {self.navn} \n emnekode : {self.emnekode} \n semester : {self.semester} \n studiepoeng : {self.studiepoeng} \n"
    

class Studieplan():
    def __init__(self, ID, navn, emne):
        self.ID = ID
        self.navn = navn
        self.emne = []
        for i in range (6):
            self.emne.append([])
            
    
    def __str__(self):
        return f"\n student-ID : {self.ID} \n studie : {self.navn} \n emne :{emne_i_studieplan()} "
    
    

semester_liste=[]
emnekode_liste=[]
studiepoeng_liste=[]
aarstid_liste=[]
studieplan_liste=[[],[],[],[],[],[]]
studiepoeng_sum=[[],[],[],[],[],[]]


        
while True:
    with open("menyvalg_tekst", "r", encoding="UTF-8") as fila:
        print(fila.read())
    ip = input(f"Hva vil du gjøre?").lower().strip()
    match ip:
        case "1" :
            legg_til_nytt_emne(emnekode_liste, semester_liste, studiepoeng_liste, aarstid_liste)
        case "2" :
            funksjon_2_ny(studieplan_liste, semester_liste, emnekode_liste, studiepoeng_sum, studiepoeng_liste)
        case "3" :
            skriv_ut_liste(emnekode_liste, semester_liste, studiepoeng_liste)
        case "4" :
            skriv_ut_studieplan(studieplan_liste)
        case "5" :
            sjekk_studieplan(studiepoeng_sum)
        case "6" :
            lagre_emne_studieplan_fil(studieplan_liste, studiepoeng_sum)
        case "7" :
            les_inn()
        case "8" :
            break
        case _:
            print("ugyldig commando:", ip)

print(emnekode_liste)
print(studiepoeng_liste)
print(studieplan_liste)