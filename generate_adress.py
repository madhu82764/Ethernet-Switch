import random

def random_MAC():
    return [ random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff) ]


def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))


if __name__ == '__main__':

    file= open('mac_to_port.txt', 'w')
    for i in range(1, 101):
        file = open("mac_to_port.txt", "a")
        file.write(MACprettyprint(random_MAC()))
        file.write("   port ")
        file.write(str(i))
        file.write("\n")
        file.close()


    
