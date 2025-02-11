import socket


def is_port_open(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    try:
        sock.connect((ip, port))
        sock.close()
        return True
    
    except:
        return False


def find_ssh_open_hosts(subnet):
    open_hosts = []
    port = 22
    
    for i in range(1, 254):
        ip = f"{subnet}.{i}"
        if is_port_open(ip, port):
            print(f"IP address with SSH port: {ip}")
            open_hosts.append(ip)

    return open_hosts


if __name__ == "__main__":
    subnet = "192.168.158"  
    print(f"Scannig network {subnet}.0/24...")
    open_hosts = find_ssh_open_hosts(subnet)

    if open_hosts:
        print("IP addresses with SSH port:")
        for host in open_hosts:
            print(host)
    else:
        print("No IP address with SSH port found")
