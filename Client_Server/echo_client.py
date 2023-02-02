import socket
import threading
from tkinter import *
import _thread
import sys

# Creates a udp socket connection with the server to get the server's port and host name
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 55554))
data, addr = client.recvfrom(1024)
client.close()
data = data.decode()
data = data.split(" ")

current_timer = 10.0
is_active = False
has_ran = True
cant_send = False
sent_data = False
has_exited = False

# Prints 'Wake Up!' and adds 1 minute to the timer
def wake_up():
    global current_timer, has_ran
    listbox.insert(END, "Wake Up!")
    current_timer += 60.0
    has_ran = True
    
# Creates a thread timer that runs the wake_up function when the inactive timer is up
# If the client is active, the timer restarts.
def timer():
    global has_ran, is_active
    while True:
        if has_ran:
            has_ran = False
            start_timer = threading.Timer(current_timer, wake_up)
            start_timer.start()
        while not has_ran:
            if is_active:
                start_timer.cancel()
                is_active = False
                has_ran = True

# Creates a new thread for the timer function to run along with the rest of the code
_thread.start_new_thread(timer, ())

# Creates a root window, text field and scrollbar
root = Tk()
root.configure(background='#5EC9FB')
entry_text = StringVar()
root.geometry("550x300+500+150")
listbox = Listbox(root)
listbox.pack(side=TOP, fill=BOTH, expand= True, padx=10, pady=5)

scrollbar = Scrollbar(listbox, orient="vertical", command= listbox.yview)
scrollbar.pack(side= RIGHT, fill= Y)
listbox['yscrollcommand'] = scrollbar.set
scrollbarx = Scrollbar(listbox, orient="horizontal", command= listbox.xview)
scrollbarx.pack(side= BOTTOM, fill= X)
listbox['xscrollcommand'] = scrollbarx.set

# Connects to the server through tcp and prints the server's message
conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_socket.connect((data[1], int(data[0])))
resp = conn_socket.recv(1024).decode()
resp = resp.split('\n')
print(resp)
for part in resp:
    listbox.insert(END, f" {part}")

# Tries to send the data in the entry field. If it can't send the data then it means 
# that the connection with the server was closed, then it runs the exit function.
def send_data():
    global entry_text, cant_send, is_active, sent_data
    data = entry.get()
    try:
        conn_socket.send(data.encode())
        listbox.insert(END, f">> {data}")
        entry_text.set("")
        is_active = True
        sent_data = True
    except:
        listbox.insert(END, "Connection Closed...")
        cant_send = True
        exit()

# Sends to the server that the client has exited manually instead of sending a command.
# It then closes the connection and stops the code.
def exit():
    try:
        conn_socket.send("exited".encode())
        conn_socket.recv(1024)
    except: pass
    conn_socket.close()
    root.destroy
    sys.exit()

# Creates a entry field, exit button, and send button
entry = Entry(root, width=40, textvariable=entry_text)
entry.pack(side=LEFT, fill=X, expand=True, padx= 5, pady=5)
exit_button = Button(root, text= 'exit', bg='#FF5733', command= exit)
exit_button.pack(side=RIGHT, expand=True, fill=X, padx=5)
button = Button(root, text= 'send', command= send_data)
button.pack(side=RIGHT, expand=True, fill=X, padx=5)

# Runs the connection between the server and the client
def run_connection():
    global sent_data
    while True:
        # Checks if the client sent data before continuing to run the code
        if sent_data:
            sent_data = False

            # Tries to receive data from the server, else it exits
            try: 
                resp = conn_socket.recv(1024).decode()
            except:
                exit()
            if resp == '':
                entry.config(state='disabled')
                button.config(state='disabled')
                exit()
            
            # Prints the server's response
            resp = resp.split('\n')
            listbox.insert(END, f" Server: {resp[0]}")
            resp.pop(0)
            for part in resp:
                listbox.insert(END, f" {part}")
            print(resp)

            # If the server sends 'Connection Closed...' then the client exits
            if "Closed" in resp:
                entry.config(state='disabled')
                button.config(state='disabled')
                exit()
            elif resp == "You are the admin!\nPassword: 42istheanswer":
                resp = conn_socket.recv(1024).decode()
                listbox.insert(END, f" Server: {resp}")

        # If the client can't send data then he exits from the loop
        elif cant_send: break
    
# Creates a thread of the running connection.
_thread.start_new_thread(run_connection, ())

root.mainloop()
