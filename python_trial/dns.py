import socket
from threading import Thread

class DNS_Resolver:
    def __init__(self):
        self.ip_address = "11.111.111.11"
        self.port = "8502"
        self.cache = {
	    ".": "199.7.83.42" #root dns server
        }
    
    def do_lookup(self, recv_socket, host):
        # Do a lookup for the ip of the host, 
        # while storing the resolved ip of
        # all intermediate DNS name servers.

        # get vector of host names
        host_vec = host.split('.')
        host_vec.reverse()

        # resolve DNS loopup iteratively
        curr_dns_server = self.cache["."]
        for host_name in host_vec:
            # take cached-in value directly
            if host_name in self.cache.keys():
                curr_dns_server = self.cache[host_name]
            # or lookup with DNS server
            else:
                curr_dns_server = resolve_dns(curr_dns_server, host_name)
                self.cache[host_name] = curr_dns_server
        
        return curr_dns_server


    def send_response(self, socket, host, ip):
        # Send response back to the client on recv_socket
        message = {
            "host": host,
            "resolved_ip": ip
        }
        socket.sendall(message)


    def main(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.ip_address, self.port))
        sock.listen(5)
 
        while True:
            recv_socket, address = sock.accept()
            message_chunks = []
            while True:
                data = recv_socket.recv(4096)
                if not data:
                    break
                message_chunks.append(data)
 
            message_bytes = b''.join(message_chunks)
            message_str = message_bytes.decode("utf-8")
            message_dict = json.loads(message_str)
            #
            # complete the code for main()
            ip_address = self.do_lookup(recv_socket, message_dict["host"])
            self.send_response(recv_socket, message_dict["host"], ip_address)
