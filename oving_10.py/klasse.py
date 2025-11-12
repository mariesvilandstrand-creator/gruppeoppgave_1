

def emne_i_studieplan(self):
    for i in range (6):
        print (f"\n semester 1: \n {self.emnekode[i]}")


class Emne():
    def __init__(self, navn, emnekode, semester = 0, studiepoeng = 0):
        self.navn = navn
        self.emnekode = emnekode
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f"\n navn : {self.navn} \n emnekode : {self.emnekode} \n semester : {self.semester} \n studiepoeng : {self.studiepoeng} \n"
    
    def semester_til_emnet(self):
        return self.semester
    

class Studieplan():
    def __init__(self, ID, navn, studiepoeng, emne):
        self.ID = ID
        self.navn = navn
        self.studiepoeng =  [[],[],[],[],[],[]]
        self.emne =  [[],[],[],[],[],[]]
            
    def __str__(self):
        return f"\n student-ID : {self.ID} \n studie : {self.navn} \n emne :{emne_i_studieplan()} "
    
