from AfronomFactory import AfronomFactory


class Afronom:

    sequencer = None

    def __init__(self):
        self.settings = AfronomFactory.createSettings()
        self.tempo = self.settings.settingsData["Afronom"]["tempo"]
        self.volume = self.settings.settingsData["Afronom"]["volume"]
        self.rhythm = self.settings.settingsData["Afronom"]["rhythm"]

        AfronomFactory.createDefaultController() \
            .withSpeedUpEvent(self.speedUp) \
            .withSlowDownEvent(self.slowDown) \
            .initialize()

        # AfronomKeyboardController(self).initialize()

    def speedUp(self):
        if self.sequencer is not None:
            self.sequencer.speedUp()

    def slowDown(self):
        if self.sequencer is not None:
            self.sequencer.slowDown()

    def play(self):
        self.sequencer = AfronomFactory.createSequencer()
        self.sequencer \
            .withTempo(self.tempo) \
            .withInstruments([AfronomFactory.createDefaultInstrument()]) \
            .playInLoop("X.xx.xx.X.x.x.x.")


if __name__ == "__main__":
    # test_settings()
    Afronom().play()
