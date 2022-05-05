#!/usr/bin/python3
import socket

#Ferramentas para scan. Script em desenvolvimento
#Autor: Cleiton Souza
#Data: Abril/2022
#=================================================

#Classe para facilitar o uso de cores no script
class colors: 
    RED ='\033[31;1m' 
    GREEN ='\033[32;1m' 
    BLUE ='\033[34;1m' 
    YELLOW ='\033[33;1m'
    CYAN = '\033[1;36m'
    END ='\033[m'

print(colors.YELLOW +"==========================================="+colors.END)
print(colors.YELLOW +"||         Script para Scan              ||"+colors.END)
print(colors.YELLOW +"==========================================="+colors.END)

def menu():
    escolha = int(input(colors.YELLOW +'''
            Bem-Vindo !
    Qual script deseja executar ?

    1 - DNS Resolver
    2 - Banner Grabbing
    3 - PortScan
    Escolha: ''' + colors.END))
    while escolha != 0:
        if escolha == 1:
        #Script - DNS RESOLVER

            print ("=============== DNS RESOLVER ==============")
            resp = 1
            while resp == 1:
                host = input("Digite o Host: ") 
                print ("Site digitado:",host, "| IP do Host -->" + colors.RED , socket.gethostbyname(host) + colors.END)
                resp=int(input("Deseja fazer uma nova pesquisa ? \n1 - Nova Pesquisa \n2 - Sair: \nDigite a opção desejada: "))
            else: 
                print("Fim do programa")
                exit()        
        elif escolha == 2:
        #Script - BannerGrabbing    
            print("=============== BANNER GRABBING ===========")
            ip = input("Digite o IP: ")
            porta = str(input("Digite a porta: "))

            conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexao.connect_ex((ip,int(porta)))
            banner = conexao.recv(1024)
            print (banner)
            conexao.close()
            exit()
        elif escolha == 3:
        #Script PortScan    
            print("=============== PORTSCAN ====================")
        def scan():

            alvo = input("Digite o IP ou Domínio do Alvo: ")
            portaI = int(input("Digite a porta Inicial: "))
            portaF = int(input("Digite a porta Final: "))

            print ("Scan em andamento...")
            for porta in range(portaI, portaF):
                conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5) #Para agilizar o scan das portas
                if conexao.connect_ex((alvo, porta)) == 0:
                    print ("Porta",porta,"[ABERTA]") 
                    conexao.close()
                                    
        scan()
        exit()
menu()