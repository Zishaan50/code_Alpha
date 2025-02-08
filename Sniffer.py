import socket
import struct
import binascii

def analyze_packet(packet):
    # Unpack the Ethernet frame
    eth_header = struct.unpack("!6s6sH", packet[0:14])
    eth_protocol = socket.ntohs(eth_header[2])
    
    # Unpack the IP header
    ip_header = struct.unpack("!BBHHHBBH4s4s", packet[14:34])
    ip_protocol = ip_header[6]
    
    # Unpack the TCP header
    tcp_header_length = (ip_header[0] & 0xF) * 4
    tcp_header = struct.unpack("!HHLLBBHHH", packet[14 + tcp_header_length:14 + tcp_header_length + 20])
    
    # Print the packet details
    print("Ethernet Protocol:", eth_protocol)
    print("IP Protocol:", ip_protocol)
    print("Source IP:", socket.inet_ntoa(ip_header[8]))
    print("Destination IP:", socket.inet_ntoa(ip_header[9]))
    print("Source Port:", tcp_header[0])
    print("Destination Port:", tcp_header[1])
    print("TCP Sequence Number:", tcp_header[2])
    print("TCP Acknowledgment Number:", tcp_header[3])
    print("TCP Header Length:", tcp_header_length)
    print("TCP Flags:", binascii.hexlify(packet[14 + tcp_header_length + 13:14 + tcp_header_length + 14]))
    print("Data:", packet[14 + tcp_header_length + 20:])
    print("-" * 50)

def sniff_packets():
    # Create a raw socket and bind it to the network interface
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    while True:
        # Receive a packet
        packet = sock.recvfrom(65535)[0]
        
        # Analyze the packet
        analyze_packet(packet)

# Start sniffing packets
sniff_packets()