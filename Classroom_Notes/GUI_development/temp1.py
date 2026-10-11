import socket

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for char in alphabet:
        if char not in s:
            return False
    return True

# Set up server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Server is listening on port 9999...")

conn, addr = server.accept()
print(f"Connected to client at {addr}")

# Receive string from client
data = conn.recv(1024).decode()
print(f"Received from client: '{data}'")

# Check if it is a pangram
if is_pangram(data):
    response = "Success: The string is a valid pangram!"
else:
    response = "Failed: The string is NOT a pangram."

# Send response back to client
conn.send(response.encode())
conn.close()
server.close()


