import socket
import sys
import concurrent.futures
from datetime import datetime

# Simple Multithreaded Port Scanner for Network Security Analysis

def scan_port(target_host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 second timeout
        
        # Attempt to connect to the port
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
        
    except socket.error:
        pass

def main():
    # Example target (localhost or safe testing sandbox)
    target = "127.0.0.1" 
    
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)
    
    # Common ports to scan
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 8080, 8443]
    
    # Use ThreadPoolExecutor for faster multi-threaded scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target, port) for port in ports_to_scan]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
