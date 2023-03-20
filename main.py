import socket
import ipaddress
from termcolor import colored

print("| | | |         | |  |  ___|        | |")
print("| |_| | __ _ ___| |_ | |____  _____| |")
print("|  _  |/ _` / __| __ |  __\ \/ / _ \ |")
print("| | | | (_| \__ \ |_ | |___>  <  __/_|")
print("\_| |_/\__,_|___/\__ \____/_/\_\___(_)")

print("")
print("_" * 30)
print("")

while True:
    try:
        target_host = input("> Enter the target IP: ")
        ipaddress.IPv4Address(target_host)
        break
    except ValueError:
        print(colored("Invalid IP address. Please try again.", "red"))

start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print("")
print("_" * 30)
print("")


for port in range(start_port, end_port+1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(colored(f"[+] Port {port} is open", "green"))
        sock.close()
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except socket.error:
        print("_" * 30)
        print(colored(f"Could not connect to port {port}", "red"))
