from factories import AbstractAfronomFactory
from interfaces.platforms import M5StackPlatform
from m5stick_specific.instrument_m5stick import BuzzerDrum
from rp2040_specific.instrument_rp2040 import LedLighter, TogglerInstrument


class M5StickFactory(AbstractAfronomFactory, M5StackPlatform):

    class Instrument:

        @staticmethod
        def createMechanicDrum():
            return TogglerInstrument(pin=13)  # rele zapojene do pinu 14

        @staticmethod
        def createBuzzerDrum():
            return BuzzerDrum(pin=26)  # interny speaker
            # return ThreadedInstrumentAdapter(BuzzerDrum())

        @staticmethod
        def createLedLighter():
            return LedLighter(pin=19)  # interna ledka
            # return ThreadedInstrumentAdapter(LedLighter())

    def createDefaultInstrument(self):
        return M5StickFactory.Instrument.createMechanicDrum()


