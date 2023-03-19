"""
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

""" Import """
from Mahasiswa import Mahasiswa
from Dosen import Dosen

""" Kelas Asprak """
class Asprak(Mahasiswa):
    # private
    __matkul = ""
    __dosen = Dosen()

    # constructor
    def __init__(self, nama="", jenis_kelamin="", nim="", peralatan="", matkul="", dosen=Dosen()):
        super().__init__(nama, jenis_kelamin, nim, peralatan)
        self.__matkul = matkul
        self.__dosen = dosen

    # setter and getter
    def setMatkul(self, matkul):
        self.__matkul = matkul
    def setDosen(self, dosen):
        self.__dosen = dosen
    def getMatkul(self):
        return self.__matkul
    def getDosen(self):
        return self.__dosen
    
    # methods
    def homework(self):
        print(self.getName(), "(", self.getGender(), ")", "is giving homework")