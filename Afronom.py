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


class ThreadedInstrumentAdapter(Instrument):

    def __init__(self, instrument):
        self.instrument = instrument

    def playNormal(self, note):
        start_new_thread(self.instrument.playNormal, (note,))
        return 0

    def playAccent(self, note):
        start_new_thread(self.instrument.playAccent, (note,))
        return 0


class LedLighter(Instrument):

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


class BuzzerDrum(Instrument):

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


class InstrumentFactory:

    @staticmethod
    def createBuzzerDrum():
        return ThreadedInstrumentAdapter(BuzzerDrum())

    @staticmethod
    def createPrinter():
        return Printer()

    @staticmethod
    def createLedLighter():
        return ThreadedInstrumentAdapter(LedLighter())


class Sequencer:

    TEMPO_BPM = 150
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
            # sleep(self.tempo_sec / 2 - seconds)
            sleep(self.tempo_sec / 2)

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
    .withInstruments([InstrumentFactory.createBuzzerDrum(), Printer()]) \
    .playInLoop("X.xx.xx.X.x.x.x.")
