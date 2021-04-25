from _thread import *
from interfaces import Instrument


class AbstractInstrument(Instrument):

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


class Printer(AbstractInstrument):

    def playNormal(self, note):
        print("p", end="")
        return 0

    def playAccent(self, note):
        print("P", end="")
        return 0

    #  def onBarEnd(self):
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
