#!/usr/bin/python3
import sys,time,os
from socket import *

if sys.platform=='linux':
    os.system('clear')
else:
    pass

time.sleep(1)
Nettowākugōsuto = '''

 ██████   █████           █████     █████    ^-^Nettowākugōsuto^-^   █████                                              █████            
░░██████ ░░███           ░░███     ░░███                             ░░███                                              ░░███             
 ░███░███ ░███   ██████  ███████   ███████    ██████  █████ ███ █████ ░███ █████ █████ ████  ███████  █████  █████ ████ ███████    ██████ 
 ░███░░███░███  ███░░███░░░███░   ░░░███░    ███░░███░░███ ░███░░███  ░███░░███ ░░███ ░███  ███░░███ ███░░  ░░███ ░███ ░░░███░    ███░░███
 ░███ ░░██████ ░███████   ░███      ░███    ░███ ░███ ░███ ░███ ░███  ░██████░   ░███ ░███ ░███ ░███░░█████  ░███ ░███   ░███    ░███ ░███
 ░███  ░░█████ ░███░░░    ░███ ███  ░███ ███░███ ░███ ░░███████████   ░███░░███  ░███ ░███ ░███ ░███ ░░░░███ ░███ ░███   ░███ ███░███ ░███
 █████  ░░█████░░██████   ░░█████   ░░█████ ░░██████   ░░████░████    ████ █████ ░░████████░░███████ ██████  ░░████████  ░░█████ ░░██████ 
░░░░░    ░░░░░  ░░░░░░     ░░░░░     ░░░░░   ░░░░░░     ░░░░ ░░░░    ░░░░ ░░░░░   ░░░░░░░░  ░░░░░███░░░░░░    ░░░░░░░░    ░░░░░   ░░░░░░  
                                                                                            ███ ░███                                      
OccupyTheWeb                                                                                ░░██████                                       
                                                                                            ░░░░░░                                        
'''
time.sleep(1)
print(Nettowākugōsuto)

def help ():
    print('Hello Friend!!')
    print('Usage: ./Nwkgōsuto.py [ip target here] [prtocol type] [start port] [end port]')
    print('Example(TCP): ./Nwkgōsuto.py 192.168.1.1 tcp 1 1544')
    print('Example(UDP): ./Nwkgōsuto.py 192.168.1.1 udp 1 1544')
    print('\n[^-^]ネットワークゴースト[^-^]')
    print('Nettowākugōsuto Created By OccupyTheWeb\n')

def scanPort(network,typeprotocol,startPort,endPort):
    print('===============================================')
    print('[*] Starting Nettowākugōsuto scan report for ip ( %s' % network ,' )')
    
    if typeprotocol == 'tcp':
        tcp_scan(network,startPort,endPort)
    elif typeprotocol == 'udp':
        udp_scan(network,startPort,endPort)
    else:
        print(f'[!]Error: {typeprotocol} Not Found try [TCP] or [UDP][!]\n')
        help()
    print('===============================================\n\n')
    print('[+] Nettowākugōsuto Done: IP address %s' % network )
    
def tcp_scan(ip,startPort,endPort):
    try:
        os.remove('OpenPorts.txt')
    except FileNotFoundError:
        f = open('OpenPorts.txt','w')
        f.write('\n')
    
    number = 0
    try:
        for port in range(startPort,endPort + 1):
            s = socket(AF_INET,SOCK_STREAM)
            number = number+1
            s.settimeout(1)
            if s.connect_ex((ip,port)) == 0: 
                server_name = getservbyport(number)
                with open('OpenPorts.txt','a') as f_obj:
                    f_obj.write(f'[+] {ip}:{port}/TCP {server_name} Open\n')
                print(f'[+] {ip}:{port}/TCP {server_name} Open')        
            s.close()
    except Exception:
        pass
    with open('OpenPorts.txt','a') as f_obj:
        f_obj.write(f'[+] {ip}:{port}/TCP {server_name} Open')

def udp_scan(ip,startPort,endPort):
    try:
        os.remove('OpenPorts.txt')
    except FileNotFoundError:
        f = open('OpenPorts.txt','w')
        f.write('\n')

    number = 0
    try:
        for port in range(startPort,endPort + 1):
            u = socket(AF_INET,SOCK_DGRAM)
            number = number+1
            u.settimeout(1)
            if u.connect_ex((ip,port)) == 0:
                server_name = getservbyport(number)
                with open('OpenPorts.txt','a') as f_obj:
                    f_obj.write(f'[+] {ip}:{port}/UDP {server_name} Open\n')
                print(f'[+] {ip}:{port}/UDP {server_name} Open')
            u.close()
    except Exception:
        pass
    
if __name__ == '__main__':
    try:
        if len(sys.argv) !=5 :
            help()
        
        network   = sys.argv[1]
        typeprotocol = str(sys.argv[2])
        startPort = int(sys.argv[3])
        endPort   = int(sys.argv[4])
    except Exception:
        pass
    if len(sys.argv) == 5:
        scanPort(network,typeprotocol,startPort,endPort)

print('Nettowākugōsuto Created By OccupyTheWeb')
