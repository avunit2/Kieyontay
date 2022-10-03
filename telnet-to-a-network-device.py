import pexpect

#define variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

#create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

#check for errors and if there are any, display them
if result !=0:
    print('---FAILURE! creating sesion for: ', ip_address)
    exit()

#send user credentials to the device and check for any errors and display any in terminal
#session is expecting username, enter details
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

#check for error and display if any exist
if result !=0:
    print('---FAILURE! entering username: ', username)
    exit()

#session is expecting password, enter details
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])

#check for error
if result !=0:
    print('--- FAILURE! entering password: ', password)
    exit()

#display success message
print('---------------------------')
print('')
print('---Success! connecting to: ', ip_address)
print('--- Username: ', username)
print('--- Password: ', password)
print('')
print('---------------------------')

#terminate telnet session
session.sendline('quit')
session.close()