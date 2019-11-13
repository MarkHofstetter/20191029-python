import socket, threading

def TCP_connect(ip, port_number, timeout, ports):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(timeout)
    try:
        TCPsock.connect((ip, port_number))
        ports[port_number] = True
    except:
        ports[port_number] = False


def scan_ports(host_ip, timeout):
    threads = []
    ports = {}
    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, timeout, ports))
        threads.append(t)
    for i in range(10000):
        threads[i].start()

    # Wartet bis alle threads zuende sind
    for i in range(10000):
        threads[i].join()

    for i in range(10000):
        if ports[i]:
            print("Port [%d] Listening" % (i))

if __name__ == "__main__":
    host_ip = input("Target IP: ")
    timeout = 1
    scan_ports(host_ip, timeout)