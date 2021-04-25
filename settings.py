import json

from interfaces import Om


class Settings(Om):

    DEFAULT_SETTINGS = {
        "Afronom": {
            "tempo": 100,
            "volume": 400,
            "rhythm": "X.xx.xx.X.x.x.x."
        }
    }

    CONFIG_FILENAME = "afronom.cfg"

    settingsData = None

    def __init__(self):
        pass

    def load(self):
        f = open(self.CONFIG_FILENAME)
        self.settingsData = json.loads(f.read())
        f.close()
        return self

    def save(self):
        f = open(self.CONFIG_FILENAME, 'w')
        f.write(json.dumps(self.settingsData))
        f.close()
        return self

    def resetDefaults(self):
        f = open(self.CONFIG_FILENAME, 'w')
        f.write(json.dumps(self.DEFAULT_SETTINGS))
        f.close()
        return self


def test_settings():
    s = Settings()
    s.resetDefaults()
    s.load()


if __name__ == "__main__":
    test_settings()
