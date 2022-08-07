#!/usr/bin/python3

import socket, sys

print ("===============DNS RESOLVER==============")
host = input("Digite o Host: ") 
while host != "sair":  
    print ("Site digitado:",host, "| IP do Host -->", socket.gethostbyname(host))
    host = input("Digite um novo Host ou sair para terminar a pesquisa ")
else:
    print("Pesquisa Finalizada")
