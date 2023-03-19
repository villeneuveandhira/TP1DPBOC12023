"""
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

""" Import """
from Mahasiswa import Mahasiswa

""" Kelas BEM """
class BEM(Mahasiswa):
    # private
    __position = "" ## Jabatan

    # constructor
    def __init__(self, nama="", jenis_kelamin="", nim="", peralatan="", jabatan=""):
        super().__init__(nama, jenis_kelamin, nim, peralatan)
        self.__position = jabatan

    # setter and getter
    def setPositionBEM(self, jabatan):
        self.__position = jabatan
    def getPositionBEM(self):
        return self.__position
    
    # methods
    def planning(self):
        print(self.getName(), "(", self.getGender(), ")", "is planning an innovation!")
    def working(self):
        print(self.getName(), "(", self.getGender(), ")", "is working on innovation!")