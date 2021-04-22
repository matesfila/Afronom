from sequencer import Sequencer_sync
from instrument import InstrumentFactory
from settings import Settings


class Afronom:

    def __init__(self):
        self.settings = Settings()
        self.tempo = self.settings.settingsData["Afronom"]["tempo"]
        self.volume = self.settings.settingsData["Afronom"]["volume"]
        self.rhythm = self.settings.settingsData["Afronom"]["rhythm"]

    def play(self):
        Sequencer_sync() \
            .withTempo(self.tempo) \
            .withInstruments([InstrumentFactory.createBuzzerDrum()]) \
            .playInLoop("X.xx.xx.X.x.x.x.")


# test_settings()
Afronom().play()
