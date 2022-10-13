import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def validateIp(ip):
    if(re.search(regex,ip)):
        print(ip + " is valid!")
    else:
        print(ip + " is invalid!")

ipToCheck = input("Input an IP address to check: ")
validateIp(ipToCheck)
