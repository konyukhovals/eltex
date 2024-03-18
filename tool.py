from netmiko import ConnectHandler
from env import *
import time

with open('config_list') as f:
    config_lines = f.read().splitlines()
print(config_lines)

with open('devices_list') as f:
    ip_lines = f.read().splitlines()
print(ip_lines)

for device in ip_lines:
    ip_address_of_device = device
    joint = {
        'device_type': 'eltex',
        'ip': ip_address_of_device,
        'username': login,
        'password': password
    }

    ssh_connect = ConnectHandler(**joint)

    start_time = time.time()
    output = ssh_connect.send_config_set(config_lines)
    end_time = time.time()

    output = ssh_connect.send_command_timing(
        command_string=command_write,
        strip_prompt=False,
        strip_command=False
    )

    output = ssh_connect.send_command_timing(
        command_string=command_YES,
        strip_prompt=False,
        strip_command=False
    )

    print(f"\n\n_________REPORT________joint_{joint['ip']}________REPORT________")
    print(output)
    print("_________REPORT______________END________________REPORT________")
    ssh_connect.disconnect()

print()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)

