import pyfiglet  # type: ignore
import datetime
import getpass
import sys
import socket
from colorama import Fore, Style

def banner(text):
    port_banner = pyfiglet.figlet_format(text, font="slant")
    print(Fore.BLUE + port_banner + Style.RESET_ALL)
    print('----------------------------------------------------------------')
    print("The Port Scanner started at:", datetime.datetime.now().time().replace(microsecond=0))
    print("Your Username:", getpass.getuser(), "on the system:", sys.platform)
    print('----------------------------------------------------------------')

banner("Port Scanner")

def scanning(): 
    host = input("Enter the host you want to scan: ")
    start_port = int(input("Enter the START of the port range: "))
    end_port = int(input("Enter the END of the port range: "))

    if end_port < start_port:
        print(Fore.RED + " [-] End port cannot be smaller than start port" + Style.RESET_ALL)

    try:
        host_ip = socket.gethostbyname(host)
        print("IP address of the Host is", host_ip)
        print(f"\nScanning ports {start_port} to {end_port}...\n")

        for port in range(start_port, end_port + 1): 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  
            result = sock.connect_ex((host_ip, port))
            if result == 0:
                print(Fore.GREEN + f"[~] Port {port} is OPEN" + Style.RESET_ALL)
            sock.close()

    except socket.gaierror:
        print(Fore.RED + "[-] Hostname could not be resolved." + Style.RESET_ALL)
    except socket.error:
        print(Fore.RED + "[-] Couldn't connect to server." + Style.RESET_ALL) 
    except Exception as err: 
        print(Fore.RED + "[-] Error:", str(err) + Style.RESET_ALL)

scanning()
print('\n')
print("The scan got over at:", datetime.datetime.now().time().replace(microsecond=0))
print('Returning to Command Line')
