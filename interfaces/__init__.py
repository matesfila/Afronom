class Om:
    """
    Om je základný interface, od ktorého dedia všetky ďalšie interfacy/triedy v programe Afronom.
    Z interface Om sa dá prehladne dostať ku každému prvku zdrojového kódu, tj k inštrumentom, controllerom,
    sequencerom a podobne.
    """
    pass


class Afronom(Om):
    def speedUp(self):
        pass

    def slowDown(self):
        pass

    def play(self):
        pass


class AfronomFactory(Om):
    pass


class Sequencer(Om):
    def withTempo(self, tempo):
        pass

    def withVolume(self, volume):
        pass

    def withInstruments(self, instruments):
        pass

    def speedUp(self):
        pass

    def slowDown(self):
        pass

    def playBar(self, bar):
        pass

    def playInLoop(self, bar):
        pass


class Instrument(Om):

    def playNormal(self, note):
        pass

    def playAccent(self, note):
        pass

    def onBarStart(self):
        pass

    def onBarEnd(self):
        pass

    def play(self, note):
        pass


class Controller(Om):
    pass


class ButtonController(Controller):
    def startMonitoring(self):
        pass

    def withKeyDownEvent(self, event):
        pass

    def withKeyUpEvent(self, event):
        pass
