def validate_mac_format(mac):  # This function is used to check the validity of the MAC address entered by the user
    valid = True               # In case user enters address in the wrong format we return error and exit the programme
    if not (len(mac) == 17):    # Checks if the length of the address is 17 or not 
        valid = False
    byte_list = mac.split(":")
    for each_byte in byte_list:   # Checks if for each byte the length is less than 255 
        try:
            mac_int = int(each_byte, 16)
            if not mac_int <= 255:
                valid = False
        except ValueError:
            valid = False
    return valid                # returns True or False as the value of the function depending on the computations

text_file= open("write it.text","w")  # Define a text file to store the Source address, Destination Address and Action Performed
text_file.write("\n")
text_file.write("SRC_MAC\t\t\t\t")
text_file.write("DST_MAC\t\t\t\t")
text_file.write("Action\t\n")       # Here Action Performed is whether the data is sent to all the ports or one individual port 
text_file.close()

dict1= {}   # Dictionary to store the Address and Port Values (Look Up Table)

while True:

    in_port = input("Enter input port :") # Ask for the input port number by user 
    if(int(in_port)>=100):                  # check for validity
        print("Enter Valid Port number less than 100")
        exit()

    SRC_MAC = input("Enter the Source MAC Address :").strip() # Ask for the Source MAC address by user 
    if(validate_mac_format(SRC_MAC)== False):                   # check for validity
        print("Invalid entry : " + SRC_MAC + " not in proper format, Please try again")
        exit()

    DST_MAC = input("Enter the Destination MAC Address :").strip() # Ask for the Destination MAC address by user 
    if(validate_mac_format(DST_MAC)== False):                   # check for validity
        print("Invalid entry : " + DST_MAC + " not in proper format, Please try again")
        exit()

    if DST_MAC == SRC_MAC:                                          # Return error if source and destination address is same and exit the programme
        print("Invalid entry : Destination and source cannot be same. Try Again !! ")
        exit()    

    packet=[in_port,SRC_MAC,DST_MAC]            # Store the input port, source address and destination address in packet array

    # Learning                                  # Here we learn , as in if the source address is not already present in the dictionary we add 
    if packet[1] not in dict1:                  # the address along with the port number to the dictionary
        dict1[packet[1]]= packet[0]

    # Forward                                    # The Forwarding process takes place here depending on whether or not the destination address is already
                                                 # present in the Lookup Table   
    if packet[2] not in dict1:                   # If destination address is not present in the lookup table we send the data to all the ports (broadcast)
        Action = "Broadcast sent from port "+packet[0]+ " to all ports except port "+ packet[0]
        print(Action)
    else:                                        # If the destination address is present in the Lookup table, we only send the data to that particular port
        Action = "Data sent from port "+packet[0]+ " to port "+ dict1[packet[2]]
        print(Action)  
    
    text_file = open("write it.text", "a")        # In this text file we store the source address, destination address and the action 
    text_file.write("\n")                         # that has been performed
    text_file.write(packet[1])
    text_file.write("\t\t")
    text_file.write(packet[2])
    text_file.write("\t")
    text_file.write(Action)