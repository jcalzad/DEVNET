import paramiko
from io import StringIO
import time

# Need to work on how to hide credentials or call to another file or vault
# router_ip = "<router_ip>"
# username = "<username>"
# password = "<password>"


# Command to run once you logged in
command = "show module"

# Create new SSH client
ssh = paramiko.SSHClient()

# Automatically add untrusted hosts (make sure okay for security policy in your environment)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the router using the provided credentials
    ssh.connect(router_ip, username=username, password=password, look_for_keys=False)
    # Using frequent print commands to test how far I can get
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
        time.sleep(30)

    # Read the output from the command
    output = shell.recv(99999).decode('utf-8')

    # print("Output from the command:")
    print(output)

    # Close the SSH connection
    ssh.close()

except paramiko.SSHException as e:
    print("Connection Failed: {}".format(e))

output_buffer = StringIO(output)
output_lines = output_buffer.readlines()
print(output_buffer)
# print(output_lines)

for line in output_lines:
    print(line)

output_buffer.close()
print("Finished processing")