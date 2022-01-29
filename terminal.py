import subprocess
import platform
import socket
import time
import os

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("SVVT-404 control terminal [Version 1.00]")
while True:
    code = input(">>> ")
    if code == 'ping':
        host = input("Enter the website you want to ping: ")
        number = input("Enter how many times to ping : ")

        def ping(host):
            param '-n' if platform.system().lower() == 'windows' else '-c'

            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))

        if code == 'local':
            print('Your current local IPS is: ' + host_ip)
            print('Your desktop name is: ' + host_name)

        if code == 'date':
            print("The current date is: " + time.strftime("%m/%d/%y"))

            if code == 'list':
                dir_list = os.listdir(path)
                print("Files and Directories in ", path, "": ")
                print(dir_list)
            if code == 'list -a':
                file = input("Enter the direct file path to read: ")
                dir_listdir(dir_list2)
                print(dir_list2)

                if code === 'infected':
                    print("Infected count is 3")
