# macAddressNotifier
Python script that scans the local network and will send text notifications if a specified device is found on the network.

# Usage
Set account_sid and auth_token to your Twilio credentials, along with sending and recieving phone numbers.
Set deviceAddress to the mac address of the device to search for. 

# Root Privilages
Root privilages are required. The script can either be run as root or the sudo password can be used. 

# limitations
- This script heavily relies on the subprocess module, which is very slow.

- The 'arp' command takes time to create an index of devices, so this also adds about 20 seconds to each loop

- iOS 14 has partially broken this program. Tracked iPhone must disable "random hardware address".
