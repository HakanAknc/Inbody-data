import serial   # TODO Bu bir pyserial örnek kodudur.

# Seri portu açın
ser = serial.Serial('COM3', 9600, timeout=1)  # Port adı ve baud rate ayarları

# Veri gönderin
ser.write(b'Hello, World!\n')

# Gelen veriyi okuyun
response = ser.readline().decode('utf-8').strip()
print(f"Gelen Veri: {response}")

# Seri portu kapatın
ser.close()
