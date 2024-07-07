from scapy.all import Ether, IP, TCP, UDP

def analyzer(packet, packet_list):
    if packet.haslayer(Ether):
        eth = packet[Ether]
        dest_mac = eth.dst
        src_mac = eth.src
        
        if packet.haslayer(IP):
            ip = packet[IP]
            dest_ip = ip.dst
            src_ip = ip.src
            proto = ""
            src_port = ""
            dest_port = ""
            
            if packet.haslayer(TCP):
                tcp = packet[TCP]
                src_port = tcp.sport
                dest_port = tcp.dport
                proto = "TCP"
                
            elif packet.haslayer(UDP):
                udp = packet[UDP]
                src_port = udp.sport
                dest_port = udp.dport
                proto = "UDP"
            
            packet_info = [src_mac, dest_mac, src_ip, dest_ip, proto, src_port, dest_port]
            packet_list.append(packet_info)
