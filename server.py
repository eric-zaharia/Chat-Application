# server
import socket
import threading

connections = []
total_connections = 0


class Client(threading.Thread):
    def __init__(self, socket, address, id, name):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    def run(self):
        name = self.socket.recv(32)
        self.name = name.decode("utf-8")
        self.name.ljust(32, '0')
        print(str(name.decode("utf-8")) + " connected.")
        while True:
            data = self.socket.recv(32)
            if data:
                print(str(name.decode("utf-8")) + ": " + str(data.decode("utf-8")))
                for client in connections:
                    if client.id != self.id:
                        client.socket.sendall(self.name.ljust(32, '0').encode())
                        client.socket.sendall(data)
            else:
                print(str(name.decode("utf-8")) + " disconnected.")
                self.socket.close()
                connections.remove(self)
                break


def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name: "))
        connections[len(connections) - 1].start()
        total_connections += 1


def main():
    host, port = "localhost", 12366

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    new_connections_thread = threading.Thread(target=newConnections, args=(sock,))
    new_connections_thread.start()


main()
