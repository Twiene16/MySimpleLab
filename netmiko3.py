from netmiko import ConnectHandler
rt1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.16.2",
    "username": "admin",
    "password": "cisco",   
}
rt2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.16.3",
    "username": "admin",
    "password": "cisco",   
}
rt3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.16.4",
    "username": "admin",
    "password": "cisco",   
}
net_connect = ConnectHandler(**rt1)
config_command = ['int loopback20' , 'ip address 192.168.20.2 255.255.255.0']
for n in range (2,5):
    print ("#######################Router 1 VLAN Configuration###############")
    print ("creating VLAN" + str (n))
    config_commands = ['vlan' + str(n), 'name Admin_VLAN' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output)

output = net_connect.send_command('show ip int brief')
print ( "Interfaces status for Router 1 \n" + output)

net_connect = ConnectHandler(**rt2)
output = net_connect.send_command('show ip int brief')
print ( "Interfaces status for Router 2 \n" + output)

net_connect = ConnectHandler(**rt3)
output = net_connect.send_command('show ip int brief')
print ( "Interfaces status for Router 3 \n" + output)

net_connect = ConnectHandler(**rt1)
output = net_connect.send_command('show version')
print ("#################################################")
print ( "Software version router 1 \n" + output)
