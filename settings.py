import json
from interfaces import Om


class Settings(Om):

    DEFAULT_SETTINGS = {
        "Afronom": {
            "tempo": 150,
            "volume": 400,
            "rhythm": "X.xx.xx.X.x.x.x."
        }
    }

    CONFIG_FILENAME = "settings.json"

    settingsData = None

    def __init__(self):
        pass

    def load(self):
        if not self.configFileExists():
            self.createDefaultConfigFile()
        f = open(self.CONFIG_FILENAME)
        self.settingsData = json.loads(f.read())
        f.close()
        return self

    def save(self):
        f = open(self.CONFIG_FILENAME, 'w')
        f.write(json.dumps(self.settingsData))
        f.close()
        return self

    def configFileExists(self):
        try:
            f = open(self.CONFIG_FILENAME, "r")
            f.close()
            return True
            # continue with the file.
        except OSError:  # open failed
            # handle the file open case
            return False

    def createDefaultConfigFile(self):
        f = open(self.CONFIG_FILENAME, 'w')
        f.write(json.dumps(self.DEFAULT_SETTINGS))
        f.close()
        return self


def test_settings():
    s = Settings()
    s.load()


if __name__ == "__main__":
    test_settings()
