from _thread import *
from time import sleep
from machine import Timer
from interfaces import Sequencer


class AbstractSequencer(Sequencer):
    instruments = []
    tempo = None
    tempo_sec = None
    volume = None

    stopped = True

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

    def speedUp(self):
        self.withTempo(self.tempo + 5)

    def slowDown(self):
        self.withTempo(self.tempo - 5)

    def playBar(self, bar):
        pass

    def playInLoop(self, bar):
        pass

    def stop(self):
        self.stopped = True

    def isPlaying(self):
        return not self.stopped

    def setStopped(self, value):
        self.stopped = value

    def getStopped(self):
        return self.stopped


class Sequencer_sync(AbstractSequencer):

    def __init__(self):
        super().__init__()

    def playBar(self, bar):
        self.setStopped(False)
        for instr in self.instruments:
            instr.onBarStart()

        for note in bar:
            if self.getStopped():
                break
            seconds = 0
            for instr in self.instruments:
                seconds = seconds + instr.play(note)
            sleep(self.tempo_sec / 2 - seconds)
            # sleep(self.tempo_sec / 2)

        for instr in self.instruments:
            instr.onBarEnd()

        # self.stopped = True

    def playInLoop(self, bar):
        self.setStopped(False)
        start_new_thread(self.threadFunc, (bar,))

    def threadFunc(self, bar):
        while not self.getStopped():
            self.playBar(bar)


class Sequencer_timer(AbstractSequencer):

    def __init__(self):
        super().__init__()
        self.timer = Timer(1)

    def onEightNote(self, timer):
        for instr in self.instruments:
            instr.play("x")

    def playBar(self, bar):
        self.timer.init(period=200, mode=Timer.PERIODIC, callback=self.onEightNote)
        # self.timer.init(freq=self.tempo / 60, mode=Timer.PERIODIC, callback=self.onEightNote)

    def playInLoop(self, bar):
        self.playBar(bar)



