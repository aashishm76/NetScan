# Basic Network Scanner in Python
# Aashish Madamanchi

# Library Imports
import socket
import os

print "NetSCAN 1.0 \n"


# Main
def main():
    menu()


# Command Line Menu Entry
def menu():
    print '-' * 25 + "\n       Main Menu \n" + '-' * 25
    print "1. Device Information"
    print "2. Get IP Address of Host"
    print "3. Port Scanner"
    print "4. Ping all devices on network"
    print "5. Exit \n"

    choice = input('Enter command: ')

    if choice == 1:
        deviceInfo()
    if choice == 2:
        nameToIP()
    if choice == 3:
        portChecker()
    if choice == 4:
        currNetwork()
    if choice == 5:
        exit()
    else:
        print " "
        print "Invalid selection. \n"
        menu()

# Helper request user for address entry
def addressgetter():

    addressIP = raw_input('Enter an web address: ')
    return addressIP

# Helper to process device info
def deviceInfoHelper():

    userHostName = socket.gethostname()
    userIP = socket.gethostbyname(userHostName)

    return userIP

# Provides device information
def deviceInfo():
    try:
        userHostName = socket.gethostname()
        userIP = socket.gethostbyname(userHostName)
        print "Host: ", userHostName
        print "Host IP: ", userIP
        print " "
        menu()
    except socket.error:
        print 'Unable to resolve hostname'
        menu()


# Gets IP address given hostname
def nameToIP():

    try:
        host = socket.gethostbyname(addressgetter())
        print "IP Address: " + host
        print " "
        menu()
    except socket.gaierror:
        print "\nEnter valid hostname.\n"
        menu()

# Scans for open ports given a specific address
def portChecker():

    # Get the address we want to check the ports of
    addressIP = socket.gethostbyname(addressgetter())

    # Scan ports 1 to 1024
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            check = sock.connect((addressIP, port))

            if check == 0:
                print "Port:" + port + " Open" + "\n"
                sock.shutdown()
                sock.close()
            else:
                print "Port:" + port + " Closed" + "\n"
                sock.shutdown()
                sock.close()

    except socket.gaierror:
        print 'Hostname entered cannot be resolved'
        menu()

    except socket.error, e:
        print "Socket error. Unable to complete operation."
        menu()

# List of all devices on current network
def currNetwork():

    # Get address of current device to determine what IP Address range to use
    addressIP = deviceInfoHelper()
    print('Your Device IP: ' + addressIP)

    # Splice the IP Address to obtain proper range
    baseIPAddress = addressIP[:11]
    print('Base IP Address is: ' + baseIPAddress)

    # Iterate through possible IP address and ping them
    for i in range (1, 200):
        PingIP = baseIPAddress + str(i)
        os.system('ping ' + PingIP)




if __name__ == '__main__':
    main()
