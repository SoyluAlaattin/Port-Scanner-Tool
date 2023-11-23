import socket
tara = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = input("ip gir: ")
en_dusuk_port = int(input("en dusuk port gir: "))
en_yuksek_port = int(input("en yuksek port gir: "))

for port in range(en_dusuk_port,en_yuksek_port):
    try:
        tara.connect((ip,port))
        print("{}portu açık".format(port))
    except:
        pass
    