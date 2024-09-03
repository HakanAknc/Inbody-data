from watchdog.observers import Observer  # TODO bu kodda "watchdog" kütüphane testi yapıldı sadece klasör izleniyor.
from watchdog.events import FileSystemEventHandler
import time

class DosyaIzleyici(FileSystemEventHandler):
    def on_created(self, event):
        print(f'Yeni dosya oluşturuldu: {event.src_path}')
    
    def on_deleted(self, event):
        print(f'Dosya silindi: {event.src_path}')
    
    def on_modified(self, event):
        print(f'Dosya değiştirildi: {event.src_path}')

# Klasör yolunu belirleyin, örneğin: C:\Users\Kullanici\Desktop\IzlenecekKlasor
klasor_yolu = r""

event_handler = DosyaIzleyici()
observer = Observer()
observer.schedule(event_handler, path=klasor_yolu, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
