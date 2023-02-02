import subprocess
import texttable

# Runs the CMD commands and returns them as parameters
def run_command(cmd):
    return subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE).communicate()


# Finds the ip of the host computer and the gateway
def find_ips(data, lookfor):
    place = data.find(lookfor)

    ip = ""
    place += 5
    while not (data[place].isdigit()):
        place += 1

    while data[place] == '.' or data[place].isdigit():
        ip = ip + data[place]
        place += 1
    return ip

# Finds the number of NICs connected to the computer
def find_nics(data, lookfor):
    place = data.find(lookfor)
    while not (data[place].isdigit()):
        place += 1
    return data[place]

# Finds the names of the NICs and returns a list of the names
def find_nic_name(data, nic_num):
    names = []
    name = ""
    place = data.find("Network Card")
    i = 0
    while i != nic_num:
        while data[place: place + 2] != ']:' or data[place + 4].isdigit():
            place += 1
        place += 2
        data2 = data[place:]
        if (data2.find(':') > data2.find('\n')):
            data = data[place:]
            name = data[:data.find('\n') - 2]
            names.append(name)
            place = 0
            name = ""
            i += 1
    return names

# Finds the media state of the NICs and returns a list of the states
def find_state(data, names):
    states = []
    for a in names:
        place = data.find(a)

        smalldata = data[place - 100:place]

        if smalldata.find("Media disconnected") == -1:
            states.append("Connected")
        else:
            states.append("Disconnected")
    return states

# Finds the macs of the NICs and returns a list of the macs
def find_macs(data, names):
    macs = []
    mac = ''
    for index in names:
        place = data.find(index)
        while data[place] != ':':
            place += 1
        place += 2
        while data[place] != '\r':
            mac += data[place]
            place += 1
        macs.append(mac)
        mac = ''
    return macs

# Finds whether DHCP is enabled and returns a list of the results
def find_DHCP(data, macs):
    dhcp_enabled = []
    dhcp = ''
    for index in macs:
        place = data.find(index)
        while data[place] != ':':
            place += 1
        place += 2
        while data[place] != '\r':
            dhcp += data[place]
            place += 1
        dhcp_enabled.append(dhcp)
        dhcp = ''
    return dhcp_enabled

# Creates a table displaying the NICs' information
def create_Nic_table(arr):
    tableObj = texttable.Texttable()
    tableObj.set_cols_align(["m", "m", "m", "m"])
    tableObj.set_cols_dtype(["t", "t", "t", "t"])
    tableObj.add_rows(arr)
    print(tableObj.draw())

# Creates a table displaying the IP information
def create_IP_table2(arr2):
    tableObj = texttable.Texttable()
    tableObj.set_cols_align(["m", "m"])
    tableObj.set_cols_dtype(["t", "t"])
    tableObj.add_rows(arr2)
    print(tableObj.draw())

# Commands into srings: ipconfig /all, hostname, systeminfo
ipconfig = run_command('ipconfig /all')[0]
ipconfig = ipconfig.decode('latin-1')
systeminfo = run_command('systeminfo')[0]
systeminfo = systeminfo.decode('latin-1')
host_name = run_command('hostname')[0]

host_ip = find_ips(ipconfig, "IPv4 Address")
gateway = find_ips(ipconfig, "Default Gateway")
num_nics = find_nics(systeminfo, "Network Card")
names = find_nic_name(systeminfo, int(num_nics))
media_states = find_state(ipconfig, names)
macs = find_macs(ipconfig, names)
dhcps = find_DHCP(ipconfig, macs)

arr = [['Name', 'State', 'Physical Address', 'DHCP Enabled']]
for i in range(int(num_nics)):
    a = [names[i], media_states[i], macs[i], dhcps[i]]
    arr.append(a)
arr2 = [["IPv4 Address", host_ip], ["Gateway", gateway], ["HostName", host_name]]

print("Computer Information: NIC")
create_Nic_table(arr)
print("Computer Information: IP")
create_IP_table2(arr2)
