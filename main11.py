import os   # TODO bu dosya izleme, çevirme ve çalışan çalışmayan dosyaları ayrıma ve dosya adına saat eklem işlemi yapıyor.
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# HEX-ASCII dizesini binary formatına dönüştürür.
def hex_ascii_to_binary(hex_string):
    try:
        return bytes.fromhex(hex_string)
    except ValueError:
        return None  # Hatalı hex string olması durumunda None döndürür

# Binary veriyi belirli bir ayraç kullanarak böler.
def split_by_separator(data, separator=b'\x1b'):
    return data.split(separator)

# Binary formatındaki veriyi ASCII formatına dönüştürür.
def binary_to_ascii(binary_data):
    try:
        return binary_data.decode('ascii', errors='ignore')
    except UnicodeDecodeError:
        return None  # Hatalı binary veriyi ASCII'ye çeviremiyorsa None döndürür

# Dosyayı işleyip başarılı veya hatalı klasörlerine kaydeden fonksiyon.
def process_and_save_file(input_file_path, success_folder, error_folder):
    filename = os.path.basename(input_file_path)
    
    # Saat ve tarih bilgisini al
    current_time = datetime.now().strftime("%H%M%S")
    output_filename = f"{filename}-{current_time}"
    
    output_file_path_success = os.path.join(success_folder, output_filename)
    output_file_path_error = os.path.join(error_folder, output_filename)

    try:
        with open(input_file_path, 'r') as file:
            with open(output_file_path_success, 'w') as output_file:
                for line in file:
                    hex_data = line.strip()
                    binary_data = hex_ascii_to_binary(hex_data)
                    if binary_data is None:
                        raise ValueError("Invalid HEX string")

                    split_data = split_by_separator(binary_data)
                    ascii_results = [binary_to_ascii(part) for part in split_data]

                    if None in ascii_results:
                        raise ValueError("Invalid ASCII conversion")

                    output_file.write(' '.join(ascii_results) + '\n')
    except Exception as e:
        print(f"Hata: {e}")
        os.rename(input_file_path, output_file_path_error)

# Dosya sistemindeki değişiklikleri izleyen sınıf.
class MyHandler(FileSystemEventHandler):
    def __init__(self, success_folder, error_folder):
        self.success_folder = success_folder
        self.error_folder = error_folder

    def on_modified(self, event):
        if not event.is_directory:
            process_and_save_file(event.src_path, self.success_folder, self.error_folder)

    def on_created(self, event):
        if not event.is_directory:
            process_and_save_file(event.src_path, self.success_folder, self.error_folder)

# Girdi klasörünün yolu
input_folder = r"C:\Users\Hakan Akıncı\Desktop\deneme"  # İzlemek istediğiniz klasörün yolu
# Çıktı klasörlerinin yolları
success_folder = 'success_folder_path'  # Başarılı dosyaların kaydedileceği klasör
error_folder = 'error_folder_path'  # Hatalı dosyaların kaydedileceği klasör

if __name__ == "__main__":
    os.makedirs(success_folder, exist_ok=True)  # Başarılı klasörü oluştur
    os.makedirs(error_folder, exist_ok=True)    # Hatalı klasörü oluştur

    event_handler = MyHandler(success_folder=success_folder, error_folder=error_folder)
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
