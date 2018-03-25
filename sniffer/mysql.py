from datetime import datetime, date, timedelta
import time
import calendar

import socket
import pymysql.cursors
import struct
import textwrap

def main():
	mateo = pymysql.connect(user='root', password='123456789',host='mydbdiseno2.crn0fxtqoene.us-east-1.rds.amazonaws.com', database='dbsyrus')

	cursor = mateo.cursor()

	insertar = ("INSERT INTO syrus" "(latitud, longitud, hora, timems)" "VALUES (%s, %s, %s, %s)")


	conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	conn.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	HOST = "172.31.90.245"
	conn.bind((HOST, 10701))
	
	while True:
		raw_data,addr = conn.recvfrom(65536)
		data = raw_data.decode("utf-8")
		
		if data[0:4] == ">REV":
			print("EL DATO QUE LLEGO "+data)
			lat = (data[16:19]+"."+data[19:24])
			lon = (data[24:28] + "." + data[28:33])
			segundos = int(float(data[11:16]) - (5 * 60 * 60))  # GMZ -5
			dia = int(float(data[10:11]))
			fecha = int(float(data[6:10]))

			if segundos<0:
				fecha = date(1980, 1, 6) + timedelta(weeks=fecha) + timedelta(days=dia-1)  # ojo es 6 ver problema Y correjir error

				H = int(19 + (abs(segundos) / (60 * 60)))
				M = int((segundos / 60) - (H * 60))
				S = int(segundos - (H * 60 * 60) - (M * 60))

			else:
				fecha = date(1980, 1, 6) + timedelta(weeks=fecha) + timedelta(days=dia) #ojo es 6 ver problema Y correjir error

				H = int(segundos / (60 * 60))
				M = int((segundos/60)-(H*60))
				S = int(segundos - (H*60*60) - (M*60))


			fecha = fecha.strftime('%m/%d/%Y')

			print(fecha)

			hora = fecha + "   " + str(H) + ":" + str(M) + ":" + str(S)			

			#date2time=datetime(2018,3,21,2,H,M,S)
			#print ((dt - datetime(1969, 12, 31,19,00,00)).total_seconds()*1000-1521615600000)
			#timems=(date2time - datetime(1969, 12, 31,19,00,00)).total_seconds()*1000-1521615600000
			timems=1
			base = (lat, lon, hora, timems)
			print(base)

			cursor.execute(insertar, base)

			#Make sure data is committed to the database
			mateo.commit()
		else:
			print("")

			#cursor.close()
			#mateo.close()

main()
