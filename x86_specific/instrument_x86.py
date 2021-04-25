from instruments import AbstractInstrument
from interfaces.platforms import X86Platform
from playsound import playsound


class BuzzerDrum(AbstractInstrument, X86Platform):

    FREQ_NORMAL = 500
    FREQ_ACCENT = 800
    # VOLUME = 150
    BEEP_LENGTH = 0.2

    def __init__(self):
        super().__init__()

    def playNormal(self, note):
        playsound("resources\\beep-normal.wav")
        return self.BEEP_LENGTH

    def playAccent(self, note):
        playsound("resources\\beep-accent.wav")
        return self.BEEP_LENGTH


if __name__ == "__main__":
    BuzzerDrum().playNormal("")
    BuzzerDrum().playNormal("")
    BuzzerDrum().playNormal("")
    BuzzerDrum().playNormal("")
