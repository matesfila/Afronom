from afronom import AfronomImpl
from x86_specific.factory_x86 import X86Factory

"""
Hlavný spustiteľný skript pre windows/linux.
"""
if __name__ == "__main__":
    AfronomImpl(X86Factory())
