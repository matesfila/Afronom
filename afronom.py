from interfaces import Afronom


class AfronomImpl(Afronom):

    factory = None
    sequencer = None
    controller = None

    def __init__(self, factory):
        self.factory = factory
        self.settings = self.factory.createSettings()
        self.tempo = self.settings.settingsData["Afronom"]["tempo"]
        self.volume = self.settings.settingsData["Afronom"]["volume"]
        self.rhythm = self.settings.settingsData["Afronom"]["rhythm"]

        self.controller = self.factory.createDefaultController() \
            .withSpeedUpEvent(self.speedUp) \
            .withSlowDownEvent(self.slowDown) \
            .withTogglePlayEvent(self.togglePlay) \
            .initialize()

        self.sequencer = self.factory.createSequencer() \
            .withTempo(self.tempo) \
            .withInstruments([self.factory.createDefaultInstrument()])

    def speedUp(self):
        # print("speedUp ")
        if self.sequencer is not None:
            self.sequencer.speedUp()

    def slowDown(self):
        # print("slowDown")
        if self.sequencer is not None:
            self.sequencer.slowDown()

    def play(self):
        # print("play")
        # self.controller.initialize()  # TODO preskumat tento riadok, na x86 bez neho po stlaceni stop uz nefunguje play
        # print("before play: {}".format(self.controller))
        self.sequencer.playInLoop(self.rhythm)
        # print("after play: {}".format(self.controller))

    def stop(self):
        # print("stop")
        self.sequencer.stop()

    def isPlaying(self):
        return self.sequencer is not None and self.sequencer.isPlaying()

    def togglePlay(self):
        # print("toggle")
        # return None
        if self.isPlaying():
            self.speedUp()
        else:
            self.play()

# if __name__ == "__main__":
#     # test_settings()
#     AfronomImpl(X86Factory()).play()

