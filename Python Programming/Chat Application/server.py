import socket
import threading

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        if not request:
            break
        print(f"Received: {request.decode('utf-8')}")
        client_socket.send("Message received.".encode('utf-8'))
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen(5)
    print("Server listening on port 8080")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
