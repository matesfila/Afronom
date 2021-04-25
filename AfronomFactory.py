from hwcontrollers import AfronomController
from instrument import Printer
from rp2040_specific.factory_rp2040 import RP2040Factory
from sequencer import Sequencer_sync
from settings import Settings


class AfronomFactory:

    @staticmethod
    def createSettings():
        return Settings().load()

    @staticmethod
    def createSequencer():
        return Sequencer_sync()

    @staticmethod
    def createDefaultInstrument():
        return RP2040Factory.Instrument.createBuzzerDrum()

    @staticmethod
    def createDefaultController():
        return AfronomController()
