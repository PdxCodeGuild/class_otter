import sys
import socket

def servertest(argv):
    host = argv[1]
    port = int(argv[2])

    args = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    for family, socktype, proto, canonname, sockaddr in args:
        s = socket.socket(family, socktype, proto)
        try:
            s.connect(sockaddr)
        except socket.error:
            return False
        else:
            s.close()
            return True


if __name__ == "__main__":
    if servertest(sys.argv):
        print("Server is UP")
    else:
        print("Server is DOWN")