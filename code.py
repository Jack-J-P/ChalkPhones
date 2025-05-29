# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Digital In Out example"""

import time
import board
import random
from digitalio import DigitalInOut, Direction, Pull
import digitalio



led1 = digitalio.DigitalInOut(board.GP15)
led1.direction = digitalio.Direction.OUTPUT
led1.value = False

led2 = digitalio.DigitalInOut(board.GP14)
led2.direction = digitalio.Direction.OUTPUT
led2.value = False

led3 = digitalio.DigitalInOut(board.GP13)
led3.direction = digitalio.Direction.OUTPUT
led3.value = False

led4 = digitalio.DigitalInOut(board.GP12)
led4.direction = digitalio.Direction.OUTPUT
led4.value = False

led5 = digitalio.DigitalInOut(board.GP11)
led5.direction = digitalio.Direction.OUTPUT
led5.value = False

led6 = digitalio.DigitalInOut(board.GP10)
led6.direction = digitalio.Direction.OUTPUT
led6.value = False

led7 = digitalio.DigitalInOut(board.GP9)
led7.direction = digitalio.Direction.OUTPUT
led7.value = False

led8 = digitalio.DigitalInOut(board.GP8)
led8.direction = digitalio.Direction.OUTPUT
led8.value = False

led9 = digitalio.DigitalInOut(board.GP7)
led9.direction = digitalio.Direction.OUTPUT
led9.value = False

led10 = digitalio.DigitalInOut(board.GP6)
led10.direction = digitalio.Direction.OUTPUT
led10.value = False

led11 = digitalio.DigitalInOut(board.GP5)
led11.direction = digitalio.Direction.OUTPUT
led11.value = False

led12 = digitalio.DigitalInOut(board.GP4)
led12.direction = digitalio.Direction.OUTPUT
led12.value = False

led13 = digitalio.DigitalInOut(board.GP3)
led13.direction = digitalio.Direction.OUTPUT
led13.value = False

led14 = digitalio.DigitalInOut(board.GP16)
led14.direction = digitalio.Direction.OUTPUT
led14.value = False

led15 = digitalio.DigitalInOut(board.GP17)
led15.direction = digitalio.Direction.OUTPUT
led15.value = False

b1Down = False
in1 = DigitalInOut(board.GP0)
in1.direction = Direction.INPUT
in1.pull = Pull.UP

in2 = DigitalInOut(board.GP18)
in2.direction = Direction.INPUT
in2.pull = Pull.UP

in3 = DigitalInOut(board.GP19)
in3.direction = Direction.INPUT
in3.pull = Pull.UP

in4 = DigitalInOut(board.GP20)
in4.direction = Direction.INPUT
in4.pull = Pull.UP

in5 = DigitalInOut(board.GP21)
in5.direction = Direction.INPUT
in5.pull = Pull.UP

round = 0

# Define LED pins dynamically
led_pins = [board.GP15, board.GP14, board.GP13, board.GP12, board.GP11,
            board.GP10, board.GP9, board.GP8, board.GP7, board.GP6,
            board.GP5, board.GP4, board.GP3, board.GP16, board.GP17]

 #Initialize LEDs dynamically
leds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10, led11, led12, led13, led14, led15]

print(leds[1].direction)
print(led1.direction)

for led in leds:
    led.direction = digitalio.Direction.OUTPUT
    led.value = False

def randLEDs():
    
    for led in leds:
        led.direction = digitalio.Direction.OUTPUT
        led.value = False
    time.sleep(2)
    #Generate a random number between 1 and 5
    random_number = random.randint(1, 5)
    print("Number of Lights:", random_number)

    #Select random LEDs and turn them on
    chosen_leds = []
    available_leds = leds.copy()  # Make a copy to track available LEDs

    for _ in range(random_number):
        chosen_led = random.choice(available_leds)  # Pick one LED
        chosen_leds.append(chosen_led)
        available_leds.remove(chosen_led)  # Remove it to ensure uniqueness

    for i, led in enumerate(chosen_leds, start=1):
        led.value = True  # Turn LED on
        print(f"Light{i} Activated:", led_pins[leds.index(led)])  # Show which LED activated




while True:
    if ( (not b1Down) and (not in1.value) ):
        randLEDs()
        b1Down = True
        round += 1
        print("reset round")
    elif (in1.value):
        b1Down = False
        print(2)
    else:
        print(0)


    time.sleep(0.1)

