import machine
import utime
import random

# Set up the tilt switch and LED
tilt_switch_pin = machine.Pin(0, machine.Pin.IN)
led_pin = machine.Pin(1, machine.Pin.OUT)

# Initialize game variables
score = 0
game_over = False

def flash_led():
    # Flash the LED three times
    for _ in range(3):
        led_pin.on()
        utime.sleep(0.2)
        led_pin.off()
        utime.sleep(0.2)

def wait_for_tilt():
    utime.sleep(random.randint(0,10))
    # Wait for tilt switch to be activated with timeout
    start_time = utime.time()
    while tilt_switch_pin.value() == 0:
        if utime.time() - start_time > 5:
            return False
    return True

while not game_over:
    # Prompt the player to tilt the switch
    
    print("Tilt the switch!")
    success = wait_for_tilt()

    if success:
        # Tilt switch activated - increment score
        score += 1
        print("Success! Score: {}".format(score))
        flash_led()
    else:
        # Tilt switch timeout - game over
        game_over = True

    # Check if game over condition is reached
    if score >= 10:
        game_over = True

# Game over - display final score
print("Game Over!")
print("Final Score: {}".format(score))