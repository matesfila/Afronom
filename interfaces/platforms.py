class Platform:
    """
    Základný interface pre platformu. Platforma je zariadenie, na ktorom má bežať Afronom. Môže to byť napr x86
    procesor, alebo raspberry pico tj rp2040 mikroprocesor.
    Pokiaľ trieda dedí od Platform, resp niektorého potomka, indikuje to, s akou platformou je daná trieda
    kompatibilná.
    """
    pass


class AnyPlatform(Platform):
    """
    Beží na ľubovoľnej platforme.
    """
    pass


class X86Platform(Platform):
    """
    Beží na windowse resp X86 procesore.
    """
    pass


class PikoPlatform(Platform):
    """
    Beží na Raspberry PI Pico.
    """
    pass
