from factories import DefaultAfronomFactory
from interfaces import Afronom


class AfronomImpl(Afronom):

    sequencer = None

    def __init__(self):
        self.settings = DefaultAfronomFactory.createSettings()
        self.tempo = self.settings.settingsData["Afronom"]["tempo"]
        self.volume = self.settings.settingsData["Afronom"]["volume"]
        self.rhythm = self.settings.settingsData["Afronom"]["rhythm"]

        DefaultAfronomFactory.createDefaultController() \
            .withSpeedUpEvent(self.speedUp) \
            .withSlowDownEvent(self.slowDown) \
            .initialize()

    def speedUp(self):
        if self.sequencer is not None:
            self.sequencer.speedUp()

    def slowDown(self):
        if self.sequencer is not None:
            self.sequencer.slowDown()

    def play(self):
        self.sequencer = DefaultAfronomFactory.createSequencer()
        self.sequencer \
            .withTempo(self.tempo) \
            .withInstruments([DefaultAfronomFactory.createDefaultInstrument()]) \
            .playInLoop("X.xx.xx.X.x.x.x.")


if __name__ == "__main__":
    # test_settings()
    AfronomImpl().play()
