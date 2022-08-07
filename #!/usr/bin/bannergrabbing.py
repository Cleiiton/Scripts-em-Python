#!/usr/bin/python3

#Banner Grabbing
#Autor: Cleiton Souza

import socket

ip = input("Digite o IP: ")
porta = str(input("Digite a porta: "))

conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexao.connect_ex((ip,int(porta)))
banner = conexao.recv(1024)
print (banner)
conexao.close()
