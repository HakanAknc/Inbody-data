import os     # TODO bu kod sürekli klasör izleme işi yapıyor  verilen hex ascii dosyalarını çevirip başka klasöre kaydediyor
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def hex_ascii_to_binary(hex_string):
    return bytes.fromhex(hex_string)

def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

def binary_to_ascii(binary_data):
    return binary_data.decode('ascii', errors='ignore')

def process_and_save_file(input_file_path, output_folder):
    filename = os.path.basename(input_file_path)
    output_file_path = os.path.join(output_folder, filename)

    with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
        for line in file:
            hex_data = line.strip()
            binary_data = hex_ascii_to_binary(hex_data)
            split_data = split_by_separator(binary_data)
            
            ascii_results = [binary_to_ascii(part) for part in split_data]
            output_file.write(' '.join(ascii_results) + '\n')

class MyHandler(FileSystemEventHandler):
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def on_modified(self, event):
        if not event.is_directory: 
            process_and_save_file(event.src_path, self.output_folder)
    
    def on_created(self, event):
        if not event.is_directory: 
            process_and_save_file(event.src_path, self.output_folder)

input_folder = r"C:\Users\Hakan Akıncı\Desktop\deneme"  # İzlemek istediğiniz klasörün yolu
output_folder = 'output_folder_path'  # İşlenmiş dosyaların kaydedileceği klasörün yolu

if __name__ == "__main__":
    os.makedirs(output_folder, exist_ok=True)  # Çıktı klasörü yoksa oluştur

    event_handler = MyHandler(output_folder=output_folder)
    observer = Observer()
    observer.schedule(event_handler, path=input_folder, recursive=False)

    print(f"İzleme başlatıldı: {input_folder}")
    observer.start()

    try:
        while True:
            pass  # Sonsuz döngüde kalır ve dosya değişikliklerini izler
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

