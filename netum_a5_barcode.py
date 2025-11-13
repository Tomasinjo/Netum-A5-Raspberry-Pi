import serial
import time

# usually /dev/ttyACM0 or /dev/ttyUSB0
SERIAL_PORT = '/dev/ttyACM0' 
BAUD_RATE = 9600

def main():
    print(f"Attempting to open serial port {SERIAL_PORT} at {BAUD_RATE} baud.")
    
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("Serial port opened successfully.")
    except Exception as e:
        print(f"Error opening serial port: {e}")
        return

    try:
        print("Listening for barcode scans... (Press Ctrl+C to exit)")
        while True:
            line = ser.readline()
            
            if line:
                barcode_data = line.decode('utf-8').strip()
                print(f"Barcode scanned: {barcode_data}")
            time.sleep(0.01)

    except KeyboardInterrupt:
        if 'ser' in locals() and ser.is_open:
            ser.close() # gracefully close the serial port

if __name__ == '__main__':
    main()
