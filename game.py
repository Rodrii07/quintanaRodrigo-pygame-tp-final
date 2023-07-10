import json

import pygame
import sys

from constants import *
from options import Options
from player import Player
from enemy import Enemy, Alien, Monster, Boss
from entity import Entity
from items import Coin, Heart, Flag, OneUp, Block
from level import Level
from images import *
from bullet import Bullet
from text import Text

pygame.init()

# Niveles del juego
levels = ["levels/world-1.json", "levels/world-2.json", "levels/world-3.json"]

# La clase Game representa el ciclo principal del juego y maneja la lógica del juego, incluido el
# movimiento del jugador, el comportamiento del enemigo, la progresión de nivel y la entrada del
# usuario.


class Game:
    SPLASH = 0
    START = 1
    PLAYING = 2
    PAUSED = 3
    LEVEL_COMPLETED = 4
    GAME_OVER = 5
    VICTORY = 6
    OPTIONS = 7
    SELECT_LEVEL = 8

    def __init__(self):
        """
        Esta función inicializa varios atributos y objetos para un juego.
        """
        self.window = pygame.display.set_mode([WIDTH, HEIGHT])

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.done = False

        self.bullets = pygame.sprite.Group()

        self.hero_attacking = False

        self.reset()

        self.options = Options()

        self.text = Text()

    def start(self):
        """
        La función de inicio inicializa el nivel y reaparece al héroe.
        """
        self.level = Level(levels[self.current_level])

        self.level.reset()

        self.hero.respawn(self.level)

    def advance(self):
        """
        La función "avanzar" aumenta el nivel actual en 1, inicia el juego y establece el escenario en
        "START".
        """
        self.current_level += 1

        self.start()

        self.stage = Game.START

    def reset(self):
        """
        La función "restablecer" restablece el juego inicializando al héroe, configurando el nivel
        actual en 0, iniciando el juego y configurando el escenario en SPLASH.
        """
        self.hero = Player(hero_images)

        self.current_level = 0

        self.start()

        self.stage = Game.SPLASH

    def process_events(self):
        """
        La función "process_events" maneja varios eventos, como salir del juego, presionar teclas para
        acciones de juego, hacer clic con el mouse para opciones de menú y soltar teclas para reiniciar
        el juego.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            elif event.type == pygame.KEYDOWN:
                if self.stage == Game.START:
                    self.stage = Game.PLAYING

                    self.options.play_music()

                elif self.stage == Game.PAUSED:
                    if event.key == PAUSE:
                        self.stage = Game.PLAYING

                elif self.stage == Game.PLAYING:
                    if event.key == JUMP:
                        self.hero.jump(self.level.blocks, self.options)

                    if event.key == pygame.K_a:
                        self.hero.attacking = True

                    if event.key == PAUSE:
                        self.stage = Game.PAUSED

            elif self.stage == Game.SPLASH or self.stage == Game.PAUSED:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos

                    # Comprueba si se hizo clic en el botón "JUGAR"

                    play_button_x = WIDTH / 2 - FONT_MD.size("JUGAR")[0] / 2

                    play_button_y = HEIGHT / 2 - FONT_MD.size("JUGAR")[1] / 2

                    play_button_width = FONT_MD.size("JUGAR")[0]

                    play_button_height = FONT_MD.size("JUGAR")[1]

                    if (
                        play_button_x <= mouse_x <= play_button_x + play_button_width
                        and play_button_y
                        <= mouse_y
                        <= play_button_y + play_button_height
                    ):
                        self.stage = Game.START

                    # Comprueba si se hizo clic en el botón "OPCIONES"

                    options_button_x = WIDTH / 2 - FONT_MD.size("OPCIONES")[0] / 2

                    options_button_y = HEIGHT / 2 + FONT_MD.size("JUGAR")[1] + 20

                    options_button_width = FONT_MD.size("OPCIONES")[0]

                    options_button_height = FONT_MD.size("OPCIONES")[1]

                    if (
                        options_button_x
                        <= mouse_x
                        <= options_button_x + options_button_width
                        and options_button_y
                        <= mouse_y
                        <= options_button_y + options_button_height
                    ):
                        self.stage = Game.OPTIONS

                    # Comprueba si se hizo clic en el botón "SELECCIONAR NIVEL"

                    stats_button_x = (
                        WIDTH / 2 - FONT_MD.size("SELECCIONAR NIVEL")[0] / 2
                    )

                    stats_button_y = HEIGHT / 2 + 2 * FONT_MD.size("JUGAR")[1] + 40

                    stats_button_width = FONT_MD.size("SELECCIONAR NIVEL")[0]

                    stats_button_height = FONT_MD.size("SELECCIONAR NIVEL")[1]

                    if (
                        stats_button_x <= mouse_x <= stats_button_x + stats_button_width
                        and stats_button_y
                        <= mouse_y
                        <= stats_button_y + stats_button_height
                    ):
                        self.stage = Game.SELECT_LEVEL

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.hero.attacking = False

                elif self.stage == Game.VICTORY or self.stage == Game.GAME_OVER:
                    if event.key == pygame.K_r:
                        self.reset()

            elif self.stage == Game.LEVEL_COMPLETED:
                self.advance()

        pressed = pygame.key.get_pressed()

        if self.stage == Game.PLAYING:
            if pressed[LEFT]:
                self.hero.move_left()

            elif pressed[RIGHT]:
                self.hero.move_right()

            else:
                self.hero.stop()

    def update(self):
        """
        La función actualiza el estado del juego actualizando el héroe, los enemigos, las balas y
        verificando la finalización del nivel, el fin del juego y la reaparición del héroe.
        """
        if self.stage == Game.PLAYING:
            self.hero.update(self.level, self.options)

            self.level.enemies.update(self.level, self.hero, self.bullets)

            self.hero.bullets.update(
                self.level.enemies, self.hero, self.level.blocks, self.options
            )

            for enemy in self.level.enemies:
                enemy.bullets.update(
                    [self.hero], self.hero, self.level.blocks, self.options
                )

        if self.level.completed:
            if self.current_level < len(levels) - 1:
                self.stage = Game.LEVEL_COMPLETED

            else:
                self.stage = Game.VICTORY

            pygame.mixer.music.stop()

        elif self.hero.lives == 0:
            self.stage = Game.GAME_OVER

            pygame.mixer.music.stop()

        elif self.hero.hearts == 0:
            self.level.reset()

            self.hero.respawn(self.level)

    def calculate_offset(self):
        """
        La función calcula el desplazamiento horizontal necesario para centrar al héroe en la pantalla.
        :return: el valor de `x` y 0 como una tupla.
        """
        x = -1 * self.hero.rect.centerx + WIDTH / 2

        if self.hero.rect.centerx < WIDTH / 2:
            x = 0

        elif self.hero.rect.centerx > self.level.width - WIDTH / 2:
            x = -1 * self.level.width + WIDTH

        return x, 0

    def draw(self):
        """
        La función 'dibujar' es responsable de representar varios elementos del juego en la pantalla.
        """
        offset_x, offset_y = self.calculate_offset()

        self.level.active_layer.fill(TRANSPARENT)

        self.level.active_sprites.draw(self.level.active_layer)

        if self.hero.invincibility % 3 < 2:
            self.level.active_layer.blit(
                self.hero.image, [self.hero.rect.x, self.hero.rect.y]
            )

        self.window.blit(self.level.background_layer, [offset_x / 3, offset_y])

        self.window.blit(self.level.scenery_layer, [offset_x / 2, offset_y])

        self.window.blit(self.level.inactive_layer, [offset_x, offset_y])

        self.window.blit(self.level.active_layer, [offset_x, offset_y])

        self.text.display_stats(self.window, self.hero)

        for bullet in self.hero.bullets:
            self.window.blit(
                bullet.image, [bullet.rect.x + offset_x, bullet.rect.y + 20]
            )

        for enemy in self.level.enemies:
            for bullet in enemy.bullets:
                self.window.blit(
                    bullet.image, [bullet.rect.x + offset_x, bullet.rect.y + 20]
                )

        if self.stage == Game.SPLASH:
            self.text.display_splash(self.window)

        elif self.stage == Game.OPTIONS:
            result = self.options.display_options(self.window)

            if result == "back":
                self.stage = Game.SPLASH

        elif self.stage == Game.SELECT_LEVEL:
            result = self.text.display_select_level(self.window)

            if result == 1:
                self.level = Level(levels[0])
                self.stage = Game.START

            elif result == 2:
                self.level = Level(levels[1])
                self.stage = Game.START

            elif result == 3:
                self.level = Level(levels[2])
                self.stage = Game.START

        elif self.stage == Game.START:
            self.text.display_message(
                self.window, "Listo?", "Presiona cualquier tecla para continuar."
            )

        elif self.stage == Game.PAUSED:
            self.text.display_splash(self.window)

        elif self.stage == Game.LEVEL_COMPLETED:
            self.text.display_message(
                self.window,
                "Nivel completado!",
                "Presione cualquier tecla para continuar.",
            )

        elif self.stage == Game.VICTORY:
            self.text.display_message(
                self.window, "Ganaste!", "Apreta 'R' para continuar."
            )

        elif self.stage == Game.GAME_OVER:
            self.text.display_message(
                self.window, "Perdiste.", "Apreta 'R' para continuar."
            )

        pygame.display.flip()

    def loop(self):
        """
        La función `loop` ejecuta un bucle de juego que procesa eventos continuamente, actualiza el
        estado del juego, dibuja el juego y controla la velocidad de fotogramas.
        """
        while not self.done:
            self.process_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)


# El código `if __name__ == "__main__":` es un modismo común de Python que verifica si el script
# actual se está ejecutando como el módulo principal. Esto permite que el código dentro del bloque
# `if` se ejecute solo cuando el script se ejecuta directamente, y no cuando otro script lo importa
# como un módulo.
if __name__ == "__main__":
    game = Game()

    game.start()

    game.loop()

    pygame.quit()

    sys.exit()
