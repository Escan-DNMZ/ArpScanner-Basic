import scapy.all as scapy
import optparse

def GetUserInput():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip",dest="ip",help="Enter ip adress")
    
 
    return parser.parse_args()
  

def ArpRequest(IPAdress):
    arp_request = scapy.ARP(pdst=IPAdress)
    return arp_request

def MacBroadcast():
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    return broadcast_packet

if __name__ == "__main__":
    
    (userInput,Arguments) = GetUserInput()
    if userInput.ip:
         combined_packet = ArpRequest(userInput.ip)/MacBroadcast()
         (answers,unanswers) = scapy.srp(combined_packet,timeout=1)
         answers.summary()
    else:
        print("Enter ip adress")
    
   
    
    
