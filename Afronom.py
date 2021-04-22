from time import sleep
from machine import Pin, Timer, PWM
from _thread import *


class Instrument:

    def playNormal(self, note):
        pass

    def playAccent(self, note):
        pass

    def onBarStart(self):
        pass

    def onBarEnd(self):
        pass

    def play(self, note):
        if note == "x":
            return self.playNormal(note)
        elif note == "X":
            return self.playAccent(note)
        elif note == ".":
            return 0


class Printer(Instrument):

    def playNormal(self, note):
        print("p", end="")
        return 0

    def playAccent(self, note):
        print("P", end="")
        return 0

    # def onBarEnd(self):
    #    print("---");


class ThreadedInstrument(Instrument):

    def __init__(self):
        pass

    def playNormal_internal(self, note):
        pass

    def playAccent_internal(self, note):
        pass

    def playNormal(self, note):
        start_new_thread(self.playNormal_internal, (note,))
        return 0

    def playAccent(self, note):
        start_new_thread(self.playAccent_internal, (note,))
        return 0


class LedLighter(ThreadedInstrument):

    def __init__(self):
        super().__init__()
        self.led = Pin(25, Pin.OUT)

    def playNormal_internal(self, note):
        led = self.led
        led.on()
        sleep(0.107)
        led.off()
        return 0.107

    def playAccent_internal(self, note):
        led = self.led
        led.on()
        sleep(0.17)
        led.off()
        return 0.17


class BuzzerDrum_threaded(ThreadedInstrument):

    FREQ_NORMAL = 500
    FREQ_ACCENT = 800
    VOLUME = 150
    BEEP_LENGTH = 0.07

    def __init__(self):
        super().__init__()
        self.buzzer = PWM(Pin(15))

    def playNormal_internal(self, note):
        self.buzzer.freq(self.FREQ_NORMAL)
        self.buzzer.duty_u16(self.VOLUME)
        sleep(self.BEEP_LENGTH)
        self.buzzer.duty_u16(0)
        return self.BEEP_LENGTH

    def playAccent_internal(self, note):
        self.buzzer.freq(self.FREQ_ACCENT)
        self.buzzer.duty_u16(self.VOLUME)
        sleep(self.BEEP_LENGTH)
        self.buzzer.duty_u16(0)
        return self.BEEP_LENGTH


class Sequencer:

    TEMPO_BPM = 200
    instruments = []

    def withInstruments(self, instruments):
        self.instruments = instruments
        return self

    def playBar(self, bar):
        pass

    def playInLoop(self, bar):
        pass


class Sequencer_sync(Sequencer):

    def __init__(self):
        super().__init__()
        self.tempo_sec = 60 / self.TEMPO_BPM

    def playBar(self, bar):
        for instr in self.instruments:
            instr.onBarStart()

        for note in bar:
            seconds = 0
            for instr in self.instruments:
                seconds = seconds + instr.play(note)
            sleep(self.tempo_sec / 2 - seconds)
            #  sleep(self.tempo_sec / 2)

        for instr in self.instruments:
            instr.onBarEnd()

    def playInLoop(self, bar):
        while True:
            self.playBar(bar)


class Sequencer_timer(Sequencer):

    def __init__(self):
        super().__init__()
        self.timer = Timer()

    def onEightNote(self, timer):
        for instr in self.instruments:
            instr.play("x")

    def playBar(self, bar):
        self.timer.init(freq=self.TEMPO_BPM / 60, mode=Timer.PERIODIC, callback=self.onEightNote)

    def playInLoop(self, bar):
        self.playBar(bar)


Sequencer_sync() \
    .withInstruments([BuzzerDrum_threaded(), Printer()]) \
    .playInLoop("X.xx.xx.X.x.x.x.")
