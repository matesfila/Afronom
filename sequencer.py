from time import sleep
from machine import Timer


class Sequencer:

    instruments = []
    tempo = None
    tempo_sec = None
    volume = None

    def withTempo(self, tempo):
        self.tempo = tempo
        self.tempo_sec = 60 / self.tempo
        return self

    def withVolume(self, volume):
        self.volume = volume
        return self

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
        self.timer.init(freq=self.tempo / 60, mode=Timer.PERIODIC, callback=self.onEightNote)

    def playInLoop(self, bar):
        self.playBar(bar)
