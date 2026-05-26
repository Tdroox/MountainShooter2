from factory.entity_factory import EntityFactory

class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list = []

    def run(self):

        player = EntityFactory.get_entity("player")
        self.entity_list.append(player)