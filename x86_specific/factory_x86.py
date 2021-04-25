from instruments import ThreadedInstrumentAdapter, Printer
from interfaces import AfronomFactory
from x86_specific.instrument_x86 import BuzzerDrum


class X86Factory(AfronomFactory):

    class Instrument:

        @staticmethod
        def createPrinter():
            return Printer()

        @staticmethod
        def createBuzzerDrum():
            return ThreadedInstrumentAdapter(BuzzerDrum())
