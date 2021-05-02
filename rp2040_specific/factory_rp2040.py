from controllers import EmptyAfronomController
from factories import AbstractAfronomFactory
from interfaces.platforms import PikoPlatform
from rp2040_specific.instrument_rp2040 import LedLighter, BuzzerDrum, TogglerInstrument


class RP2040Factory(AbstractAfronomFactory, PikoPlatform):

    class Instrument:

        @staticmethod
        def createMechanicDrum():
            return TogglerInstrument(pin=14)  # rele zapojene do pinu 14

        @staticmethod
        def createBuzzerDrum():
            # return ThreadedInstrumentAdapter(BuzzerDrum())
            return BuzzerDrum(pin=15)  # bzuciak zapojeny do pinu 15

        @staticmethod
        def createLedLighter():
            # return ThreadedInstrumentAdapter(LedLighter())
            return LedLighter(pin=25)  # interna ledka na raspberry pico

    def createDefaultInstrument(self):
        return RP2040Factory.Instrument.createMechanicDrum()

    def createDefaultController(self):
        return EmptyAfronomController()
