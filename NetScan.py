# Basic Network Scanner in Python
# Aashish Madamanchi

# Library Imports
import socket
import sys

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
    print "3. Exit \n"

    choice = input('Enter command: ')

    if choice == 1:
        deviceInfo()
    if choice == 2:
        nameToIP()
    if choice == 3:
        portChecker()
    if choice == 4:
        exit()
    else:
        print " "
        print "Invalid selection. \n"
        menu()


# Provides device information
def deviceInfo():
    try:
        userHostName = socket.gethostname()
        userIP = socket.gethostbyname(userHostName)
        print "Host: ", userHostName
        print "Host IP: ", userIP
        print " "
        menu()
    except:
        print 'Unable to resolve hostname'
        menu()


# Gets IP address given hostname
def nameToIP():
    addressQuery = raw_input('Enter a web address: ')

    try:
        host = socket.gethostbyname(addressQuery)
        print "IP Address: " + host
        print " "
        menu()
    except socket.gaierror:
        print "\nEnter valid hostname.\n"
        menu()

def portChecker():

    # Get the address we want to check the ports of
    addressQuery = raw_input('Enter a web address: ')
    addressIP = socket.gethostbyname(addressQuery)

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

if __name__ == '__main__':
    main()
