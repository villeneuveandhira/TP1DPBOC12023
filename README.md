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

Penjelasan:
1.	Hubungan 'Mahasiswa' dan 'Dosen' dengan 'Human' adalah inheritance:
	-	Secara objek sama, sesama manusia.
	-	Atribut yang digunakan sama, yaitu nama dengan jenis kelamin.
	-	Berbeda kelas karena mempunyai atribut dan kegiatan masing-masing.
2.	Hubungan 'BEM' is a 'Mahasiswa' juga dengan 'DPM' is a 'Mahasiswa':
	-	'BEM' dan 'DPM' merupakan mahasiswa.
	-	Namun dipisah berbeda kelas karena memiliki tugas masing-masing.
3.	Hubungan 'Asprak' is a 'Mahasiswa' also a 'Dosen' (multiple-inheritance):
	-	'Asprak' adalah mahasiswa.
	-	Walaupun bukan dosen tapi 'Asprak' dapat membantu 'Dosen' mengajar dan memberi tugas.

Keterangan:
-	Bahasa pemrograman, Python. Karena, mendukung multiple-inheritance selain C++ sedangkan Java tidak bisa.
-	Atribut [peralatan] pada 'Mahasiswa' dengan 'Dosen' berbeda.
-	'Mahasiswa' mempunyai peralatan yaitu beberapa textbooks dan laptop,
	sedangkan 'Dosen' mempunyai beberapa markers dan laptop.