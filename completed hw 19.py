import os
import socket
import traceback
import ipaddress


class Entry:
    def __init__(self, ip, domain_name):
        self.ip = ip
        self.domain_name = domain_name


class Db:
    def __init__(self):
        self.db = []


def parse_query(data, database):
    data = data[2:-1:]

    if "ADD" in data:
        print("ADD FOUND")
        try:
            address = data[4::].split(":")[0]
            ip = ipaddress.ip_address(data[4::].split(":")[1])
            print("DNS :", address, "\nIP:",ip)
            database.append(Entry(ip, address))
            print("ALL ADDRESSES")
            for x in database:
                print(x.ip, x.domain_name)
            return "ADDED"
        except:
            print(Exception)
            return "SERVER ERROR"
    else:
        try:
            for x in database:
                if x.domain_name == data:
                    print("RETURNING:", x.ip)
                    return x.ip
        except:
            print(Exception)
            return "SERVER ERROR"
        else:
            return "DNS NOT FOUND"


def main():
    tmp = os.getenv("DNS_LISTEN", "127.0.0.1:8080")
    laddr, _, lport = tmp.partition(":")
    lport = int(lport)
    database = Db()
    database.db.append(Entry(ipaddress.ip_address('64.233.161.102'), 'google.com'))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((laddr, lport))
    print("Server is running!")
    while True:
        data, addr = sock.recvfrom(1024)
        try:
            response = parse_query(str(data), database.db)
        except:
            traceback.print_exc()
            continue
        sock.sendto(bytes(str(response), encoding="utf-8"), addr)
        print("SENT!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass