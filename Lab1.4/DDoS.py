import ipaddress
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self, (int(random.randint(0x0B000000, 0xDF000000)), random.randint(8, 24)), strict = False)
    def regular(self):
        if not self.is_multicast and not self.is_private:
            return True
        else:
            return False

networks = [IPv4RandomNetwork().with_prefixlen for x in range(0, 51)]

print(networks)
