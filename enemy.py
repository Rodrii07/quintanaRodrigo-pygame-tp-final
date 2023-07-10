import pygame
from entity import Entity
from constants import *
from options import Options
from bullet import Bullet

options = Options()

# El código define clases para diferentes tipos de enemigos en un juego, incluidos Alien, Monster y
# Boss, cada uno con sus propios movimientos y comportamientos de disparo.


class Enemy(Entity):
    def __init__(self, x, y, images, lives=3):
        super().__init__(x, y, images[0])

        self.images_left = images

        self.images_right = [pygame.transform.flip(img, 1, 0) for img in images]

        self.current_images = self.images_left

        self.image_index = 0

        self.steps = 0
        self.lives = lives

        self.value = 15

        self.shoot_delay = 4000

        self.last_shot = 0

        self.bullets = pygame.sprite.Group()

    def reverse(self):
        """
        Define una clase con varios métodos para controlar el movimiento y el
        comportamiento de un personaje en un juego.
        """
        self.vx *= -1

        if self.vx < 0:
            self.current_images = self.images_right

        else:
            self.current_images = self.images_left

        self.image = self.current_images[self.image_index]

    def die(self, options):
        """
        La función disminuye el número de vidas, reproduce un sonido si el número de vidas sigue siendo
        mayor que 0, juega un juego sobre el sonido y mata el objeto si el número de vidas es menor o
        igual a 0, y devuelve True.

        :parametro options: El parámetro "opciones" es un objeto que contiene varios ajustes y
        configuraciones para el juego.
        :return: Verdadero.
        """
        self.lives -= 1

        if self.lives > 0:
            if options.sound_on:
                options.play_sound(HURT_SOUND)

        elif self.lives <= 0:
            if options.sound_on:
                options.play_sound(GAMEOVER_SOUND)

            self.kill()

            return True

    def check_world_boundaries(self, level):
        """
        La función comprueba si la posición del objeto está fuera de los límites izquierdo o derecho del
        nivel y lo ajusta en consecuencia.

        :parametro level: El parámetro "nivel" es una estructura de datos que
        representa los límites o las dimensiones del mundo del juego. Podría contener información como
        el ancho y el alto del nivel, así como cualquier otra propiedad o método relevante necesario
        para la lógica del juego
        """
        if self.rect.left < 0:
            self.rect.left = 0
            self.reverse()

        elif self.rect.right > level.width:
            self.rect.right = level.width
            self.reverse()

    def move_and_process_blocks(self, blocks):
        """
        La función mueve el objeto horizontal y verticalmente y comprueba si hay colisiones con bloques
        en ambas direcciones.

        :parametro blocks: El parámetro "bloques" es un grupo de objetos sprites que representan los bloques
        del juego. Estos bloques se utilizan para detectar colisiones y determinar el movimiento del
        personaje del jugador
        """
        self.rect.x += self.vx

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.reverse()

            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.reverse()

        self.rect.y += self.vy

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vy > 0:
                self.rect.bottom = block.rect.top

                self.vy = 0

            elif self.vy < 0:
                self.rect.top = block.rect.bottom

                self.vy = 0

    def set_images(self):
        """
        La función establece la imagen de un objeto en función de su índice de imagen actual e
        incrementa el índice de imagen y el contador de pasos.
        """
        if self.steps == 0:
            self.image = self.current_images[self.image_index]

            self.image_index = (self.image_index + 1) % len(self.current_images)

        self.steps = (self.steps + 1) % 20

    def is_near(self, hero):
        """
        La función comprueba si la distancia entre el objeto propio y el objeto principal es inferior al
        doble del ancho.

        :parametro hero: El parámetro "héroe" es un objeto que representa al personaje héroe en el juego.
        :return: un valor booleano que indica si la distancia entre las coordenadas x del rect del
        objeto self y el rect del objeto hero es menor que 2 veces el valor de la variable WIDTH.
        """
        return abs(self.rect.x - hero.rect.x) < 2 * WIDTH

    def update(self, level, hero, bullets):
        """
        La función actualiza la posición y el comportamiento de un personaje en un juego según el nivel,
        el héroe y las balas.

        :parametro level, hero, bullets: ya explicados en otras funciones.
        """
        if self.is_near(hero):
            self.apply_gravity(level)

            self.move_and_process_blocks(level.blocks)

            self.check_world_boundaries(level)
            self.set_images()

    def reset(self):
        """
        La función restablece la posición, la velocidad, las imágenes y los pasos de un objeto.
        """
        self.rect.x = self.start_x
        self.rect.y = self.start_y

        self.vx = self.start_vx
        self.vy = self.start_vy

        self.current_images = self.images_left

        self.image = self.current_images[0]

        self.steps = 0


class Alien(Enemy):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.start_x = x
        self.start_y = y

        self.start_vx = 2

        self.start_vy = 0

        self.vx = self.start_vx
        self.vy = self.start_vy

    def shoot(self, bullets):
        """
        La función de disparar crea un nuevo objeto Bullet y lo agrega al grupo de balas.

        :parametro bullets: El parámetro "balas" es una colección o contenedor que contiene todas las balas
        del juego. Es probable que sea una estructura de datos como una lista o un conjunto
        """
        bullet = Bullet(self.rect.x, self.rect.y, facing_right=False, owner="enemy")

        self.bullets.add(bullet)

    def auto_shoot(self, hero, bullets):
        """
        La función `auto_shoot` comprueba si el enemigo está cerca del héroe y dispara balas si ha
        pasado suficiente tiempo desde el último disparo.

        :parametro hero, bullets:
        """
        if self.is_near(hero):
            current_time = pygame.time.get_ticks()

            if current_time - self.last_shot > self.shoot_delay:
                self.shoot(bullets)
                self.last_shot = current_time

    def update(self, level, hero, bullets):
        if self.is_near(hero):
            self.apply_gravity(level)

            self.move_and_process_blocks(level.blocks)

            self.check_world_boundaries(level)
            self.set_images()
            self.auto_shoot(hero, bullets)


# La clase Monstruo representa un tipo de enemigo que puede moverse e interactuar con bloques en un
# juego.
class Monster(Enemy):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.start_x = x
        self.start_y = y

        self.start_vx = -2

        self.start_vy = 0

        self.vx = self.start_vx
        self.vy = self.start_vy

    def move_and_process_blocks(self, blocks):
        reverse = False

        self.rect.x += self.vx

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.reverse()

            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.reverse()

        self.rect.y += self.vy + 1

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        reverse = True

        for block in hit_list:
            if self.vy >= 0:
                self.rect.bottom = block.rect.top

                self.vy = 0

                if self.vx > 0 and self.rect.right <= block.rect.right:
                    reverse = False

                elif self.vx < 0 and self.rect.left >= block.rect.left:
                    reverse = False

            elif self.vy < 0:
                self.rect.top = block.rect.bottom

                self.vy = 0

        if reverse:
            self.reverse()


# La clase 'Jefe' es una subclase de 'Enemigo' que se inicializa con posiciones de inicio, velocidades
# e imágenes específicas.
class Boss(Enemy):
    def __init__(self, x, y, images, lives):
        super().__init__(x, y, images, lives)

        self.start_x = x
        self.start_y = y

        self.start_vx = -2

        self.start_vy = 0

        self.vx = self.start_vx
        self.vy = self.start_vy
