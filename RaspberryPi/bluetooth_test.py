from bluetooth import *

server_socket = BluetoothSocket(RFCOMM)

port = 1
server_socket.bind(("", port))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Accepted connection from ", address)

client_socket.send("bluetooth connected!")

while True:
    data = client_socket.recv(1024)
    print(data)
    X, Y, Z = data.split(",")
    print(f"X: {X}, Y: {Y}, Z: {Z}")

client_socket.close()
server_socket.close()
