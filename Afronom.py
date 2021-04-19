from time import sleep
from machine import Pin
import math


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
            playNormal(self, note);
        elif note == "X":
            playAccent(self, note);
        elif note == ".":
            pass


class Printer(Instrument):

    def playNormal(self, note):
        print("x");
        return 0;

    def playAccent(self, note):
        print("X");
        return 0;

    #def onBarEnd(self):
    #    print("---");

        
class LedLighter(Instrument):
    
    
    def __init__(self):
        self.led = Pin(25, Pin.OUT)

    def playNormal(self, note):
        l = self.led
        l.on();
        sleep(0.003);
        l.off();
        return 0.003;

    def playAccent(self, note):
        l = self.led
        l.on();
        sleep(0.07);
        l.off();
        return 0.07;

        
class Sequencer:
    
    TEMPO_BPM = 150;

    def __init__(self):
        self.tempo_sec = 60 / self.TEMPO_BPM

    def playBar(self, bar, instrument):
        instrument.onBarStart();
        for note in bar:
            if note == "X":
                seconds = instrument.playAccent(note)
                sleep(self.tempo_sec / 2 - seconds);
            if note == "x":
                seconds = instrument.playNormal(note)
                sleep(self.tempo_sec / 2 - seconds);
            elif note == ".":
                sleep(self.tempo_sec / 2 - seconds);
        instrument.onBarEnd();


sequencer = Sequencer()
instrument = LedLighter()
            
while True:
    sequencer.playBar("X.xx.xx.X.x.x.x.", instrument);