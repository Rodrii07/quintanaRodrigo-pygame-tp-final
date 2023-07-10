import pygame
from entity import Entity

# El código define varias clases para diferentes tipos de entidades en un juego, como bloques,
# monedas, potenciadores y banderas.


class Block(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)


class Coin(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self.value = 5


class OneUp(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character):
        character.lives += 1


class Heart(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character):
        character.hearts += 1
        character.hearts = max(character.hearts, character.max_hearts)


class Flag(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
