from controllers import EmptyAfronomController
from factories import AbstractAfronomFactory
from instruments import Printer
from rp2040_specific.instrument_rp2040 import LedLighter, BuzzerDrum


class RP2040Factory(AbstractAfronomFactory):

    class Instrument:

        @staticmethod
        def createBuzzerDrum():
            # return ThreadedInstrumentAdapter(BuzzerDrum())
            return BuzzerDrum()

        @staticmethod
        def createPrinter():
            return Printer()

        @staticmethod
        def createLedLighter():
            # return ThreadedInstrumentAdapter(LedLighter())
            return LedLighter()

    def createDefaultInstrument(self):
        return RP2040Factory.Instrument.createBuzzerDrum()

    def createDefaultController(self):
        return EmptyAfronomController()
