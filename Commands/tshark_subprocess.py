import re
import subprocess

tsharkCall = [r"(enter desantion here)"] + r"-i 5 -c 50".split(" ") #this command captures 50 packets and keeps
#it in the program

#this coammnd take an existing pcap file and make a txt file out of it
#tsharkCall = [r"C:\Program Files\Wireshark\tshark.exe"] + r"-i 4 -V -r (enter desantion here) > (enter desantion here)".split(" ")

#this command writes a new pcap file that capures 50 packets
#tsharkCall = [r"C:\Program Files\Wireshark\tshark.exe"] + r"-i 5 -w (enter desantion here) -c 50".split(" ") #this command captures 50 packets and keeps

#runs the command
tsharkProc = subprocess.Popen(tsharkCall,
                              bufsize=0,
                              shell=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE)

x = tsharkProc.communicate()[0].decode('utf-8', errors='replace') #puts the output into X
rows = [i.strip() for i in re.findall(r"\s+.+\n",x)] #makes X into a list using regex
for i in rows:
    print(i)
print(rows)
#f = open('test.txt',"r",encoding="utf-8")
#print(f.read())
#print(rows)
