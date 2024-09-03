def hex_ascii_to_binary(hex_string):   # Todo bu kod çevirme işlemi yapar
    return bytes.fromhex(hex_string)

def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

def binary_to_ascii(binary_data):
    return binary_data.decode('ascii', errors='ignore')

def process_file(file_path):
    with open(file_path, 'r') as file:  
        for line in file:               
            hex_data = line.strip()     
            binary_data = hex_ascii_to_binary(hex_data)    
            split_data = split_by_separator(binary_data)   
            
            ascii_results = [binary_to_ascii(part) for part in split_data] 
            print(ascii_results) 

file_path = 'inbody.txt'
process_file(file_path)
