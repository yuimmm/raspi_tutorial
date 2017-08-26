from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT

PIN = 4

for i in range(10):
    while True:
        humi, temp = DHT.read_retry(DHT.DHT11, PIN)
        # remeasure when value is incorrect
        if (humi > 90) or (temp > 50):
            print('- error:', humi, temp)
            sleep(0.1)
            continue
        break
    #  display informatin
    print("+", datetime.now().strftime('%H:%M:%S'))
    print("| humid=", humi, "%")
    print("| temp=", temp, "Do")
    sleep(10)

