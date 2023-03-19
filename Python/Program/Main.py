"""
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
"""

""" Import """
from os import system
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from BEM import BEM
from DPM import DPM
from Asprak import Asprak

""" Program """
def main():
    # Instantiate
    student = []
    teacher = []
    studentBEM = []
    studentDPM = []
    studentAssist = []

    ##
    # Data (HARDCODED)
    ##
    # Data Mahasiswa
    student.append(Mahasiswa("Afri", "Male", "2001023", "Laptop, Notebook"))
    student.append(Mahasiswa("Anin", "Female", "2004506", "Notebook"))
    # Data Dosen
    teacher.append(Dosen("Mrs.Rose", "Female", "2658", "Laptop, Marker"))
    # Data BEM
    studentBEM.append(BEM("Rapi", "Male", "2108938", "Laptop", "President"))
    # Data DPM
    studentDPM.append(DPM("Alga", "Male", "2105673", "Laptop", "Member"))
    # Data Asprak
    studentAssist.append(Asprak("Najmi", "Female", "2102843", "Notebook", "DPBO", teacher))
    studentAssist.append(Asprak("Bulan", "Male", "2007890", "Laptop", "DPBO", teacher))

    ##
    # Output
    ##
    system("cls")
    print("========================")
    print("=== TP1-DPBO-C1-2023 ===")
    print("========================")
    print("------------------------------------------------------------")
    print("DATA DOSEN")
    i = 0
    for person in teacher:
        print("   No-",i+1)
        print("    - ", "NIP Dosen          : ", person.getNumDosen())
        print("    - ", "Nama Dosen         : ", person.getName())
        print("    - ", "Jenis kelamin      : ", person.getGender())
        print("    - ", "Peralatan Dosen    : ", person.getToolDosen())
        i += 1
    print("------------------------------------------------------------")
    
    print("------------------------------------------------------------")
    print("DATA MAHASISWA")
    i = 0
    for person in student:
        print("   No-",i+1)
        print("    - ", "NIM Mahasiswa          : ", person.getNumMahasiswa())
        print("    - ", "Nama Mahasiswa         : ", person.getName())
        print("    - ", "Jenis kelamin          : ", person.getGender())
        print("    - ", "Peralatan Mahasiswa    : ", person.getToolMahasiswa())
        i += 1
    print("------------------------------------------------------------")

    print("------------------------------------------------------------")
    print("DATA BEM")
    i = 0
    for person in studentBEM:
        print("   No -", i+1)
        print("    - ", "NIM Mahasiswa          : ", person.getNumMahasiswa())
        print("    - ", "Nama Mahasiswa         : ", person.getName())
        print("    - ", "Jenis kelamin          : ", person.getGender())
        print("    - ", "Peralatan Mahasiswa    : ", person.getToolMahasiswa())
        print("    - ", "Jabatan                : ", person.getPositionBEM(), " of BEM")
        i += 1
    print("------------------------------------------------------------")

    print("------------------------------------------------------------")
    print("DATA DPM")
    i = 0
    for person in studentDPM:
        print("   No -", i+1)
        print("    - ", "NIM Mahasiswa          : ", person.getNumMahasiswa())
        print("    - ", "Nama Mahasiswa         : ", person.getName())
        print("    - ", "Jenis kelamin          : ", person.getGender())
        print("    - ", "Peralatan Mahasiswa    : ", person.getToolMahasiswa())
        print("    - ", "Jabatan                : ", person.getPositionDPM(), " of DPM")
        i += 1
    print("------------------------------------------------------------")

    print("------------------------------------------------------------")
    print("DATA ASPRAK")
    i = 0
    for person in studentAssist:
        print("   No -", i+1)
        print("    - ", "NIM Mahasiswa          : ", person.getNumMahasiswa())
        print("    - ", "Nama Mahasiswa         : ", person.getName())
        print("    - ", "Jenis kelamin          : ", person.getGender())
        print("    - ", "Peralatan Mahasiswa    : ", person.getToolMahasiswa())
        print("    - ", "Mata kuliah            : ", person.getMatkul())
        i += 1
    print("------------------------------------------------------------")

    # Schedule
    print()
    print("12 March 2023")
    print("  07.38 AM ", end = ' ')
    student[0].eat()
    print("  11.43 AM ", end = ' ')
    student[1].study()
    print("  04.55 PM ", end = ' ')
    studentBEM[0].planning()
    print("  09.11 PM ", end = ' ')
    studentDPM[0].sleep()

    print()
    print("14 March 2023")
    print("  08.41 AM ", end = ' ')
    student[1].drink()
    print("  09.31 AM ", end = ' ')
    teacher[0].teach()
    print("  09.33 AM ", end = ' ')
    student[1].attend()
    print("  09.36 AM ", end = ' ')
    student[0].attend()
    print("  09.39 AM ", end = ' ')
    studentBEM[0].attend()
    print("  09.39 AM ", end = ' ')
    studentDPM[0].attend()
    print("  11.56 AM ", end = ' ')
    teacher[0].assign()
    print("  17.48 PM ", end = ' ')
    studentBEM[0].working()

    print()
    print("15 March 2023")
    print("  1.22 PM ", end = ' ')
    student[0].assignment()
    print("  3.30 PM ", end = ' ')
    studentAssist[1].homework()

    print()
    print("19 March 2023")
    print("  10.32 AM ", end = ' ')
    teacher[0].score()
    
    print("============================================================")

""" run error """
if __name__ == "__main__":
    main()