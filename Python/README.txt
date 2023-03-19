# DATA DIRI
NIM : 2108067
Nama : Villeneuve Andhira Suwandhi
Prodi : Ilmu Komputer C1

# FORMAT JANJI
Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Tugas Praktikum 1<br/>
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.<br/>
Aamiin.<br/>

# TP1DPBOC12023
Catatan:
-	Diperbolehkan menambah atribut / properti dan metode baru.
-	Buatlah Class Diagram dari desain yang telah dirancang, serta berikan penjelasannya!
-	Pilihlah satu bahasa yang disukai / dikuasai, kecuali PHP.
-	Diperbolehkan menggunakan konsep yang belum diajarkan, seperti polimorfisme (overload – override),
	kelas abstrak, interface, dan sebagainya.
-	Batas waktu: Minggu, 19 Maret 2023

Challenge (0 - 25 poin):
-	Buatlah interaksi antar objek dengan syarat dan batasan yang didefinisikan sendiri.
	Sebagai contoh, pengurus DPM tidak bisa memberi masukan sebelum ketua BEM melaksanakan prokernya,
	atau dosen yang tidak bisa memberi nilai sebelum asisten memberikan tugas.

# PENJELASAN
![UML](https://user-images.githubusercontent.com/101118033/226180927-1c0cb57a-7fef-40cd-80ac-950266e1f524.png)

Alasan:
1.	Hubungan 'Mahasiswa' dan 'Dosen' dengan 'Human' adalah inheritance:
	-	Secara objek sama, sesama manusia.
	-	Atribut yang digunakan sama, yaitu nama dengan jenis kelamin.
	-	Berbeda kelas karena mempunyai atribut dan kegiatan masing-masing.
2.	Hubungan 'BEM' is a 'Mahasiswa' juga dengan 'DPM' is a 'Mahasiswa':
	-	'BEM' dan 'DPM' merupakan mahasiswa.
	-	Namun dipisah berbeda kelas karena memiliki tugas masing-masing.
3.	Hubungan 'Asprak' is a 'Mahasiswa' also has a 'Dosen':
	-	'Asprak' adalah mahasiswa.
	-	Walaupun bukan dosen tapi 'Asprak' dapat membantu 'Dosen' mengajar dan memberi tugas.

Keterangan:
-	Bahasa pemrograman, Python.
-	Atribut [peralatan] pada 'Mahasiswa' dengan 'Dosen' berbeda.
-	'Mahasiswa' mempunyai peralatan yaitu beberapa textbooks dan laptop,
	sedangkan 'Dosen' mempunyai beberapa markers dan laptop.
