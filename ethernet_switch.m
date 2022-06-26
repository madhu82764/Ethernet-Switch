

M= containers.Map();

while true

    input_port_number= input('Enter the input port no : ', 's');
    src_mac_address= input('Enter source mac address : ', 's');
    dest_mac_address = input('Enter destination mac address : ','s');
    
    
    %learn 
    if isKey(M , src_mac_address) ~=1
        M(src_mac_address)= input_port_number;
    end

    %forwarding
    if isKey(M , dest_mac_address) ~=1
        statement= 'broadcast to all except input port';
        disp(statement)

    else
        statement= 'data sent to particular port';
        disp(statement)
        port= M(dest_mac_address);
        disp(port)
    end

end 