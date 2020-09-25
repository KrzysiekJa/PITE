import socket


IP = input("Input IP: ")
Ip_range  = input("Range (example: 5-100): ")

port_low  = int(Ip_range.split("-")[0])
port_high = int(Ip_range.split("-")[1])


print("Scan", IP, "from", port_low, "to", port_high)

for port in range(port_low, port_high + 1):
    s   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ret = s.connect_ex((IP, port))
    
    #if ret == 0:
    #   print("Found:", port)
    print("Return:", str(ret))
    s.close()
