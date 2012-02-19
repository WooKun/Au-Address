file_post_code = open('/home/wookun/Documents/Austalia Address/Post Code List.txt','r')
code_set = file_post_code.readlines()

file_input_address = open('/home/wookun/Documents/Austalia Address/input address.txt','r')
input_address_list = file_input_address.readlines()

for i in range(len(code_set)):
    code_set[i] = code_set[i].replace('\n','') 
    #"\n" may be tricky, so we eliminate newline here.
    
for i in range(len(input_address_list)):
    input_address_list[i] = input_address_list[i].replace('\n','')
address_w_code = []
for temp_address in input_address_list:
    temp_code = temp_address[-4:] #Extract post code.
    if temp_code in code_set:
        address_w_code.append(temp_address)


