"""
# ? pandas
pandas exel kolon çekme 
import pandas as pd                                 

# Excel dosyasını oku
excel_file_path = 'Inbody_Data.xlsx'
df = pd.read_excel(excel_file_path)

# Kolon isimlerini al
# column_names = df.columns.tolist()

# Satır isimlerini al (Eğer satır isimleri ilk sütundaysa)
row_names = df.iloc[:, 1].tolist()

print("Satır İsimleri:", row_names)
"""

# ----------------------------------------------------------------------

"""
# ? os 
import os
print(dir(os))

Os modülünün hangi dizinde olduğunu söyler.
print(os.getcwd())
"""

"""
Bulunduğum dizini değiştirmek için ise;
os.chdir("C/Users/Desktop")
"""

"""
Şuan bulunduğumuz dizindeki dosyaları ve klasörleri listelemek için;
print(os.listdir())
for i in os.listdir():
    print(i)
"""

"""
Bulunduğum dizinde bir tane dosya,klasör oluşturmak için;
print(os.getcwd())
os.mkdir("Deneme1")
Şu şekilde bir kullanım hata verecektir;
os.mkdir("Deneme2/Deneme3")
"""

"""
Verilen kloseörleri iç içe oluşturmak için makedirs() metodu kullanılır.
print(os.getcwd())
os.makedirs("Deneme2/Deneme3")
"""

"""
Deneme2 altında Deneme3'ü silmek için os.rmdir() kullanılır.
print(os.getcwd())
os.rmdir("Deneme2/Deneme3")
"""

"""
Deneme2 ve Deneme2'nin altındaki bütün klasörleri silmek istediğinizde os.removedirs("Deneme2/Deneme3") Kullanılır;
print(os.getcwd())
os.removedirs("Deneme2/Deneme3")
"""

"""
Dizin içerisinde bulunan dosyanın ismini değiştirmek için os.rename("test.txt","test2.txt")
print(os.getcwd())
os.rename("test.txt","test2.txt")
"""

"""
Bir dosyanın özelliklerini almak için os.stat("test2.txt) fonksiyonu kullanılır.
print(os.getcwd())
from datetime import datetime
print(os.stat("test2.txt"))
dosyanın değiştirilme tarihini bulabilmek için:
print(os.stat("test2.txt").st_mtime)
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))
"""

"""
os.walk() fonksiyonu içerisine bir dizin verilir ve bu dizin altındaki tüm dosya ve klasörleri 
tek tek gezinerek os.walk fonksiyonu bir değer dönüyor.Ve bu değer liste değeridir.
print(os.walk("C:/Users/Özlem GÜL/Desktop/python"))
for i in os.walk("C:/Users/Özlem GÜL/Desktop/YAPAY ZEKA"):
    print(i)
her bir i değeri bir demettir.
for klasör_yolu,klasör_isimleri,dosya_isimler in os.walk("C:/Users/Özlem GÜL/Desktop/YAPAY ZEKA"):
    for i in dosya_isimler:
        print(i)
"""

# ------------------------------------------------------------------------------------------

"""
Yıl bilgisini almak için : %Y
Ay ismini almak için : %B
Gün ismini almak için : %A
Saat bilgisini almak için : %X
Gün bilgisini almak için : %D
"""

"""
# ?datatime
from datetime import datetime
# print(dir(datetime))
şu_an = datetime.now()    # şuan ki tarih-saat
print(şu_an)

print(şu_an.year)         # yıl
print(şu_an.month)        # ay
print(şu_an.day)          # gün
print(şu_an.hour)         # saat
print(şu_an.minute)       # dakika
print(şu_an.second)       # saniye
print(şu_an.microsecond)  # milisaniye
"""
from datetime import datetime
# print(dir(datetime))
şu_an = datetime.now()    # şuan ki tarih-saat
print(şu_an)