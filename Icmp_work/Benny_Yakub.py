import subprocess
import re
import sys
from texttable import *

# Tshark call to turn the pcap file into a txt file
tsharkCall = [r"C:\Program Files\Wireshark\tshark.exe"] + r"-r icmp.pcapng > icmp.txt -Y icmp".split(" ")

# Runs a cmd command and returns the output
def run_command(tsharkCall):
    return subprocess.Popen(tsharkCall, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE).communicate()


# Inserts all of the required data into a list
def get_data(data):
    updated_data = []
    for i in data:
        num = re.findall(r'\d+', i)[0]
        ip = re.findall(r'\d+\.\d+\.\d+\.\d+', i)[0]
        time = re.findall(r'\d+\.\d+', i)[0]
        ttl = re.findall(r'ttl=(\d+)', i)[0]
        seq = re.findall(r'seq=(.+),', i)[0]
        packet_data = [num, ip, time, ttl, seq]
        updated_data.append(packet_data)
    return updated_data

# Connects all of the ruequest packets to their response packets into a list of lists
def connect_data(updated_data):
    final_data = [["Request IP", "At Time", "TTL", "Reply IP", "At Time", "TTL", "Turn Around"]]
    while len(updated_data) > 0:
        temp_data = [updated_data[0][1], updated_data[0][2], updated_data[0][3]]
        for i in range(len(updated_data)):
            if i != 0 and updated_data[i][4] == updated_data[0][4]:
                break
        temp_data.append(updated_data[i][1])
        temp_data.append(updated_data[i][2])
        temp_data.append(updated_data[i][3])
        turnaround = float(updated_data[i][2]) - float(updated_data[0][2])
        temp_data.append(turnaround)
        final_data.append(temp_data)
        updated_data.pop(i)
        updated_data.pop(0)
    return final_data

# Prints the data in a table using texttable
def print_table(connected_data):
    table_NIC = Texttable()
    table_NIC.set_cols_align(["c", "c", "c", "c", "c", "c", "c"])
    table_NIC.set_cols_valign(["m", "m", "m", "m", "m", "m", "m"])
    table_NIC.add_rows(connected_data)
    print(table_NIC.draw())

run_command(tsharkCall)

# To check whether the file exists or is in the right directory
try:
    with open('icmp.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

data = data.split('\n')
data.pop(len(data)-1)
updated_data = get_data(data)
connected_data = connect_data(updated_data)
print_table(connected_data)

"""
 In order to connect the right request packets to the response packets I compared the sequence
 numbers in the sequence num field.

 The TTL field defines how many routers a specific packet can hop before being thrown away.
 The TTL value can go up to 255, but is usually 64 or 128.
 Only one computer has a TTL of 128 in this recording - 10.100.102.7
 A reason for the different values in the TTL field is that the messages being recieved from 
 10.100.102.7 are from outside of the lan, which means that the packet would have hopped routers
 in order to reach this lan which would change the TTL from its starting value
"""