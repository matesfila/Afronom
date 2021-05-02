from machine import Pin

from controllers import AbstractButtonController, AbstractAfronomController
from interfaces.platforms import M5StackPlatform


class M5StackButton(AbstractButtonController, M5StackPlatform):

    gpioPort = None

    def __init__(self, gpioPort):
        self.gpioPort = gpioPort

    def buttonEvent(self, value):
        # print(value)
        if value is 0:
            if self.onKeyDownEvent is not None:
                self.onKeyDownEvent()
        elif value is 1:
            if self.onKeyUpEvent is not None:
                self.onKeyUpEvent()

    def install_irq(self, gpioNum):
        # print("installing irq")
        p = Pin(gpioNum, Pin.IN, Pin.PULL_UP)
        p.irq(lambda p: self.buttonEvent(p.value()), Pin.IRQ_FALLING | Pin.IRQ_RISING)
        # p.irq(lambda p: print("{}, value = {}".format(p, p.value())), Pin.IRQ_FALLING | Pin.IRQ_RISING)

    def startMonitoring(self):
        self.install_irq(self.gpioPort)
        return self


class AfronomOneButtonController(AbstractAfronomController):

    def onButtonDown(self):
        # self.speedUpEvent()
        # self.slowDownEvent()
        # self.togglePlayEvent()
        print("button press")

    def onButtonUp(self):
        pass

    def initialize(self):
        # gpio port pre m5stick je 35
        M5StackButton(35) \
            .withKeyDownEvent(self.onButtonDown) \
            .withKeyUpEvent(self.onButtonUp) \
            .startMonitoring()
        return self


# AfronomOneButtonController().initialize()
