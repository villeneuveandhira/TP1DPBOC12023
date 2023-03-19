"""
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

""" Import """
from Human import Human

""" Kelas Mahasiswa """
class Mahasiswa(Human):
    # private
    __num = ""     ## NIM
    __tool = ""    ## Peralatan

    # constructor
    def __init__(self, nama="", jenis_kelamin="", nim="", peralatan=""):
        super().__init__(nama, jenis_kelamin)
        self.__num = nim
        self.__tool = peralatan

    # setter and getter
    def setNumMahasiswa(self, nim):
        self.__num = nim
    def setToolMahasiswa(self, peralatan):
        self.__tool = peralatan
    def getNumMahasiswa(self):
        return self.__num
    def getToolMahasiswa(self):
        return self.__tool
    
    # methods
    def study(self):
        print(self.getName(), "(", self.getGender(), ")", "is studying!")
    def attend(self):
        print(self.getName(), "(", self.getGender(), ")", "is attending class!")
    def assignment(self):
        print(self.getName(), "(", self.getGender(), ")", "is working on assignment!")