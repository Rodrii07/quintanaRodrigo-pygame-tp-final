import pygame


# La clase 'Entidad' representa un objeto en un juego con atributos de posición, imagen, velocidad y
# métodos para aplicar la gravedad.
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vy = 0
        self.vx = 0

    def apply_gravity(self, level):
        """
        La función aplica la gravedad a la velocidad vertical de un objeto y la limita a la velocidad
        terminal del nivel.

        :param level:
        """
        self.vy += level.gravity
        self.vy = min(self.vy, level.terminal_velocity)
