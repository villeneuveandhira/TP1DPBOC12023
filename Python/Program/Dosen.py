"""
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

""" Import """
from Human import Human

""" Kelas Dosen """
class Dosen(Human):
    # private
    __num = ""     ## NIP
    __tool = ""    ## Peralatan

    # constructor
    def __init__(self, nama="", jenis_kelamin="", nip="", peralatan=""):
        super().__init__(nama, jenis_kelamin)
        self.__num = nip
        self.__tool = peralatan

    # setter and getter
    def setNumDosen(self, nip):
        self.__num = nip
    def setToolDosen(self, peralatan):
        self.__tool = peralatan
    def getNumDosen(self):
        return self.__num
    def getToolDosen(self):
        return self.__tool
    
    # methods
    def teach(self):
        print(self.getName(), "is teaching!")
    def assign(self):
        print(self.getName(), "is giving a new assignment!")
    def score(self):
        print(self.getName(), "is giving score!")