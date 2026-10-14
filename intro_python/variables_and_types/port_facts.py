#port_facts.py
#برنامج يحسب عدد المنافذ وعدد عناوين  ورقم اخر منفذ ipv4
PORT_BITS=16
IPV4_BITS=32
total_port=2**(PORT_BITS)
total_ipv4=2**(IPV4_BITS)
highest_port=total_port-1
print(f"total port = {total_port}\nTotal ipv4={total_ipv4}\nHighest port={highest_port}")
