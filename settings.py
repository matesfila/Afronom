import yaml
from yaml import SafeLoader
from interfaces import Om


class Settings(Om):

    DEFAULT_SETTINGS = {
        "Afronom": {
            "tempo": 100,
            "volume": 400,
            "rhythm": "X.xx.xx.X.x.x.x."
        }
    }

    CONFIG_FILENAME = "settings.yaml"

    settingsData = None

    def __init__(self):
        pass

    def load(self):
        f = open(self.CONFIG_FILENAME)
        self.settingsData = yaml.load(f.read(), Loader=SafeLoader)
        f.close()
        return self

    def save(self):
        f = open(self.CONFIG_FILENAME, 'w')
        f.write(yaml.dump(self.settingsData))
        f.close()
        return self

    def generateDefaults(self):
        f = open("default-settings.yaml", 'w')
        f.write(yaml.dump(self.DEFAULT_SETTINGS))
        f.close()
        return self


def test_settings():
    s = Settings()
    s.generateDefaults()
    s.load()


if __name__ == "__main__":
    test_settings()
