from interfaces.platforms import AnyPlatform


class HwButton(AnyPlatform):
    """
    Abstraktná trieda pre monitorovanie eventov hardwarových controllerov.
    """

    onKeyDownEvent = None
    onKeyUpEvent = None

    def startMonitoring(self):
        pass

    def withKeyDownEvent(self, event):
        self.onKeyDownEvent = event
        return self

    def withKeyUpEvent(self, event):
        self.onKeyUpEvent = event
        return self


class AfronomController(AnyPlatform):

    speedUpEvent = None
    slowDownEvent = None

    def initialize(self):
        pass

    def withSpeedUpEvent(self, event):
        self.speedUpEvent = event
        return self

    def withSlowDownEvent(self, event):
        self.slowDownEvent = event
        return self
