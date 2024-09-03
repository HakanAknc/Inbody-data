from watchdog.observers import Observer  # TODO bu kodda sadece klasör izleme işlemi yapıyor.
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'Dosya Değiştirildi: {event.src_path}')
    
    def on_created(self, event):
        print(f'Dosya Oluşturuldu: {event.src_path}')
    
    def on_deleted(self, event):
        print(f'Dosya Silindi: {event.src_path}')
    
    def on_moved(self, event):
        print(f'Dosya Taşındı/Yeniden Adlandırıldı: {event.src_path} -> {event.dest_path}')

if __name__ == "__main__":
    path = r""  # İzlenecek dizin (bu örnekte geçerli dizin)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
