from datetime import datetime
import time

def tima():
    current_time = datetime.now().strftime("%H:%M:%S")

    print(current_time)

    time.sleep(1)
    ascii_values = [ord(char) for char in current_time]
    print (ascii_values)
    
tima()

