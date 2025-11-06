class Klasse():
    def __init__(self, navn, emnekode, semester, studiepoeng):
        self.navn = navn
        self.emnekode = emnekode
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f"\n navn : {self.navn} \n emnekode : {self.emnekode} \n semester : {self.semester} \n studiepoeng : {self.studiepoeng} \n"
    

class Studieplan():
    def __init__(self, ID, tittel, s1, s2, s3, s4, s5, s6):
        