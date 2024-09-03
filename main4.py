def hex_ascii_to_binary(hex_string):          # TODO farklı dosyaya kaydetme işlemi
    return bytes.fromhex(hex_string)

def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

def binary_to_ascii(binary_data):
    return binary_data.decode('ascii', errors='ignore')

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as file, open(output_file_path, 'w') as output_file:
        for line in file:
            hex_data = line.strip().decode('ascii')
            binary_data = hex_ascii_to_binary(hex_data)
            split_data = split_by_separator(binary_data)
            
            ascii_results = [binary_to_ascii(part) for part in split_data]
            output_file.write(' '.join(ascii_results) + '\n')

input_file_path = 'inbody.txt'
output_file_path = 'output410.txt'

process_file(input_file_path, output_file_path)
