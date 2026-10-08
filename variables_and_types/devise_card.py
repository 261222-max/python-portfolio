#device_card.py
#this program stores and prints a network device record.

MAX_CONNECTIONS=100

device_name= "web-server-01"
device_ip ="192.0.2.20"
service = "HTTPS"
open_port = 443

print("Device:",device_name)
print("ip address:",device_ip)
print("service:",service)
print("port:",open_port)
print("Max connections:",MAX_CONNECTIONS)

service= "SSH"
open_port = 22

print("Updated service:",service,"on port",open_port)
