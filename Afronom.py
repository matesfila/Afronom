from time import sleep
from machine import Pin, Timer


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


class LedLighter(Instrument):

    def __init__(self):
        self.led = Pin(25, Pin.OUT)
        # self.timer = Timer()

    # def playNormal(self, note):
    #     self.note = note
    #     # self.timer.init(freq=0, mode=Timer.ONE_SHOT, callback=self.playNormal_internal)

    def playNormal(self, note):
        led = self.led
        led.on()
        sleep(0.007)
        led.off()
        return 0.007

    def playAccent(self, note):
        led = self.led
        led.on()
        sleep(0.07)
        led.off()
        return 0.07


class Sequencer:
    TEMPO_BPM = 130

    def __init__(self):
        self.instruments = []

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
            # sleep(self.tempo_sec / 2)

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
    .withInstruments([LedLighter(), Printer()]) \
    .playInLoop("X.xx.xx.X.x.x.x.")
