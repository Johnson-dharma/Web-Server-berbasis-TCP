import socket
import webbrowser

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

# Fungsi untuk mengirim file HTML
def send_html_file(filename):
    try:
        with open(filename, 'r') as file:
            html_content = file.read()
            send(html_content)
            webbrowser.open_new_tab('file://' + filename)
    except FileNotFoundError:
        print("File not found!")

send_html_file("portofoliocci.html")

x = int(input("1 untuk terus mengirim pesan: "))
while x == 1:
    send(input("Masukan pesan: "))
    x = int(input("1 untuk terus mengirim pesan: "))

send(DISCONNECT_MESSAGE)
