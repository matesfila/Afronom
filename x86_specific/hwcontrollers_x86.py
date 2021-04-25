import threading

from pynput.keyboard import Listener, Key

from controllers import AbstractButtonController, AfronomController
from interfaces.platforms import X86Platform


class PCKeyboard(AbstractButtonController, X86Platform):
    """
    Monitor štandardnej počítačovej klávesnice.
    Nebude fungovať v micropythone, dostupné iba pre PC.
    """

    """
    Pomocná množina, do ktorej sa ukladajú už stlačené klávesy, aby
    sa udalosť onKeyDownEvent vyvolala pre stále stlačenú klávesu iba raz
    (pretože držaním klávesy na klávesnici sa klávesa defaultne klávesa
    stláča opakovane).
    """
    pressedKeys = set()

    def on_press(self, key):
        if (self.onKeyDownEvent is not None) and (key not in self.pressedKeys):
            self.pressedKeys.add(key)
            return self.onKeyDownEvent(key)

    def on_release(self, key):
        if key in self.pressedKeys:
            self.pressedKeys.remove(key)
        if self.onKeyUpEvent is not None:
            return self.onKeyUpEvent(key)
        # if key == Key.esc:
        #     return False  # Stop listener

    def thread_function(self):
        super().startMonitoring()
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
        return self

    def startMonitoring(self):
        x = threading.Thread(target=self.thread_function)
        x.start()


class AfronomKeyboardController(AfronomController, X86Platform):

    def onKeyDown(self, key):
        if Key.up == key:
            # print("speeding up")
            self.speedUpEvent()
        elif Key.down == key:
            # print("slowing down")
            self.slowDownEvent()

    def initialize(self):
        PCKeyboard() \
            .withKeyDownEvent(lambda key: self.onKeyDown(key)) \
            .withKeyUpEvent(lambda key: self.onKeyDown(key)) \
            .startMonitoring()


if __name__ == "__main__":
    PCKeyboard() \
        .withKeyDownEvent(lambda key: print('{0} key down'.format(key))) \
        .withKeyUpEvent(lambda key: print('{0} key up'.format(key))) \
        .startMonitoring()
