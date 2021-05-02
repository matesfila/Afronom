from factories import AbstractAfronomFactory
from instruments import ThreadedInstrumentAdapter, Printer
from interfaces.platforms import X86Platform
from x86_specific.hwcontrollers_x86 import AfronomKeyboardController
from x86_specific.instrument_x86 import BuzzerDrum


class X86Factory(AbstractAfronomFactory, X86Platform):

    class Instrument:

        @staticmethod
        def createPrinter():
            return Printer()

        @staticmethod
        def createBuzzerDrum():
            return ThreadedInstrumentAdapter(BuzzerDrum())

    def createDefaultInstrument(self):
        return X86Factory.Instrument.createPrinter()

    def createDefaultController(self):
        return AfronomKeyboardController()
