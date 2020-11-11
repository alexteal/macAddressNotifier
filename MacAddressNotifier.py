import subprocess
from twilio.rest import Client


# Twilio identifiers here:
account_sid = 'AccountSID'
auth_token = 'Token'
client = Client(account_sid, auth_token)
deviceAtLocation = False
# This would be the address you are scanning for
deviceAddress = "XX:XX:XX:XX:XX:XX"


def macAddressArray():
    macAddys = []
    index = 0
    print("beginning network scrape")
    output = str(subprocess.check_output(['arp -a'], shell=True))
    while output.find(" at ") > 0:
        macAddys.append(output[output.find(" at ") + 4:output.find(" on ")])
        output = output[output.find(" on ") + 4:len(output)]
        index += 1
    print("testing arp cache purge")
    # Sudo is required to purge the arp cache
    # You can either give this program root privileges, or place the sudo password here
    subprocess.call('echo {} | sudo -S {}'.format('YOUR_PASSWORD', 'arp -a -d'), shell=True)
    print("arp cache successfully purged.")
    return macAddys


while True:
    macAddresses = macAddressArray()
    if deviceAddress in macAddresses:
        message = client.messages.create(
            body='The specified device has connected to the server\'s local network.',
            #Phone number provided by Twilio goes here
            from_='+twilio',
            #Destination number goes here
            to='+destination'
        )
        print (message.sid)
        print('device at location')
        deviceAtLocation = True
        while deviceAtLocation == True:
            subprocess.run(['arp -a'], shell=True)
            # arp -a doesn't fully run without a sleep function
            time.sleep(20)
            print("device still at location")
            macAddresses = macAddressArray()
            if deviceAddress not in macAddresses:
                deviceAtLocation = False
        print("device has left location.")
    print(deviceAddress in macAddresses)
    print("device not at location")

    time.sleep(10)
