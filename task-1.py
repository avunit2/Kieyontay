import netmiko
import getpass

connectionInfo = {
    'device_type':'',
    'host':'192.168.1.1',
    'username':'',
    'password':'',
    'secret':''
}

print("*** Device connection script ***")
connectionType = input("Do you want to connect via Telnet (1) or SSH (2)? ")
connectionInfo["username"] = input("Device username: ")
connectionInfo["password"] = getpass.getpass("Device password: ")
connectionInfo["secret"] = getpass.getpass("Secret password: ")
print("+ Configuration complete, connecting to device...")

if connectionType == "1":
    connectionInfo["device_type"] = "cisco_ios"
    session = netmiko.ConnectHandler(**connectionInfo)
    print("+ Connected to device!")
    session.enable()
    runningConfig = session.send_command("show running-config")
    saveConfig = input("Do you want to save the running config? (Y/N)")
    if saveConfig == "Y":
        file = open("running-config.txt", "w+")
        file.write(runningConfig)
        print("+ Configuration saved to file!")
    session.close()

elif connectionType == "2":
    connectionInfo["device_type"] = "cisco_ios_telnet"
    session = netmiko.ConnectHandler(**connectionInfo)
    print("+ Connected to device!")
    session.close()
else:
    print("- Invalid connection type!")
    exit()
