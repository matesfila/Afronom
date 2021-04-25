from instrument import ThreadedInstrumentAdapter, Printer
from rp2040_specific.instrument_rp2040 import LedLighter, BuzzerDrum


class RP2040Factory:

    class Instrument:

        @staticmethod
        def createBuzzerDrum():
            return ThreadedInstrumentAdapter(BuzzerDrum())

        @staticmethod
        def createPrinter():
            return Printer()

        @staticmethod
        def createLedLighter():
            return ThreadedInstrumentAdapter(LedLighter())
