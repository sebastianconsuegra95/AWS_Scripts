from datetime import datetime, date, time, timedelta
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
            segundo = int(float(data[11:16]) - (5 * 60 * 60))  # GMZ -5
            dias = int(float(data[10:11]))
            fecha = int(float(data[6:10]))

            if segundo<0:
                segundo = segundo + (5 * 60 * 60)  # GMZ
                fecha = date(1980, 1, 6) + timedelta(weeks=fecha) + timedelta(days=dias-1)  # ojo es 6 ver problema Y correjir error
                H = int(19 + (abs(segundo) / (60 * 60)))
                H2 = int(segundo / (60 * 60))
                M = int((segundo / 60) - (H2 * 60))
                S = int(segundo - (H2 * 60 * 60) - (M * 60))       

            else:
                fecha = date(1980, 1, 6) + timedelta(weeks=fecha) + timedelta(days=dias) #ojo es 6 ver problema Y correjir error
                H = int(segundo / (60 * 60))
                M = int((segundo / 60)-(H*60))
                S = int(segundo - (H*60*60) - (M*60))


            S = str(S)
            M = str(M)
            H = str(H)
            
            if len(M) == 1:
                M="0"+M
            if len(S) == 1:
                S="0"+S
                

            #fecha = fecha.strftime('%m/%d/%Y')
            Month = fecha.strftime('%m')
            Day   = fecha.strftime('%d')
            Year  = fecha.strftime('%Y')

            dias = str(dias)

            date2time=datetime(Year,Month,Day,H,M,S)
            print(date2time)
            #date2time=datetime(2018,3,21,2,H,M,S)
			#print ((dt - datetime(1969, 12, 31,19,00,00)).total_seconds()*1000-1521615600000)
            timems=(date2time - datetime(1969, 12, 31,19,00,00)).total_seconds()*1000
            base = (lat, lon, hora, timems)

            cursor.execute(insertar, base)

            # Make sure data is committed to the database
            mateo.commit()
        else:
            print("")

            #cursor.close()
            #mateo.close()

main()
