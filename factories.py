from controllers import AbstractAfronomController
from interfaces import AfronomFactory
from sequencers import Sequencer_sync
from settings import Settings


class AbstractAfronomFactory(AfronomFactory):

    # nechal by som tu aj metodu createAfronom, avšak dochádze k chybe circular dependencies
    # @staticmethod
    # def createAfronom():
    #     return AfronomImpl()

    def createSettings(self):
        return Settings().load()

    def createSequencer(self):
        return Sequencer_sync()

    def createDefaultController(self):
        return AbstractAfronomController()
