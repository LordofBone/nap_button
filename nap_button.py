import time
from pathlib import Path

import RPi.GPIO as GPIO
from pygame import mixer, error as pygame_error

from config.sleep_machine_config import *

mixer.init()

GPIO.setmode(GPIO.BCM)
GPIO_BUTTON = button_pin
GPIO.setup(GPIO_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class SleepMachine:
    def __init__(self):
        """
        Initialize the sleep machine
        """
        print("Initializing sleep machine")
        self.playing = False
        self.button_push_time = 0
        self.debounce_time = button_debounce_time
        mixer.music.set_volume(volume)
        sleep_noise = Path(__file__).parent / 'audio' / f'{audio_file_name}'
        try:
            mixer.music.load(sleep_noise)
        except pygame_error:
            raise Exception(f"Could not load audio file: {sleep_noise}")
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
