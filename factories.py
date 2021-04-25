from controllers import AfronomController
from interfaces import AfronomFactory
from sequencers import Sequencer_sync
from settings import Settings
from x86_specific.factory_x86 import X86Factory


class DefaultAfronomFactory(AfronomFactory):

    # nechal by som tu aj metodu createAfronom, avšak dochádze k chybe circular dependencies
    # @staticmethod
    # def createAfronom():
    #     return AfronomImpl()

    @staticmethod
    def createSettings():
        return Settings().load()

    @staticmethod
    def createSequencer():
        return Sequencer_sync()

    @staticmethod
    def createDefaultInstrument():
        return X86Factory.Instrument.createPrinter()

    @staticmethod
    def createDefaultController():
        return AfronomController()
