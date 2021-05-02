from instruments import AbstractInstrument
from interfaces.platforms import M5StackPlatform
from time import sleep
from machine import Pin, PWM


class BuzzerDrum(AbstractInstrument, M5StackPlatform):

    FREQ_NORMAL = 500
    FREQ_ACCENT = 800
    VOLUME = 200
    BEEP_LENGTH = 0.07

    pinNumber = None

    def __init__(self, pin):
        super().__init__()
        self.pinNumber = pin
        self.buzzer = PWM(Pin(self.pinNumber))

    def playNormal(self, note):
        self.buzzer.freq(self.FREQ_NORMAL)
        self.buzzer.duty(self.VOLUME)
        sleep(self.BEEP_LENGTH)
        self.buzzer.duty(0)
        return self.BEEP_LENGTH

    def playAccent(self, note):
        self.buzzer.freq(self.FREQ_ACCENT)
        self.buzzer.duty(self.VOLUME)
        sleep(self.BEEP_LENGTH)
        self.buzzer.duty(0)
        return self.BEEP_LENGTH

