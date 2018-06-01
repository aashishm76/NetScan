# Basic Network Scanner in Python
# Aashish Maadamanchi

# Library Imports
import socket


print "NetSCAN 1.0 \n"

# Main
def main():
    Menu()

# Command Line Menu Entry
def Menu():
    print "---Main Menu---"
    print "1. Device Information"
    print "2. Get IP Address of Host"
    print "3. Exit \n"

    choice = input('Enter command: ')

    if choice == 1:
        deviceInfo()
    if choice == 2:
        nameToIP()
    if choice == 3:
        exit()
    else:
        print " "
        print "Invalid selection. \n"
        Menu()

# Provides device information
def deviceInfo():

    try:
        userHostName = socket.gethostname()
        userIP = socket.gethostbyname(userHostName)
        print "Host: ", userHostName
        print "Host IP: ", userIP
        Menu()
    except:
        print 'Unable to resolve hostname'
        Menu()

# Gets IP address given hostname
def nameToIP():

    addressQuery = raw_input('Enter a web address: ')

    try:
        host = socket.gethostbyname(addressQuery)
        print "IP Address: " + host
        print " "
        Menu()
    except socket.gaierror:
        print "\nEnter valid hostname.\n"
        Menu()

if __name__ == '__main__':
   main()

