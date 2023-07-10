import pygame
from constants import *
from options import Options

options = Options()


# La clase `Bullet` representa un objeto de bala en un juego, con métodos para actualizar su posición,
# verificar colisiones con enemigos, el personaje del jugador y bloques, y manejar las consecuencias
# de esas colisiones.
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, facing_right, owner):
        super().__init__()
        self.original_image = pygame.image.load("assets\character/bullet.png")
        self.image = pygame.transform.scale(self.original_image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x  # Posición inicial en el eje x
        self.rect.y = y  # Posición inicial en el eje y
        self.speed = 10  # Velocidad de la bala
        self.direction = 1 if facing_right else -1  # Dirección de la bala
        self.owner = owner  # Dueño de la bala

    def update(self, enemies, hero, blocks, options):
        """
        La función actualiza la posición de un sprite y verifica las colisiones con los enemigos, el
        héroe y los bloques.

        :parametro enemies: El parámetro "enemigos" es un grupo de sprites que contiene todos los sprites
        enemigos del juego
        :parametro hero: El parámetro "héroe" representa el personaje del jugador en el juego. Es una
        instancia de una clase que contiene información sobre la posición, la puntuación y la salud del
        héroe
        :parametro blocks: El parámetro "bloques" es un grupo de sprites que contiene todos los bloques del
        juego. Estos bloques son objetos con los que el jugador y los enemigos pueden chocar
        :parametro options: El parámetro "opciones" es un objeto que contiene varias configuraciones y
        opciones para el juego. Es probable que incluya cosas como la configuración de sonido, la
        dificultad del juego y otras características personalizables
        """
        self.rect.x += self.speed * self.direction

        hit_list = pygame.sprite.spritecollide(self, enemies, False)
        for enemy in hit_list:
            if (
                "enemy" != self.owner
            ):  # Verifica si el enemigo es diferente al propietario
                result = enemy.die(options)
                if result:
                    hero.score += enemy.value
                self.kill()

        if self.direction > 0:
            if not pygame.sprite.spritecollide(self, [hero], False):
                hit_list = pygame.sprite.spritecollide(self, blocks, False)
                for block in hit_list:
                    self.kill()
        else:
            if pygame.sprite.collide_rect(self, hero):
                if options.sound_on:
                    options.play_sound(HURT_SOUND)
                hero.hearts -= 1
                self.kill()

        hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in hit_list:
            self.kill()
