import json


class Settings:

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
        self.load()

    def load(self):
        f = open(self.CONFIG_FILENAME)
        self.settingsData = json.loads(f.read())
        f.close()

    def save(self):
        f = open(self.CONFIG_FILENAME, 'w')
        f.write(json.dumps(self.settingsData))
        f.close()

    def resetDefaults(self):
        f = open(self.CONFIG_FILENAME, 'w')
        f.write(json.dumps(self.DEFAULT_SETTINGS))
        f.close()


def test_settings():
    s = Settings()
    s.resetDefaults()
    s.load()
