import json


class ConfigFile:
    """ Class for reading and writing config file """

    PATH = 'config.json'

    def __init__(self):
        pass

    def write_checkpoint(self, site, checkpoint):
        dictionary = self.read_file()
        dictionary[site] = checkpoint

        json_object = json.dumps(dictionary, indent=4)

        with open(self.PATH, "w") as outfile:
            outfile.write(json_object)

        return

    def get_site_checkpoint(self, site):
        dictionary = self.read_file()

        if site in dictionary:
            if dictionary[site] == '':
                return None
            return dictionary[site]
        else:
            return None

    def read_file(self):
        with open(self.PATH, 'r') as openfile:
            json_object = json.load(openfile)
        return json_object
