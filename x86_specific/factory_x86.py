from instrument import ThreadedInstrumentAdapter
from x86_specific.instrument_x86 import BuzzerDrum


class X86Factory:

    class Instrument:

        @staticmethod
        def createBuzzerDrum():
            return ThreadedInstrumentAdapter(BuzzerDrum())
