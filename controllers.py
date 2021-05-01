from interfaces import ButtonController, Om, Controller


class AbstractButtonController(ButtonController):
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


class AbstractAfronomController(Controller):

    speedUpEvent = None
    slowDownEvent = None
    playEvent = None
    stopEvent = None
    togglePlayEvent = None

    def initialize(self):
        return self

    def withSpeedUpEvent(self, event):
        self.speedUpEvent = event
        return self

    def withSlowDownEvent(self, event):
        self.slowDownEvent = event
        return self

    def withPlayEvent(self, event):
        self.playEvent = event
        return self

    def withStopEvent(self, event):
        self.stopEvent = event
        return self

    def withTogglePlayEvent(self, event):
        self.togglePlayEvent = event
        return self


class EmptyAfronomController(AbstractAfronomController):
    pass
