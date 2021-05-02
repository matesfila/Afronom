from afronom import AfronomImpl
from m5stick_specific.factory_m5stick import M5StickFactory

"""
Hlavný spustiteľný skript pre M5Stick zariadenia.
"""
if __name__ == "__main__":
    AfronomImpl(M5StickFactory())
