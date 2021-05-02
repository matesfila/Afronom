from afronom import AfronomImpl
from rp2040_specific.factory_rp2040 import RP2040Factory

"""
Hlavný spustiteľný skript pre Raspberry PI Pico zariadenia.
"""
if __name__ == "__main__":
    AfronomImpl(RP2040Factory())
