#Pilihan Raya System

import mysql.connector
import bcrypt

table = [
	[" 1", "Pegawai SPR"], #add new user,show bilangan undi,add new calon , user()
	[" 2", "User"], #check Pusat Mengundi, saluran, Masa, undi (PRU/PRN) , Show dah undi atau belum
	[" 3", "Ejen Pilihan Raya"] #check no user ic, user()
]

table2 = [
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
			"(ic VARCHAR(12), "
			"username VARCHAR(200), "
			"password VARCHAR(200), "
			"level VARCHAR(200), "
			"PRIMARY KEY (ic))")

		mydbse.execute("CREATE TABLE IF NOT EXISTS ejen "
			"(ic VARCHAR(12), "
			"username VARCHAR(200), "
			"password VARCHAR(200), "
			"PRIMARY KEY (ic))")

		mydbse.execute("CREATE TABLE IF NOT EXISTS user "
			"(ic VARCHAR(12), "
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
			"ic VARCHAR(12), "
			"fullname VARCHAR(200), "
			"parti VARCHAR(200))")

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
				print(user_data[2].encode('utf-8'))
				print("Selamat kembali, " + username + ".")
				print("SPR Belum Siap")
			else:
				if count == 1:
					print("Kata laluan anda salah. Maaf Anda telah mencapai Had Maksimum iaitu 3 kali. Sila cuba lagi")
					print("\n-------------------------------------------------------------")
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
				spr(3)
			else:
				print("\n-------------------------------------------------------------")
				system()

	except mysql.connector.Error as err:
		print("Gagal log masuk : {}".format(err))

def user():
	username = input("Sila masukkan Nombor Ic anda: ")

	try:
		projectdatabase = database()
		mydbse = projectdatabase.cursor()
		mydbse.execute("SELECT * FROM user WHERE ic=%s",
			(username,))
		user_data = mydbse.fetchone()

		if user_data:
			mydbse.execute("SELECT username FROM user WHERE ic=%s",
				(username,))
			username2 = mydbse.fetchone()[0]

			print("Selamat kembali, " + username2 + ".")
			print("User Belum Siap")
		else:
			print("Nombor Ic anda tiada dalam data, Sila pastikan ic anda betul.")
			askuser = input("Adakah anda mahu Log Masuk Y untuk ya atau mana-mana kunci untuk berhenti? [ Y atau mana-mana kunci ] : ")
			askuser = askuser.upper()
			if askuser == "Y":
				user()
			else:
				print("\n-------------------------------------------------------------")
				system()

	except mysql.connector.Error as err:
		print("Gagal log masuk : {}".format(err))

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
				print("Ejen Belum Siap")
			else:
				if count == 1:
					print("Kata laluan anda salah. Maaf Anda telah mencapai Had Maksimum iaitu 3 kali. Sila cuba lagi")
					print("\n-------------------------------------------------------------")
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
		userchoice = int(input("Please Choose [1 or 2 or 3]: "))
		print()
		if userchoice == 1 or userchoice == 2:
			if userchoice == 1:
				print("\n-------------------------------------------------------------")
				print("                    Log In As Pagawai SPR")
				print("-------------------------------------------------------------\n")
				spr(count)
			elif userchoice == 2:
				print("\n-------------------------------------------------------------")
				print("                    Log In As User")
				print("-------------------------------------------------------------\n")
				user()
		elif userchoice == 3:
			print("\n-------------------------------------------------------------")
			print("                    Log In As Ejen SPR")
			print("-------------------------------------------------------------\n")
			ejen(count)
		else:
			print("\n-------------------------------------------------------------\n")
			print("     You just need to fill either 1 or 2 or 3 !!!")
			print("\n-------------------------------------------------------------\n")
	except ValueError:
		print("\n-------------------------------------------------------------\n")
		print("     You just need to fill either 1 or 2 or 3 !!!")
		print("\n-------------------------------------------------------------\n")

createdatabase()

while True:
	system()