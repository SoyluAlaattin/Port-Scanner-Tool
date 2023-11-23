import socket

def scan_all_ports(target):
    for port in range(1, 65536):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} açık")
            s.close()
        except KeyboardInterrupt:
            print("Tarama kullanıcı tarafından kesildi.")
            break
        except socket.error:
            pass

def main():
    target = input("Hedef IP adresini girin: ")
    target = socket.gethostbyname(target)
    scan_all_ports(target)

if __name__ == "__main__":
    main()

