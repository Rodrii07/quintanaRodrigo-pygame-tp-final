import pygame
from entity import Entity
from constants import *
from options import Options
from level import Level
from bullet import Bullet
from enemy import Enemy

options = Options()

# La clase Player representa al personaje principal de un juego y maneja sus movimientos, acciones e
# interacciones con el mundo del juego.


class Player(Entity):
    def __init__(self, images):
        super().__init__(0, 0, images["idle"])

        self.image_idle_right = images["idle"]
        self.image_idle_left = pygame.transform.flip(self.image_idle_right, 1, 0)
        self.images_run_right = images["run"]
        self.images_run_left = [
            pygame.transform.flip(img, 1, 0) for img in self.images_run_right
        ]
        self.image_jump_right = images["jump"]
        self.image_jump_left = [
            pygame.transform.flip(img, 1, 0) for img in self.image_jump_right
        ]
        self.image_attack_right = images["attack"]
        self.image_attack_left = [
            pygame.transform.flip(img, 1, 0) for img in self.image_attack_right
        ]

        self.running_images = self.images_run_right
        self.jumping_images = self.image_jump_right
        self.attacking_images = self.image_attack_right
        self.image_index = 0
        self.steps = 0

        self.speed = 5
        self.jump_power = 20

        self.vx = 0
        self.vy = 0
        self.facing_right = True
        self.on_ground = True
        self.attacking = False

        self.score = 0
        self.lives = 3
        self.hearts = 3
        self.max_hearts = 3
        self.invincibility = 0
        self.attack_delay = 500
        self.last_attack = pygame.time.get_ticks()
        self.bullets = pygame.sprite.Group()

    def move_left(self):
        """
        La función mueve un objeto hacia la izquierda estableciendo su velocidad horizontal en un valor
        negativo.
        """
        self.vx = -self.speed
        self.facing_right = False

    def move_right(self):
        """
        La función mueve un objeto hacia la derecha estableciendo su velocidad horizontal en un valor
        """
        self.vx = self.speed
        self.facing_right = True

    def stop(self):
        """
        La función establece la velocidad de un objeto en cero.
        """
        self.vx = 0

    def jump(self, blocks, options):
        """
        La función permite que un personaje salte cambiando su posición vertical y verificando
        colisiones con bloques.

        :parametro blocks, options:
        """
        self.rect.y += 1

        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        if len(hit_list) > 0:
            self.vy = -1 * self.jump_power
            if options.sound_on:
                options.play_sound(JUMP_SOUND)
        self.rect.y -= 1

    def attack(self, enemies, options):
        """
        La función "ataque" se utiliza para realizar una acción de ataque creando un objeto de viñeta y
        agregándolo al grupo de viñetas.

        :parametro enemies: El parámetro "enemigos" es una lista de objetos enemigos que el héroe puede
        atacar

        :parametro options: El parámetro "opciones" es un objeto que contiene varias configuraciones y
        opciones para el juego.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack >= self.attack_delay:
            if options.sound_on:
                options.play_sound(ATTACK_SOUND)

            bullet = Bullet(self.rect.x, self.rect.y, self.facing_right, owner="hero")
            self.bullets.add(bullet)

            self.last_attack = current_time

    def check_world_boundaries(self, level):
        """
        La función verifica si la posición del objeto está dentro de los límites del nivel y lo ajusta
        si es necesario.

        :parametro level: El parámetro "level" es un objeto que contiene información sobre el nivel actual
        """
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > level.width:
            self.rect.right = level.width

    def move_and_process_blocks(self, blocks):
        """
        La función mueve un sprite y verifica las colisiones con los bloques, ajustando la posición y la
        velocidad del sprite en consecuencia.

        :parametro blocks:
        """
        self.rect.x += self.vx
        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.vx = 0
            elif self.vx < 0:
                self.rect.left = block.rect.right
                self.vx = 0

        self.on_ground = False
        self.rect.y += self.vy + 1
        hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in hit_list:
            if self.vy > 0:
                self.rect.bottom = block.rect.top
                self.vy = 0
                self.on_ground = True
            elif self.vy < 0:
                self.rect.top = block.rect.bottom
                self.vy = 0

    def process_coins(self, coins, options):
        """
        La función procesa las colisiones entre el jugador y las monedas, actualizando la puntuación y
        reproduciendo un sonido si está habilitado.

        :parametro coins: El parámetro "monedas" es un grupo de sprites de pygame que representan las
        monedas en el juego
        :parametro options: El parámetro "opciones" es un objeto que contiene varias configuraciones y
        opciones para el juego.
        """
        hit_list = pygame.sprite.spritecollide(self, coins, True)

        for coin in hit_list:
            if options.sound_on:
                options.play_sound(COIN_SOUND)
            self.score += coin.value

    def process_enemies(self, enemies, options):
        """
        La función procesa las colisiones enemigas y reduce la salud del jugador si no es invencible.

        :parametro enemies, options:
        """
        hit_list = pygame.sprite.spritecollide(self, enemies, False)

        if len(hit_list) > 0 and self.invincibility == 0:
            if options.sound_on:
                options.play_sound(HURT_SOUND)
            self.hearts -= 1
            self.invincibility = int(0.75 * FPS)

    def process_powerups(self, powerups, options):
        """
        La función procesa los potenciadores comprobando si hay colisiones con el jugador y aplicando el
        efecto del potenciador.

        :parametro powerups, options:
        """
        hit_list = pygame.sprite.spritecollide(self, powerups, True)

        for p in hit_list:
            if options.sound_on:
                options.play_sound(POWERUP_SOUND)
            p.apply(self)

    def check_flag(self, level, options):
        """
        La función verifica si el sprite del jugador choca con el sprite de la bandera y actualiza el
        estado de finalización del nivel en consecuencia.

        :parametro level, options:
        """
        hit_list = pygame.sprite.spritecollide(self, level.flag, False)

        if len(hit_list) > 0:
            level.completed = True
            if options.sound_on:
                options.play_sound(LEVELUP_SOUND)

    def set_image(self):
        """
        La función establece la imagen de un personaje en función de su estado actual (atacando,
        corriendo, inactivo, saltando) y dirección (izquierda o derecha).
        """
        if self.attacking:
            if self.facing_right:
                self.attacking_images = self.image_attack_right

            else:
                self.attacking_images = self.image_attack_left

            self.steps = (self.steps + 1) % self.speed
            if self.steps == 0:
                self.image_index = (self.image_index + 1) % len(self.attacking_images)
                self.image = self.attacking_images[self.image_index]

        elif self.on_ground:
            if self.vx != 0:
                if self.facing_right:
                    self.running_images = self.images_run_right

                else:
                    self.running_images = self.images_run_left

                self.steps = (self.steps + 1) % self.speed
                if self.steps == 0:
                    self.image_index = (self.image_index + 1) % len(self.running_images)
                    self.image = self.running_images[self.image_index]

            else:
                if self.facing_right:
                    self.image = self.image_idle_right
                else:
                    self.image = self.image_idle_left

        else:
            if self.facing_right:
                self.jumping_images = self.image_jump_right
            else:
                self.jumping_images = self.image_jump_left

            self.steps = (self.steps + 1) % self.speed
            if self.steps == 0:
                self.image_index = (self.image_index + 1) % len(self.jumping_images)
                self.image = self.jumping_images[self.image_index]

    def die(self):
        """
        La función disminuye el número de vidas y reproduce un sonido si el jugador aún tiene vidas; de
        lo contrario, se reproduce un juego sobre el sonido.
        """
        self.lives -= 1

        if self.lives > 0:
            if options.sound_on:
                options.play_sound(DIE_SOUND)
        else:
            if options.sound_on:
                options.play_sound(
                    GAMEOVER_SOUND,
                )

    def respawn(self, level):
        self.rect.x = level.start_x
        self.rect.y = level.start_y
        self.hearts = self.max_hearts
        self.invincibility = 0
        self.facing_right = True

    def update(self, level, options):
        self.process_enemies(level.enemies, options)
        self.apply_gravity(level)
        self.move_and_process_blocks(level.blocks)
        self.check_world_boundaries(level)

        self.set_image()

        if self.hearts > 0:
            self.process_coins(level.coins, options)
            self.process_powerups(level.powerups, options)
            self.check_flag(level, options)

            if self.invincibility > 0:
                self.invincibility -= 1
        else:
            self.die()

        if self.attacking:
            self.attack(level.enemies, options)
