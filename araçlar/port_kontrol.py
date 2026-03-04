import socket

def p(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    s = sock.connect_ex((host, port))
    sock.close()
    return s == 0

if __name__ == "__main__":
    host = input("Host girin (örnek: 127.0.0.1): ")
    port = int(input("Port numarası girin: "))

    if p(host, port):
        print("Port açık")
    else:
        print("Port kapalı")
