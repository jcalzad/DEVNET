import paramiko
from io import StringIO
import time
from tabulate import tabulate
import argparse

# Setup argparse to accept IP address, username, and password
#parser = argparse.ArgumentParser(description="SSH into a router and execute a command.")
#parser.add_argument("ip", help="IP address of the router")
#parser.add_argument("username", help="Username for the router")
#parser.add_argument("password", help="Password for the router")
#
#args = parser.parse_args()
#
#router_ip = args.ip
#username = args.username
#password = args.password

router_ip = "<ip_addr>"
username = "<username>"
password = "<password>"


command = "show ip interface brief vrf all | no-more"

# Create a new SSH client
ssh = paramiko.SSHClient()

# Automatically add untrusted hosts (make sure okay for security policy in your environment)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the router using the provided credentials
    ssh.connect(router_ip, username=username, password=password, look_for_keys=False)
    print("Logging in!")
    # Use invoke_shell to simulate the interactive login session
    shell = ssh.invoke_shell()

    # Send the 'enable' command (assuming it's required; otherwise, remove it)
    # shell.send('enable\n')
    # shell.send(password + '\n')  # Sending password for the 'enable' command
    shell.send(command + '\n')
    print("Sending command!")
    shell.send('exit\n')  # Exit the session

    # Wait for the command to complete
    while not shell.recv_ready():
        time.sleep(20)

    # Read the output from the command
    output = shell.recv(9999).decode('utf-8')

    # print("Output from the command:")
    # print(output)

    # Close the SSH connection
    ssh.close()

except paramiko.SSHException as e:
    print("Connection Failed: {}".format(e))

output_buffer = StringIO(output)
output_lines = output_buffer.readlines()
# print(output_buffer)
# print(output_lines)

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

interfaces = []
for line in output_lines:
    #print(line)
    if str("protocol-up") in line:
        #print(line)
        parts = line.split()
        interface = parts[0]
        ip_address = parts[1]
        status = parts[2]
        #protocol = parts[-1]
        #print("Interface {} with IP {} is Up".format(interface, ip_address))
        #if status == "*up*up*up":
        #print("Interface {} with IP {} is Up".format(interface, ip_address))

        # Highlight the status based on its value
        if "protocol-up/link-up/admin-up" in line:
            status_colored = f"{GREEN}{status}{ENDC}"
        else:
            status_colored = f"{RED}{status}{ENDC}"
        
        interfaces.append([interface, ip_address, status_colored])

# Print the table
headers = ["Interface", "IP Address", "Status"]
print(tabulate(interfaces, headers=headers, tablefmt="grid"))

output_buffer.close()
print("Finished processing")
