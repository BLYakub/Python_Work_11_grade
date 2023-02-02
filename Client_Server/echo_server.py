import socket
import _thread
import datetime
import time
import random

# Creating a temporary socket to find an open port
socket_temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp.bind(("",0))
port = socket_temp.getsockname()[1]
socket_temp.close()

quotes = ["“Be yourself; everyone else is already taken.”\n ― Oscar"]
quotes.append("“Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.”\n ― Albert Einstein")
quotes.append("“A room without books is like a body without a soul.”\n ― Marcus Tullius Cicero")

# Sends a continuous broadcast saying the open server port and the server's host name
def broadcast():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    server.settimeout(0.2)
    host = socket.gethostname()
    message = f'{port} {host}'
    while True:
        print("running")
        server.sendto(message.encode(), ('<broadcast>', 55554))
        print("message sent!")
        time.sleep(1)

_thread.start_new_thread(broadcast,())

# Runs the connection between the server and the client
# Either runs the specific commands or just sends back a echo
def handle(client_socket, address):
    global clients, has_psw
    first_message = False

    # Checks whether the client that connected is the first client
    # If it is the first client then the server sends the password to the client
    if clients[len(clients)-1][1] == address and clients[len(clients)-1][2] == True:
        message = f"Welcome! You are the admin.\nPassword: {password}\nEnter your commands:"
    else:
        message = f"Welcome!\nEnter your commands:"

    client_socket.send(message.encode())

    # Here the server runs the commands 
    while True:
        try:
            data = client_socket.recv(1024).decode()
        except:
            break

        # When the client quits and gives the correct password, 
        # the server disconnects from both the clients and restarts the clients list
        if data.lower() == 'quit':
            answer = quit(client_socket)
            if answer: 
                clients = []
                has_psw = False
                break
            else: client_socket.send("Incorrect Password".encode())
        
        # Disconnects an individual client
        elif data.lower() == "exit":
            exit(client_socket)
        
        # Gives the current date and time
        elif data.lower() == "time":
            get_time(client_socket)

        # Sends a quote of the day
        elif data.lower() == "quote":
            get_quote(client_socket)
        
        # Flips a coin and sends the outcome
        elif data.lower() == "flip coin":
            flip_coin(client_socket)
        
        # If the client exits from the client side using the exit button 
        # instead of sending an exit command, it will still run the exit command
        elif data == "exited":
            exit(client_socket)
        
        # Sends an echo back to the client
        else: 
            message = f"{data}"
            client_socket.send(message.encode())

# Checks whether the password given from the client is correct
# If it is correct the server closes all connections. If not it sends false
def quit(client_socket):
    client_socket.send("Enter password:".encode())
    answer = client_socket.recv(1054).decode()
    if answer == password:
        for client in clients:
            client[0].send("Connection Closed...".encode())
            client[0].close()
        return True
    return False

# Exits an individual client. If the client that exited was the admin, then the server
# finds the next client and sends the password to him. If there are no more clients
# the server sets the has_psw to False, which lets the next person to connect become the admin
def exit(client_socket):
    global has_psw
    has_true = False
    for i in range(len(clients)):
        if clients[i][0] == client_socket: 
            if clients[i][2] == True: has_true = True
            clients.pop(i)
            break
    client_socket.send("Connection Closed...".encode())
    client_socket.close()
    if clients == []: has_psw = False
    elif has_true:
        clients[0][2] = True
        clients[0][0].send(f"You are the admin!\nPassword: {password}".encode())

# Gets and sends the current time to the client
def get_time(client_socket):
    x = datetime.datetime.now()
    print(x)
    client_socket.send(x.strftime("%c").encode())

# Connects to a QOTD server to get the quote and sends it to the client
def get_quote(client_socket):
    # quote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # quote_socket.connect(('djxmmx.net',17))
    # quote = quote_socket.recv(1024).decode()
    # quote = quote.replace("\r", "")
    # quote = quote[:-1]
    # quote_socket.close()
    random.shuffle(quotes)
    client_socket.send(quotes[0].encode())

# Flips a coin and sends the result to the client
def flip_coin(client_socket):
    coin = ('heads', 'tails')
    client_socket.send(random.choice(coin).encode())


conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
password = "42istheanswer"
has_psw = False
clients = []
host = socket.gethostname()
add = (host, port)

conn_socket.bind(add)
conn_socket.listen(2)

# The server waits for a connection from a client. When a client connects, the server checks
# if one of the existing clients are already admin, 
# and assings its role accordingly (admin or not admin)
while True:
    print("waiting for connection")
    data_socket,address = conn_socket.accept()
    if not has_psw: 
        has_psw = True
        clients.append([data_socket, address, True])
    else: clients.append([data_socket, address, False])
    print(clients)
    print(f"conn made with {address}")
    _thread.start_new_thread(handle,(data_socket, address))

