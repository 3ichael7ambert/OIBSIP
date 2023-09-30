import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))

    while True:
        message = input("Enter your message: ")
        client.send(message.encode('utf-8'))
        response = client.recv(1024)
        print(f"Server response: {response.decode('utf-8')}")

if __name__ == "__main__":
    main()
