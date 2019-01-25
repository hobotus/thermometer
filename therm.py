from machine import Pin, I2C
from ads1x15 import ADS1115

i2c = I2C(sda = Pin(21), scl = Pin(22))

ads = ADS1115(i2c, 72, 3)

size = 20

array = []
for _ in range(size):
    array.append(ads.read(0, 0))


while True:
    array.pop(0)
    array.append(ads.read(0, 0))

    print(sum(array)/size*1)
