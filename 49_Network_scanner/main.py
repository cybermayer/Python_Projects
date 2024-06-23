#region IMPORT

import argparse
from typing import List, Dict
import scapy.all as scapy

#endregion

def get_arguments() -> argparse.Namespace:
    
    """<DOC
    
            Parses command-line arguments and returns target IP or IP range.
        
                RETURNS: argparse.Namespace: Object containing parsed arguments.
        
    DOC?>"""
    
    #region CODE

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Specify target IP or IP range")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify target IP or IP range.")

    return options

    #endregion

def scan(ip: str) -> List[Dict[str, str]]:
    
    """<DOC
    
            Returns a list of dictionaries containing IP and MAC address pairs of clients on the network.
        
                PARAMETERS:
                            -ip (str): Target IP address or IP range to scan.
            
                RETURNS: List[Dict[str, str]]: List of dictionaries with 'ip' and 'mac' keys representing IP and MAC address pairs.
        
    DOC?>"""
    
    #region CODE

    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet / arp_packet
    answered_list = scapy.srp(arp_broadcast_packet,
                              timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

    #endregion

def print_result(scan_list: List[Dict[str, str]]) -> None:
    
    """<DOC
    
        Prints IP and MAC address pairs of clients on the network.
    
            PARAMETERS: 
                        -scan_list (List[Dict[str, str]]): List of dictionaries containing 'ip' and 'mac' keys representing IP and MAC address pairs.  
            
    DOC?>"""
    
    #region CODE

    print("IP\t\t\tMAC\n----------------------------------------")
    for client in scan_list:
        print(f"{client['ip']}\t\t{client['mac']}")

    #endregion

#region MAIN

if __name__ == '__main__':
    options = get_arguments()
    result_list = scan(options.target)
    print_result(result_list)

#endregion
