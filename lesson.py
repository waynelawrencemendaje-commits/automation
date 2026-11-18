# Day 3: First Netmiko connection and command execution
from netmiko import ConnectHandler

router_device = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.10.85',
    'port': 32770,
    'username': 'admin',
    'password': 'eve',
    'secret': 'eve',
}


try:
    print("Connecting to router...")
    net_connect = ConnectHandler(**router_device)


    # Elevate to Privileged EXEC mode (R1#)
    net_connect.enable()


    # 1. Define your commands in a list
    commands_to_run = [
        "show version",
        "show ip interface brief",
        "show running-config"
    ]


    # 2. Loop through the list to execute them one by one
    for cmd in commands_to_run:
        print(f"\n--- Output for: {cmd} ---")
        output = net_connect.send_command(cmd)
        print(output)


    net_connect.disconnect()
    print("\nDisconnected successfully.")
except Exception as e:
    print(f"Connection failed: {e}")

