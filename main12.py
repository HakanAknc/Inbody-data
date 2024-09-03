import os        # TODO dosya izlem, çevirme, kaydetme işlemi yapar. yeni eklenen dosya ismi değişikiliği kaydederke tarih formatında kaydediyor
from datetime import datetime   # todo ikili kaydediyor
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# HEX-ASCII dizesini binary formatına dönüştürür.
def hex_ascii_to_binary(hex_string):
    return bytes.fromhex(hex_string)

# Binary veriyi belirli bir ayraç kullanarak böler.
def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

# Binary formatındaki veriyi ASCII formatına dönüştürür.
def binary_to_ascii(binary_data):
    return binary_data.decode('ascii', errors='ignore')

# Dosyayı işleyip yeni klasöre kaydeden fonksiyon.
def process_and_save_file(input_file_path, output_folder):
    # Mevcut tarih ve saat bilgisini al
    current_time = datetime.now().strftime("%Y-%m-%d %H%M%S.%f")  # Tarih ve saat formatı

    # Yeni dosya ismi oluştur
    output_filename = f"{current_time}.txt"
    output_file_path = os.path.join(output_folder, output_filename)

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

    def on_modified(self, event):    # todo on_modified, Bu olay, mevcut bir dosya veya dizin üzerinde bir değişiklik yapıldığında tetiklenir.
        if not event.is_directory: 
            process_and_save_file(event.src_path, self.output_folder)
    
    def on_created(self, event):     # todo on_created, Bu olay, bir dosya veya dizin oluşturulduğunda tetiklenir.
        if not event.is_directory: 
            process_and_save_file(event.src_path, self.output_folder)

input_folder = r""  # İzlemek istediğiniz klasörün yolu
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
