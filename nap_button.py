import time

import RPi.GPIO as GPIO
from pygame import mixer
from pathlib import Path

mixer.init()

GPIO.setmode(GPIO.BCM)
GPIO_BUTTON = 23
GPIO.setup(GPIO_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class SleepMachine:
    def __init__(self):
        """
        Initialize the sleep machine
        """
        print("Initializing sleep machine")
        self.playing = False
        self.button_push_time = 0
        self.debounce_time = 0.5
        mixer.music.set_volume(0.3)
        sleep_noise = Path(__file__).parent / 'audio' / 'sleep_noise.mp3'
        mixer.music.load(sleep_noise)
        print(f"Sleep machine initialized with audio file: {sleep_noise}")

    def play_pause_sound(self):
        """
        Play or pause the sound
        :return:
        """
        if self.playing:
            mixer.music.pause()
            self.playing = False
            print("Pausing sound")
        else:
            mixer.music.play(loops=-1)
            self.playing = True
            print("Playing sound")

    def button_callback(self, channel):
        """
        Callback function to handle button presses, with debounce
        :return:
        """

        if time.time() - self.button_push_time > self.debounce_time:
            print(f"Button pressed at channel: {channel}")
            self.button_push_time = time.time()
            self.play_pause_sound()


SleepMachineAccess = SleepMachine()

# Add an event detection to the button
GPIO.add_event_detect(GPIO_BUTTON, GPIO.FALLING, callback=SleepMachineAccess.button_callback)

# Keep the program running and provide a way to exit and cleanup the GPIO
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting.")
