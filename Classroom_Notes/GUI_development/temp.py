import socket

# Pangram to send
pangram_string = "The quick brown fox jumps over the lazy dog"

# Set up client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

print(f"Sending string: '{pangram_string}'")
client.send(pangram_string.encode())

# Receive response from server
response = client.recv(1024).decode()
print(f"Server response: {response}")

client.close()