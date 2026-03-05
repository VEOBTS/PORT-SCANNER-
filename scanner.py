import socket

# CHANGE 1: Added watermark/banner function
def print_banner():
    print("===================================")
    print("        DEMEJI PORT SCANNER        ")
    print("===================================")

# CHANGE 2: Expanded common port dictionary
PORT_NAMES ={
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MYSQL",
    3389: "RDP",
    8080: "HTTP-PROXY"
}

# CHANGE 3: Service enumeration (banner grabbing)
def enumerate_service(sock, port):
    try:
        sock.send(b"\r\n")
        banner = sock.recv(1024).decode().strip()
        if banner:
            return banner
    except:
        pass
    
    # fallback to dictionary if banner grabbing fails
    return PORT_NAMES.get(port, "Unknown")

# CHANGE 4: Save results to txt
def save_results_txt(results):
    with open("scan_results.txt", "w") as f:
        f.write("IP | Port | Service | Banner\n")
        f.write("----------------------------------\n")
        for r in results:
            f.write(f"{r}\n")

# CHANGE 5: Banner prints when script starts
print_banner()

target_ip = "127.0.0.1"
results = []

for port in PORT_NAMES:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM for TCP , AF_INET for IPv4
    sock.settimeout(0.5)

    status = sock.connect_ex((target_ip, port))  # connect_ex returns 0 if connection is successful

    if status == 0:
        banner = enumerate_service(sock, port)
        service = PORT_NAMES.get(port, "Unknown")

        output = f"{target_ip} | {port} | {service} | {banner}"
        print(f"Port {port} ({service}) is open")
        results.append(output)

    else:
        print(f"Port {port} ({PORT_NAMES[port]}) is closed")

    sock.close()

# CHANGE 6: Save results after scan finishes
save_results_txt(results)