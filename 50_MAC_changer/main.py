#region IMPORT

import subprocess
import re
import argparse

#endregion 

def modify_mac_address(network_interface, new_mac_address) -> None:
    
    """<DOC
    
            Modify the MAC address of the specified network interface.
            
                PARAMS:
                        -network_interface (str): Name of the network interface (e.g. 'eth0', 'wlan0').
                        -new_mac_address (str): New MAC address to assign to the interface.

    DOC?>"""

    #region CODE
    
    print(f'[+] Modifying MAC address for network interface {network_interface} to {new_mac_address}\n')
    
    # Bringing the network interface down
    subprocess.call(['ifconfig', network_interface, 'down'])

    # Changing the MAC address
    subprocess.call(['ifconfig', network_interface, 'hw', 'ether', new_mac_address])

    # Bringing the network interface up
    subprocess.run(['ifconfig', network_interface, 'up'], check=True)

    # Verify the new MAC address (commented out, can be enabled if needed)
    # subprocess.run(['ifconfig', network_interface], check=True)

    #endregion

def retrieve_current_mac(network_interface) -> str:
    
    """<DOC
    
            Retrieve the current MAC address of the specified network interface.
        
                PARAMS:
                        -network_interface (str): Name of the network interface (e.g., 'eth0', 'wlan0').
        
                RETURNS: str: Current MAC address of the network interface, or None if not found.
                
    DOC?>"""

    #region CODE
    
    try:
        ifconfig_output = subprocess.check_output(["ifconfig", network_interface])
        mac_address_search = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", ifconfig_output.decode())
        if mac_address_search:
            return mac_address_search.group(0)
        else:
            print('[-] MAC address could not be found.')
            return None
            
    except subprocess.CalledProcessError:
        print(f'[-] Could not execute ifconfig for interface {network_interface}')
        return None

    #endregion

def get_arguments():
    
    """<DOC
    
            Parse and return command-line arguments.
        
                RETURNS: Namespace: Contains parsed command-line arguments.

    DOC?>"""

    #region CODE
    
    parser = argparse.ArgumentParser(description="Change the MAC address of a network interface.")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="The network interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="mac", required=True, help="The new MAC address to assign to the interface")
    
    return parser.parse_args()

    #endregion

#region MAIN

# Parse command-line arguments
arguments = get_arguments()

# Retrieve the original MAC address
initial_mac = retrieve_current_mac(arguments.interface)
print(f'Current MAC: {str(initial_mac)}')

# Modify the MAC address
modify_mac_address(arguments.interface, arguments.mac)

# Retrieve the MAC address after modification
final_mac = retrieve_current_mac(arguments.interface)
if final_mac == arguments.mac:
    print(f'[+] MAC address was successfully changed to {final_mac}')
else:
    print('[-] MAC address was not changed')

#endregion
