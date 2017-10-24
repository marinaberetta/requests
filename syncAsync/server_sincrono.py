import socket
import threading
import time

lock = threading.Lock()

class ThreadedServer(object):

    def __init__(self, host, port):
        self.lista = []
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            # print(threading.active_count())
            client, address = self.sock.accept()
            # client.settimeout(1000)

            self.listenToClient(client,address)


    def listenToClient(self, client, address):
        size = 4096
        while True:
            try:
                data = client.recv(size)
                for a in data.split(b'\r\n'):
                    if(b"number=" in a):
                        a = a.decode("utf-8") 
                        a = a.replace("number=","")
                        a = int(a)
                if data:
                    # Set the response to echo back the recieved data 
                    # response = data
                    # response += "\r\nbody: AEHOE"
                    response = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>'+str(a*2).encode()+b'</body></html>\r\n'
                    # response = b'<html><body><h1>OLA PROFESSOR</h1></body></html>\r\n'
                    client.send(response)
                    client.close()
                else:
                    raise error('Client disconnected')
                print("OK")
                time.sleep(1)
                break;
            except ValueError:
                print(ValueError)
                client.close()
                raise
                return False


if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()

