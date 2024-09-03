def hex_ascii_to_binary(hex_string):    # TODO Buraya kadar manuel
    hex_string = hex_string.replace(' ', '')
    return bytes.fromhex(hex_string)

def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

def binary_to_ascii(binary_data):
    return binary_data.decode('ascii', errors='ignore')

# Dosyayı okuyarak veriyi işler ve açıklamalı çıktıyı yazdırır. 
def process_file(file_path):
    headers = [
        "InBody ID ",  
        "ID ",  
        "Gender ",
        "Height ",
        "Age ",
        "Weight ",
        "Test Date ",
        "Test Time "  
    ]
    
    with open(file_path, 'r') as file:
        for line in file:
            hex_data = line.strip()  
            binary_data = hex_ascii_to_binary(hex_data)  
            split_data = split_by_separator(binary_data)  
            
            ascii_results = [binary_to_ascii(part) for part in split_data if part]  
            
            print(f"{'='*40}")
            for index, result in enumerate(ascii_results):
                description = headers[index] if index < len(headers) else f" {index + 1}"
                print(f"{description}: {result}")
            print(f"{'='*40}")

file_path = 'inbody.txt'
process_file(file_path)
