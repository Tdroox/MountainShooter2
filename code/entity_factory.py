from entities.player import Player
from entities.enemy import Enemy
from entities.background import Background

class EntityFactory:

    @staticmethod
    def get_entity(entity_type):

        if entity_type == "player":
            return Player("player", None, None)

        elif entity_type == "enemy":
            return Enemy("enemy", None, None)

        elif entity_type == "background":
            return Background("background", None, None)

        return None