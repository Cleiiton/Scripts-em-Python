#!/usr/bin/python3
 
#PORTSCAN
#Autor: Cleiton Souza

import socket

alvo = input("Digite o IP ou Domínio do Alvo: ")
portaI = int(input("Digite a porta Inicial: "))
portaF = int(input("Digite a porta Final: "))

print ("Scan em andamento...")
for porta in range(portaI, portaF):
	conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(0.5)
	if conexao.connect_ex((alvo, porta)) == 0:
		print ("Porta",porta,"[ABERTA]") 
		conexao.close()
