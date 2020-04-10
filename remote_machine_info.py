#!/usr/bin/python3
import socket
'''
this program can be used for the purpose of getting the 
informaiton regarding the remote host and remote host IP
'''
def remote_host_info():
    remote_host = 'www.python.org'
    try:
        print('IP address of %s: %s' %(remote_host,socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print('%s: %s' %(remote_host,err_msg))
if __name__=='__main__':
    remote_host_info()
