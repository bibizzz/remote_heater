import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run yr script")


GPIO.setmode(GPIO.BOARD)
# defines channel for controlling the set up
# wheel motor
forward_ch = 10 
backward_ch = 11
# light the scen
light_ch = 12
# press button
button_ch = 13

channel_list = [forward_ch, backward_ch, light_ch, button_ch]

def init_out(channel_list):
    GPIO.setup(channel_list, GPIO.OUT)


# set pin to 1 for a duration time
def action(channel, duration_s):
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(duration_s)
    GPIO.output(channel, GPIO.LOW) 