"""
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

""" Kelas Human """
class Human:
    # private
    __name = ""     ## Nama
    __gender = ""   ## Jenis_kelamin

    # constructor
    def __init__(self, nama = "", jenis_kelamin = ""):
        self.__name = nama
        self.__gender = jenis_kelamin

    # setter and getter
    def setName(self, nama):
        self.__name = nama
    def setGender(self, jenis_kelamin):
        self.__gender = jenis_kelamin
    def getName(self):
        return self.__name
    def getGender(self):
        return self.__gender
    
    # methods
    def eat(self):
        print(self.__name, "(", self.__gender, ")", "is eating!")
    def drink(self):
        print(self.__name, "(", self.__gender, ")", "is drinking!")
    def sleep(self):
        print(self.__name, "(", self.__gender, ")", "is sleeping!")