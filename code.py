from adafruit_circuitplayground import cp
from time import sleep


def slow_print(inp):
    print(inp)
    sleep(.05)

def Main():
    switchpos = cp.switch
    R = 0
    G = 0
    B = 0
    x, y, z = cp.acceleration
    if switchpos == False:
        cp.pixels.fill((0, 0, 0))
        slow_print("Switch value %s" % switchpos)

    else:
        slow_print((x, y, z))
        cp.pixels.fill(((R + abs(int(x))), (G + abs(int(y))), (B + abs(int(z)))))
        # slow_print(switchpos)



while True:
    Main()
