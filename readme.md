## Overview

This portscanner is a simple Python network enumeration tool
that checks whether common ports on a target machine are open or closed.
It also attempts **basic service enumeration** by grabbing banners from
open ports.

This project demonstrates the **core principles of port scanning** using
Python's built‑in `socket` library.

------------------------------------------------------------------------

## What is a Port Scanner?

A **port scanner** is a tool used in networking and cybersecurity to
discover open ports on a system.\
Open ports usually indicate that a **service or application is running**
and listening for connections.

Examples: - Port 80 → HTTP (web server) - Port 22 → SSH (remote login) -
Port 443 → HTTPS (secure web traffic)

Security professionals use port scanners for: - Network discovery -
Service enumeration - Security auditing

------------------------------------------------------------------------

## Python Socket Library

This script uses Python's built‑in **socket** module.

The socket library allows programs to: - Create network connections -
Send and receive data - Communicate with other systems over TCP or UDP

### How a connection works in the script

1.  A **socket object** is created.
2.  The scanner attempts a **TCP connection** to a specific port.
3.  If the connection succeeds, the port is **open**.
4.  If it fails, the port is **closed**.

Example from the code:

``` python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

-   `AF_INET` → IPv4 addressing
-   `SOCK_STREAM` → TCP connection

------------------------------------------------------------------------

## Target Configuration

The script scans a specific machine defined in the code.

Example:

``` python
target_ip = "127.0.0.1"
```

This means the scanner targets:

**127.0.0.1 (localhost)** --- the same machine running the scanner.

You can change it to another IP:

``` python
target_ip = "192.168.1.10"
```

------------------------------------------------------------------------

## Port Dictionary

The scanner includes a **built‑in dictionary of common ports and
services**.

Example:

``` python
PORT_NAMES = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}
```

This allows the scanner to label discovered ports with their **expected
services**.

------------------------------------------------------------------------

## Banner Grabbing (Service Enumeration)

If a port is open, the scanner attempts **banner grabbing**.

Banner grabbing works by: 1. Sending a small request to the service. 2.
Reading the response returned by the server. 3. Extracting service
information.

Example:

``` python
sock.send(b"\r\n")
banner = sock.recv(1024).decode()
```

If a banner is received, it may reveal: - Server software - Service
version - Configuration details

If no banner is returned, the script falls back to the **port
dictionary**.

------------------------------------------------------------------------

## How the Script Works (Step by Step)

1.  Print the **Demeji watermark banner**
2.  Define a list of **common ports**
3.  Create a **TCP socket**
4.  Attempt connection to each port
5.  Identify open ports
6.  Attempt **service enumeration**
7.  Store results
8.  Save scan results to a **TXT file**

------------------------------------------------------------------------

## Output Format

The results are stored in:

    scan_results.txt

Format:

    IP | Port | Service | Banner
    127.0.0.1 | 80 | HTTP | Apache/2.4.52

------------------------------------------------------------------------

## Running the Scanner

Run the script with:

``` bash
python scanner.py
```

The scanner will: - Check common ports - Attempt banner grabbing - Print
results to the terminal - Save results to a file

------------------------------------------------------------------------

## Educational Purpose

This tool is intended for **learning networking and cybersecurity
concepts**, including:

-   TCP connections
-   Port scanning basics
-   Service enumeration
-   Python socket programming

Only scan **systems you own or have permission to test**.
