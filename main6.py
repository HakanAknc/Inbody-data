import os       # TODO bu kod birden fazla asci verisini alıp işleyip yeni bir klasöre kaydediyor
 
def hex_ascii_to_binary(hex_string):
    return bytes.fromhex(hex_string)

def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

def binary_to_ascii(binary_data):
    return binary_data.decode('ascii', errors='ignore')

def process_files_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(input_file_path):
            output_file_path = os.path.join(output_folder, filename)
            
            with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
                for line in file:
                    hex_data = line.strip()
                    binary_data = hex_ascii_to_binary(hex_data)
                    split_data = split_by_separator(binary_data)
                    
                    ascii_results = [binary_to_ascii(part) for part in split_data]
                    output_file.write(' '.join(ascii_results) + '\n')

input_folder = 'hex_asci'
output_folder = 'binary_ascii' 
process_files_in_folder(input_folder, output_folder)
