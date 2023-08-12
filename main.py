#Pilihan Raya System

import mysql.connector
import bcrypt
import random

table = [
	[" 1", "Pegawai SPR"],
	[" 2", "User"], #check Pusat Mengundi, saluran, Masa, undi (PRU/PRN) , Show dah undi atau belum
	[" 3", "Ejen Pilihan Raya"] #check no user ic, user()
]

table2 = [
	[" 1", "Daftar Pegawai SPR Baru"],
	[" 2", "Daftar Ejen Pilihan Raya Baru"],
	[" 3", "Daftar User Baru"], 					#belum
	[" 4", "Daftar calon Pilihan Raya"], 			#belum
	[" 5", "Lihat Bilangan Kehadiran Pilihan Raya"],#belum
	[" 6", "Lihat Keputusan Pilihan Raya"], 		#belum
	[" 7", "Lihat Keputusan Penuh Pilihan Raya"], 	#belum
	[" 8", "Undi"], 								#belum
	[" 9", "Log Out"] 								#belum
]

table3 = [
	[" 1", "Daftar Ejen Pilihan Raya Baru"],
	[" 2", "Daftar User Baru"], 					#belum
	[" 3", "Daftar calon Pilihan Raya"], 			#belum
	[" 4", "Lihat Bilangan Kehadiran Pilihan Raya"],#belum
	[" 5", "Lihat Keputusan Pilihan Raya"], 		#belum
	[" 6", "Lihat Keputusan Penuh Pilihan Raya"], 	#belum
	[" 7", "Undi"], 								#belum
	[" 8", "Log Out"] 								#belum
]

def database():
	return mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="pilihanraya")

def createdatabase():
	try:
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="")

		myprojectdb = mydb.cursor()
		myprojectdb.execute("CREATE DATABASE IF NOT EXISTS pilihanraya")

		projectdatabase = database()
		mydbse = projectdatabase.cursor()

		mydbse.execute("CREATE TABLE IF NOT EXISTS spr "
			"(ic VARCHAR(200), "
			"username VARCHAR(200), "
			"password VARCHAR(200), "
			"level VARCHAR(200), "
			"PRIMARY KEY (ic))")

		mydbse.execute("CREATE TABLE IF NOT EXISTS ejen "
			"(ic VARCHAR(200), "
			"username VARCHAR(200), "
			"password VARCHAR(200), "
			"PRIMARY KEY (ic))")

		mydbse.execute("CREATE TABLE IF NOT EXISTS user "
			"(ic VARCHAR(200), "
			"fullname VARCHAR(200), "
			"date VARCHAR(200), "
			"gender VARCHAR(200), "
			"pusatmengundi VARCHAR(200), "
			"saluran VARCHAR(200), "
			"masa VARCHAR(200), "
			"undianparti VARCHAR(200), "
			"undian INT, "
			"PRIMARY KEY (ic))")

		mydbse.execute("CREATE TABLE IF NOT EXISTS calon "
			"(tempatbertanding VARCHAR(200), "
			"ic VARCHAR(200), "
			"fullname VARCHAR(200), "
			"parti VARCHAR(200),"
            "PRIMARY KEY (ic))")

		try:
			projectdatabase = database()
			mydbse = projectdatabase.cursor()
			mydbse.execute("SELECT * FROM spr WHERE username=%s",
				("admin",))
			sameinpt = mydbse.fetchone()

			if not sameinpt:
				ic="admin"
				ic = bcrypt.hashpw(ic.encode('utf-8'), bcrypt.gensalt())

				passwrd = "admin"
				passwrd = bcrypt.hashpw(passwrd.encode('utf-8'), bcrypt.gensalt())
				mydbse.execute("INSERT INTO spr"
					"(ic, username, password, level)"
					"VALUES(%s, %s , %s ,%s)",
					(ic, "admin", passwrd , "admin"))
				projectdatabase.commit()

		except mysql.connector.Error as err:
			print("Failed to Insert data: {}".format(err))

	except mysql.connector.Error as err:
		print("Error: {}".format(err))

def ictoanything(ic,username):
	tahun=int(ic[0:2])
	if tahun >= 0 and tahun <= 24 :
		tahun += 2000
	else:
		tahun +=1900

	bulan=int(ic[2:4])
	if bulan < 1 or bulan > 12 :
		print("Bulan Di Nombor Ic tidak valid... Sila pastikan anda mengisi nombor Ic yang betul")
		sprsystem(username)
	else:
		if bulan == 1 :
			bln = "JANUARI"
		elif bulan == 2 :
			bln = "FEBUARI"
		elif bulan == 3 :
			bln = "MAC"
		elif bulan == 4 :
			bln = "APRIL"
		elif bulan == 5 :
			bln = "MEI"
		elif bulan == 6 :
			bln = "JUN"
		elif bulan == 7 :
			bln = "JULAI"
		elif bulan == 8 :
			bln = "OGOS"
		elif bulan == 9 :
			bln = "SEPTEMBER"
		elif bulan == 10 :
			bln = "OKTOBER"
		elif bulan == 11 :
			bln = "NOVEMBER"
		elif bulan == 12 :
			bln = "DISEMBER"

		hari = int(ic[4:6])
		if hari < 1 or hari > 31 :
			print("Tarikh Lahir Di Nombor Ic tidak valid... Sila pastikan anda mengisi nombor Ic yang betul")
			sprsystem(username)
		else:
			DOB = str(hari) + " " + bln + " " + str(tahun)
			umur = 2023 - tahun
			if umur < 18 :
				print("Umur Pengundi Mestilah melebihi 18 Tahun")
				sprsystem(username)
			else:
				jntina=int(ic)
				jntina%=2
				if jntina == 0:
					jantina = "PEREMPUAN"
				else :
					jantina = "LELAKI"

				negeriasal=int(ic[6:8])
				if negeriasal==1 or negeriasal==21 or negeriasal==22 or negeriasal==23 or negeriasal==24:
					negeri="Johor"
				elif negeriasal==2 or negeriasal==25 or negeriasal==26 or negeriasal==27:
					negeri="Kedah"
				elif negeriasal==3 or negeriasal==28 or negeriasal==29:
					negeri="Kelantan"
				elif negeriasal==4 or negeriasal==30 :
					negeri="Melaka"
				elif negeriasal==5 or negeriasal==31 or negeriasal==59:
					negeri="Negeri Sembilan"
				elif negeriasal==6 or negeriasal==32 or negeriasal==33:
					negeri="Pahang"
				elif negeriasal==7 or negeriasal==34 or negeriasal==35:
					negeri="Pulau Pinang"
				elif negeriasal==8 or negeriasal==36 or negeriasal==37 or negeriasal==38 or negeriasal==39:
					negeri="Perak"
				elif negeriasal==9 or negeriasal==40 :
					negeri="Perlis"
				elif negeriasal==10 or negeriasal==41 or negeriasal==42 or negeriasal==43 or negeriasal==44:
					negeri="Selangor"
				elif negeriasal==11 or negeriasal==45 or negeriasal==46:
					negeri="Terengganu"
				elif negeriasal==12 or negeriasal==47 or negeriasal==48 or negeriasal==49:
					negeri="Sabah"
				elif negeriasal==13 or negeriasal==50 or negeriasal==51 or negeriasal==52 or negeriasal==53:
					negeri="Sarawak"
				elif negeriasal==14 or negeriasal==54 or negeriasal==55 or negeriasal==56 or negeriasal==57:
					negeri="Kuala Lumpur"
				elif negeriasal==15 or negeriasal==58 :
					negeri="Labuan"
				elif negeriasal==16 :
					negeri="Putrajaya"
				else:
					negeri="Negeri Tidak Diketahui"

				return umur,DOB,jantina,negeri

def daftaradminspr(username):
	ic = input("Sila masukkan Nombor Ic : ")
	try:
		umur,DOB,jantina,negeri=ictoanything(ic,username)
		try:
			projectdatabase = database()
			mydbse = projectdatabase.cursor()
			mydbse.execute("SELECT * FROM user ")
			account = mydbse.fetchone()

			if account:
				if bcrypt.checkpw(ic.encode('utf-8'), account[0].encode('utf-8')):
					print("Nombor Ic Telah didaftar. Sila Masukkan Nombor Ic yang lain.")
					sprsystem(username)
				else:
					username2 = input("Sila Masukkan Username : ")
					try:
						projectdatabase = database()
						mydbse = projectdatabase.cursor()
						mydbse.execute("SELECT * FROM spr WHERE username=%s",
							(username2,))
						sameinpt = mydbse.fetchone()

						if not sameinpt:
							passwrd = "123"
							level = input("Account yang anda daftar sebagai ? [Admin atau staf] : ")
							level=level.lower()
							if level=="admin" or level == "staf":
								fullname = input("Sila Masukkan Nama Penuh : ")
								fullname = fullname.upper()
								saluran = random.randint(1, 9)
								masa = "08:00 AM - 06:00 PM"
								undianparti = "Belum Undi"
								undianparti = bcrypt.hashpw(undianparti.encode('utf-8'), bcrypt.gensalt())
								undian = 0
								passwrd = bcrypt.hashpw(passwrd.encode('utf-8'), bcrypt.gensalt())
								ic = bcrypt.hashpw(ic.encode('utf-8'), bcrypt.gensalt())

								mydbse.execute("INSERT INTO spr"
									"(ic, username, password, level)"
									"VALUES(%s, %s , %s ,%s)",
									(ic, username2, passwrd , level))

								mydbse.execute("INSERT INTO user"
									"(ic, fullname, date, gender, pusatmengundi, saluran, masa, undianparti, undian)"
									"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
									(ic, fullname, DOB, jantina, negeri, saluran, masa, undianparti, undian))

								projectdatabase.commit()
								print("Pendaftaran Selesai ...")
								print("\n-------------------------------------------------------------\n")
								print("Nama Penuh : "+fullname+"\nTarikh Lahir : "+DOB+"\nUmur : "+str(umur)+
									"\nPusat Mengundi : "+negeri+"\n Saluran Mengundi : "+str(saluran))
								sprsystem(username)
							else :
								print("\n-------------------------------------------------------------\n")
								print("  Anda hanya perlu mengisi sama ada admin atau staf !!!")
								print("\n-------------------------------------------------------------\n")
								daftaradminspr(username)

						else:
							print("Username Anda telah berdaftar. Sila Masukkan username yang lain.")
							sprsystem(username)

					except mysql.connector.Error as err:
						print("Failed to Insert data: {}".format(err))
						sprsystem(username)
					
		except Exception as e:
			print("Error:", e)
			sprsystem(username)
	except :
		print("Nombor Ic Tidak Valid ... Sila pastikan anda mengisi nombor Ic yang betul..")
		sprsystem(username)

def daftarejenspr(username):
	ic = input("Sila masukkan Nombor Ic : ")
	try:
		umur,DOB,jantina,negeri=ictoanything(ic,username)
		try:
			projectdatabase = database()
			mydbse = projectdatabase.cursor()
			mydbse.execute("SELECT * FROM user")
			account = mydbse.fetchone()

			if account:
				if bcrypt.checkpw(ic.encode('utf-8'), account[0].encode('utf-8')):
					print("Nombor Ic Telah didaftar. Sila Masukkan Nombor Ic yang lain.")
					sprsystem(username)
				else:
					username2 = input("Sila Masukkan Username : ")
					try:
						projectdatabase = database()
						mydbse = projectdatabase.cursor()
						mydbse.execute("SELECT * FROM ejen WHERE username=%s",
							(username2,))
						sameinpt = mydbse.fetchone()

						if not sameinpt:
							passwrd = "123"
							fullname = input("Sila Masukkan Nama Penuh : ")
							fullname = fullname.upper()
							saluran = random.randint(1, 9)
							masa = "08:00 AM - 06:00 PM"
							undianparti = "Belum Undi"
							undianparti = bcrypt.hashpw(undianparti.encode('utf-8'), bcrypt.gensalt())
							undian = 0
							passwrd = bcrypt.hashpw(passwrd.encode('utf-8'), bcrypt.gensalt())
							ic = bcrypt.hashpw(ic.encode('utf-8'), bcrypt.gensalt())

							mydbse.execute("INSERT INTO ejen"
								"(ic, username, password)"
								"VALUES(%s, %s , %s)",
								(ic, username2, passwrd))

							mydbse.execute("INSERT INTO user"
								"(ic, fullname, date, gender, pusatmengundi, saluran, masa, undianparti, undian)"
								"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
								(ic, fullname, DOB, jantina, negeri, saluran, masa, undianparti, undian))

							projectdatabase.commit()
							print("Pendaftaran Selesai ...")
							print("\n-------------------------------------------------------------\n")
							print("Nama Penuh : "+fullname+"\nTarikh Lahir : "+DOB+"\nUmur : "+str(umur)+
								"\nPusat Mengundi : "+negeri+"\n Saluran Mengundi : "+str(saluran))
							sprsystem(username)
							
						else:
							print("Username Anda telah berdaftar. Sila Masukkan username yang lain.")
							sprsystem(username)

					except mysql.connector.Error as err:
						print("Failed to Insert data: {}".format(err))
						sprsystem(username)
					
		except Exception as e:
			print("Error:", e)
			sprsystem(username)
	except :
		print("Nombor Ic Tidak Valid ... Sila pastikan anda mengisi nombor Ic yang betul..")
		sprsystem(username)

def sprsystem(username):
	username=username.lower()
	print("\n-------------------------------------------------------------")
	print("                    Pegawai SPR : "+username)
	print("-------------------------------------------------------------\n")
	if username == "admin":
		for row in table2:
			for col in row:
				print(col, end="\t")
			print()
		print("-------------------------------------------------------------")

		try:
			userchoice = int(input("Sila Pilih [1 atau 2 atau 3 atau 4 atau 5 atau 6 atau 7 atau 8 atau 9]: "))
			print()
			if userchoice == 1 or userchoice == 2:
				if userchoice == 1:
					print("\n-------------------------------------------------------------")
					print("                   Daftar Pegawai SPR Baru")
					print("-------------------------------------------------------------\n")
					daftaradminspr(username)
				elif userchoice == 2:
					print("\n-------------------------------------------------------------")
					print("                   Daftar Ejen SPR Baru")
					print("-------------------------------------------------------------\n")
					daftarejenspr(username)
			elif userchoice == 3:
				print("belum siap")
			elif userchoice == 4:
				print("belum siap")
			elif userchoice == 5:
				print("belum siap")
			elif userchoice == 6:
				print("belum siap")
			elif userchoice == 7:
				print("belum siap")
			elif userchoice == 8:
				print("belum siap")
			elif userchoice == 9:
				system()
			else:
				print("\n-------------------------------------------------------------\n")
				print("  Anda hanya perlu mengisi sama ada 1 atau 2 atau 3 atau 4 atau 5 atau 6 atau 7 atau 8 atau 9 !!!")
				print("\n-------------------------------------------------------------\n")
				sprsystem(username)
		except ValueError:
			print("\n-------------------------------------------------------------\n")
			print("  Anda hanya perlu mengisi sama ada 1 atau 2 atau 3 atau 4 atau 5 atau 6 atau 7 atau 8 atau 9 !!!")
			print("\n-------------------------------------------------------------\n")
			sprsystem(username)
	else:
		for row in table3:
			for col in row:
				print(col, end="\t")
			print()
		print("-------------------------------------------------------------")

		try:
			userchoice = int(input("Please Choose [1 or 2 or 3 or 4 or 5 or 6 or 7 or 8]: "))
			print()
			if userchoice == 1 or userchoice == 2:
				if userchoice == 1:
					print("\n-------------------------------------------------------------")
					print("                   Daftar Ejen SPR Baru")
					print("-------------------------------------------------------------\n")
					daftarejenspr(username)
				elif userchoice == 2:
					print("belum siap")
			elif userchoice == 3:
				print("belum siap")
			elif userchoice == 4:
				print("belum siap")
			elif userchoice == 5:
				print("belum siap")
			elif userchoice == 6:
				print("belum siap")
			elif userchoice == 7:
				print("belum siap")
			elif userchoice == 8:
				system()
			else:
				print("\n-------------------------------------------------------------\n")
				print("  Anda hanya perlu mengisi sama ada 1 atau 2 atau 3 atau 4 atau 5 atau 6 atau 7 atau 8 !!!")
				print("\n-------------------------------------------------------------\n")
				sprsystem(username)
		except ValueError:
			print("\n-------------------------------------------------------------\n")
			print("  Anda hanya perlu mengisi sama ada 1 atau 2 atau 3 atau 4 atau 5 atau 6 atau 7 atau 8 !!!")
			print("\n-------------------------------------------------------------\n")
			sprsystem(username)

def spr(count):
	username = input("Sila Masukkan Username Anda: ")

	try:
		projectdatabase = database()
		mydbse = projectdatabase.cursor()
		mydbse.execute("SELECT * FROM spr WHERE username=%s",
			(username,))
		user_data = mydbse.fetchone()

		if user_data:
			passwrd = input("Sila Masukkan Password Anda: ")
			if bcrypt.checkpw(passwrd.encode('utf-8'), user_data[2].encode('utf-8')):
				print("Selamat kembali, " + username + ".")
				sprsystem(username)
			else:
				if count == 1:
					print("Kata laluan anda salah. Maaf Anda telah mencapai Had Maksimum iaitu 3 kali percubaan. Sila cuba lagi")
					system()
				else:
					count -= 1
					print("Kata laluan anda salah. Sila cuba lagi. Anda hanya mempunyai " + str(count) + " peluang lagi")
					print("\n-------------------------------------------------------------")
					spr(count)
		else:
			print("Akaun Pegawai SPR anda tiada dalam data, Adakah anda serius anda Adalah Pegawai SPR?")
			askuser = input("Adakah anda mahu Log Masuk Y untuk ya atau mana-mana kunci untuk berhenti? [ Y atau mana-mana kunci ] : ")
			askuser = askuser.upper()
			if askuser == "Y":
				print("\n-------------------------------------------------------------")
				print("                    Log Masuk Sebagai Pegawai SPR")
				print("-------------------------------------------------------------\n")
				spr(3)
			else:
				print("\n-------------------------------------------------------------")
				system()

	except mysql.connector.Error as err:
		print("Gagal log masuk : {}".format(err))

def usersystem(username):
	print("\n-------------------------------------------------------------")
	print("                         "+username)
	print("-------------------------------------------------------------\n")
	print("User System Belum Siap")

def user():
	username = input("Sila masukkan Nombor Ic anda: ")

	try:
		projectdatabase = database()
		mydbse = projectdatabase.cursor()
		mydbse.execute("SELECT * FROM user ")
		user_data = mydbse.fetchone()

		if user_data:
			if bcrypt.checkpw(username.encode('utf-8'), user_data[0].encode('utf-8')):
				mydbse.execute("SELECT username FROM user WHERE ic=%s",
					(user_data[0],))
				username2 = mydbse.fetchone()[0]

				print("Selamat kembali, " + username2 + ".")
				usersystem(username)
			else:
				print("Nombor Ic anda tiada dalam data, Sila pastikan ic anda betul.")
				askuser = input("Adakah anda mahu Log Masuk Y untuk ya atau mana-mana kunci untuk berhenti? [ Y atau mana-mana kunci ] : ")
				askuser = askuser.upper()
				if askuser == "Y":
					print("\n-------------------------------------------------------------")
					print("                    Log Masuk Sebagai User")
					print("-------------------------------------------------------------\n")
					user()
				else:
					print("\n-------------------------------------------------------------")
					system()

	except mysql.connector.Error as err:
		print("Gagal log masuk : {}".format(err))

def ejensystem(username):
	print("\n-------------------------------------------------------------")
	print("                    Ejen SPR : "+username)
	print("-------------------------------------------------------------\n")
	print("ejen System Belum Siap")

def ejen(count):
	username = input("Sila Masukkan Username Anda: ")

	try:
		projectdatabase = database()
		mydbse = projectdatabase.cursor()
		mydbse.execute("SELECT * FROM ejen WHERE username=%s",
			(username,))
		user_data = mydbse.fetchone()

		if user_data:
			passwrd = input("Sila Masukkan Password Anda: ")
			if bcrypt.checkpw(passwrd.encode('utf-8'), user_data[2].encode('utf-8')):
				print("Selamat kembali, " + username + ".")
				ejensystem(username)
			else:
				if count == 1:
					print("Kata laluan anda salah. Maaf Anda telah mencapai Had Maksimum iaitu 3 kali. Sila cuba lagi")
					system()
				else:
					count -= 1
					print("Kata laluan anda salah. Sila cuba lagi. Anda hanya mempunyai " + str(count) + " peluang lagi")
					print("\n-------------------------------------------------------------")
					ejen(count)
		else:
			print("Akaun Pegawai SPR anda tiada dalam data, Adakah anda serius anda Adalah Pegawai SPR?")
			askuser = input("Adakah anda mahu Log Masuk Y untuk ya atau mana-mana kunci untuk berhenti? [ Y atau mana-mana kunci ] : ")
			askuser = askuser.upper()
			if askuser == "Y":
				print("\n-------------------------------------------------------------")
				print("                    Log Masuk Sebagai Ejen SPR")
				print("-------------------------------------------------------------\n")
				ejen(3)
			else:
				print("\n-------------------------------------------------------------")
				system()

	except mysql.connector.Error as err:
		print("Gagal log masuk : {}".format(err))

def system():
	count=3
	print("-------------------------------------------------------------")
	for row in table:
		for col in row:
			print(col, end="\t")
		print()
	print("-------------------------------------------------------------")

	try:
		userchoice = int(input("Sila Pilih [1 atau 2 atau 3]: "))
		print()
		if userchoice == 1 or userchoice == 2:
			if userchoice == 1:
				print("\n-------------------------------------------------------------")
				print("                    Log Masuk Sebagai Pegawai SPR")
				print("-------------------------------------------------------------\n")
				spr(count)
			elif userchoice == 2:
				print("\n-------------------------------------------------------------")
				print("                    Log Masuk Sebagai User")
				print("-------------------------------------------------------------\n")
				user()
		elif userchoice == 3:
			print("\n-------------------------------------------------------------")
			print("                    Log Masuk Sebagai Ejen SPR")
			print("-------------------------------------------------------------\n")
			ejen(count)
		else:
			print("\n-------------------------------------------------------------\n")
			print("     Anda hanya perlu mengisi sama ada 1 atau 2 atau 3 !!!")
			print("\n-------------------------------------------------------------\n")
	except ValueError:
		print("\n-------------------------------------------------------------\n")
		print("     Anda hanya perlu mengisi sama ada 1 atau 2 atau 3 !!!")
		print("\n-------------------------------------------------------------\n")

createdatabase()

while True:
	system()
