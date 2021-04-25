from instruments import AbstractInstrument
from interfaces.platforms import PikoPlatform
from time import sleep
from machine import Pin, PWM


class LedLighter(AbstractInstrument, PikoPlatform):

    def __init__(self):
        super().__init__()
        self.led = Pin(25, Pin.OUT)

    def playNormal(self, note):
        led = self.led
        led.on()
        sleep(0.107)
        led.off()
        return 0.107

    def playAccent(self, note):
        led = self.led
        led.on()
        sleep(0.17)
        led.off()
        return 0.17


class BuzzerDrum(AbstractInstrument, PikoPlatform):

    FREQ_NORMAL = 500
    FREQ_ACCENT = 800
    VOLUME = 150
    BEEP_LENGTH = 0.07

    def __init__(self):
        super().__init__()
        self.buzzer = PWM(Pin(15))

    def playNormal(self, note):
        self.buzzer.freq(self.FREQ_NORMAL)
        self.buzzer.duty_u16(self.VOLUME)
        sleep(self.BEEP_LENGTH)
        self.buzzer.duty_u16(0)
        return self.BEEP_LENGTH

    def playAccent(self, note):
        self.buzzer.freq(self.FREQ_ACCENT)
        self.buzzer.duty_u16(self.VOLUME)
        sleep(self.BEEP_LENGTH)
        self.buzzer.duty_u16(0)
        return self.BEEP_LENGTH
