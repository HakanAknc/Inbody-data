import pandas as pd           # TODO bu kod exel tablosundaki isimleri ascii değerlerle eşletştiriyor

def hex_ascii_to_binary(hex_string):
    hex_string = hex_string.replace(' ', '')
    return bytes.fromhex(hex_string)

def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

def binary_to_ascii(binary_data):
    return binary_data.decode('ascii', errors='ignore')

def get_row_names_from_excel(excel_file_path):
    df = pd.read_excel(excel_file_path)
    row_names = df.iloc[:, 1].tolist()  # burda exel dosyasında 1.sütundaki satır ismlerini aldım 
    return row_names

def process_file(file_path, row_names):
    with open(file_path, 'r') as file:
        for line in file:
            hex_data = line.strip()  
            binary_data = hex_ascii_to_binary(hex_data)  
            split_data = split_by_separator(binary_data)  
            
            ascii_results = [binary_to_ascii(part) for part in split_data if part]  
            
            print(f"{'='*40}")
            for index, result in enumerate(ascii_results):
                description = row_names[index] if index < len(row_names) else f" {index + 1}"
                print(f"{description}: {result}")
            print(f"{'='*40}")

excel_file_path = 'Inbody_Data.xlsx'
row_names = get_row_names_from_excel(excel_file_path)

file_path = 'inbody.txt'
process_file(file_path, row_names)
