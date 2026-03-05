import socket 

PORT_NAMES ={
    20: "FTP",
    443: "HTTPS",
    80: "HTTP",
    22: "SSH",

}
#integrate with external library to scan ports

for port in PORT_NAMES:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM for TCP , AF_INET for IPv4
    sock.settimeout(0.5) #set timeout for connection attempt
    
    status=sock.connect_ex (("127.0.0.1", port)) #connect_ex returns 0 if connection is successful

    if status == 0:
        print(f"Port {port} ({PORT_NAMES[port]}) is open")
    else:
        print(f"Port {port} ({PORT_NAMES[port]}) is closed")
