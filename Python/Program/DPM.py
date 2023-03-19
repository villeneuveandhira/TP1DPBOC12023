"""
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

""" Import """
from Mahasiswa import Mahasiswa

""" Kelas DPM """
class DPM(Mahasiswa):
    # private
    __position = ""

    # constructor
    def __init__(self, nama="", jenis_kelamin="", nim="", peralatan="", jabatan=""):
        super().__init__(nama, jenis_kelamin, nim, peralatan)
        self.__position = jabatan

    # setter and getter
    def setPositionDPM(self, jabatan):
        self.__position = jabatan
    def getPositionDPM(self):
        return self.__position
    
    # methods
    def evaluate(self):
        print(self.getName(), "(", self.getGender(), ")", "I appreciate your work!")
    def reccomend(self):
        print(self.getName(), "(", self.getGender(), ")", "recommendations")