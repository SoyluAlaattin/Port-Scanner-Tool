
import socket
import threading
from queue import Queue

# Thread queue
thread_queue = Queue()

def threader():
    while True:
        worker = thread_queue.get()
        scan_port(worker)
        thread_queue.task_done()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} açık")
        s.close()
    except socket.error:
        pass

def scan_all_ports(target):
    for x in range(100):  # Number of threads
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for port in range(1, 65536):
        thread_queue.put(port)

    thread_queue.join()

def main():
    global target
    target = input("Hedef IP adresini girin: ")
    target = socket.gethostbyname(target)
    scan_all_ports(target)

if __name__ == "__main__":
    main()
