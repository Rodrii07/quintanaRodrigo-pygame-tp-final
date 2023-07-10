import pygame
from constants import *

# La clase Text en este código es responsable de mostrar varios elementos de texto en la superficie
# del juego.


class Text:
    def __init__(self):
        pass

    def display_splash(self, surface):
        """
        La función `display_splash` muestra una pantalla de inicio con botones para jugar, acceder a
        opciones y seleccionar un nivel.

        :parametro surface: El parámetro "superficie" es la superficie de pygame en la que se mostrará la
        pantalla de bienvenida
        """
        splash_text = FONT_LG.render(TITLE, 1, C_BLACK)
        play_button_text = FONT_MD.render("JUGAR", 1, C_BLACK)
        options_button_text = FONT_MD.render("OPCIONES", 1, C_BLACK)
        stats_button_text = FONT_MD.render("SELECCIONAR NIVEL", 1, C_BLACK)

        splash_x = WIDTH / 2 - splash_text.get_width() / 2
        splash_y = HEIGHT / 3 - splash_text.get_height() / 2

        play_button_x = WIDTH / 2 - play_button_text.get_width() / 2
        play_button_y = HEIGHT / 2 - play_button_text.get_height() / 2

        options_button_x = WIDTH / 2 - options_button_text.get_width() / 2
        options_button_y = HEIGHT / 2 + play_button_text.get_height() + 20

        stats_button_x = WIDTH / 2 - stats_button_text.get_width() / 2
        stats_button_y = HEIGHT / 2 + 2 * play_button_text.get_height() + 40

        surface.fill(DARK_BLUE)
        surface.blit(splash_text, (splash_x, splash_y))

        pygame.draw.rect(
            surface,
            DARK_BLUE,
            (
                play_button_x - 10,
                play_button_y - 10,
                play_button_text.get_width() + 20,
                play_button_text.get_height() + 20,
            ),
        )
        surface.blit(play_button_text, (play_button_x, play_button_y))

        pygame.draw.rect(
            surface,
            DARK_BLUE,
            (
                options_button_x - 10,
                options_button_y - 10,
                options_button_text.get_width() + 20,
                options_button_text.get_height() + 20,
            ),
        )
        surface.blit(options_button_text, (options_button_x, options_button_y))

        pygame.draw.rect(
            surface,
            DARK_BLUE,
            (
                stats_button_x - 10,
                stats_button_y - 10,
                stats_button_text.get_width() + 20,
                stats_button_text.get_height() + 20,
            ),
        )
        surface.blit(stats_button_text, (stats_button_x, stats_button_y))

    def display_message(self, surface, primary_text, secondary_text):
        """
        La función `display_message` toma una superficie, texto primario y texto secundario, y muestra
        el texto primario y secundario centrado en la superficie.

        :parametro surface: El parámetro "superficie" se refiere al objeto de superficie en el que desea
        mostrar el mensaje.
        :parametro primary_text: El parámetro texto_principal es una cadena que representa el mensaje que desea mostrar en la superficie
        :parametro secondary_text: cadena que representa el texto que
        se mostrará como mensaje secundario en la superficie
        """
        line1 = FONT_MD.render(primary_text, 1, C_BLACK)
        line2 = FONT_SM.render(secondary_text, 1, C_BLACK)

        x1 = WIDTH / 2 - line1.get_width() / 2
        y1 = HEIGHT / 3 - line1.get_height() / 2

        x2 = WIDTH / 2 - line2.get_width() / 2
        y2 = y1 + line1.get_height() + 16

        surface.blit(line1, (x1, y1))
        surface.blit(line2, (x2, y2))

    def display_stats(self, surface, hero):
        """
        La función "display_stats" toma una superficie y un objeto héroe, y muestra los corazones, las
        vidas y la puntuación del héroe en la superficie.

        :parametro surface: El parámetro "superficie" se refiere al objeto de superficie en el que desea
        mostrar las estadísticas.
        :parametro hero: El parámetro "héroe" es una instancia de una clase que representa al personaje del
        jugador en el juego.
        """
        hearts_text = FONT_SM.render("Corazones: " + str(hero.hearts), 1, WHITE)
        lives_text = FONT_SM.render("Vidas: " + str(hero.lives), 1, WHITE)
        score_text = FONT_SM.render("Puntaje: " + str(hero.score), 1, WHITE)

        surface.blit(score_text, (WIDTH - score_text.get_width() - 32, 32))
        surface.blit(hearts_text, (32, 32))
        surface.blit(lives_text, (32, 64))

    def display_select_level(self, surface):
        """
        La función `display_select_level` muestra tres niveles en la pantalla y devuelve el nivel
        seleccionado cuando el usuario hace clic en él.

        :parametro surface: El parámetro "superficie" es la superficie de pygame en la que se mostrará la
        pantalla de selección de nivel
        :return: el número de nivel seleccionado (1, 2 o 3) según el clic del mouse del usuario.
        """
        level_1_text = FONT_MD.render("Nivel 1", 1, C_BLACK)
        level_2_text = FONT_MD.render("Nivel 2", 1, C_BLACK)
        level_3_text = FONT_MD.render("Nivel 3", 1, C_BLACK)

        level_1_x = WIDTH / 2 - level_1_text.get_width() / 2
        level_1_y = HEIGHT / 3 - level_1_text.get_height() / 2

        level_2_x = WIDTH / 2 - level_2_text.get_width() / 2
        level_2_y = HEIGHT / 2 - level_2_text.get_height() / 2

        level_3_x = WIDTH / 2 - level_3_text.get_width() / 2
        level_3_y = HEIGHT / 2 + level_3_text.get_height() + 20

        surface.fill(DARK_BLUE)

        pygame.draw.rect(
            surface,
            DARK_BLUE,
            (
                level_1_x - 10,
                level_1_y - 10,
                level_1_text.get_width() + 20,
                level_1_text.get_height() + 20,
            ),
        )
        surface.blit(level_1_text, (level_1_x, level_1_y))

        pygame.draw.rect(
            surface,
            DARK_BLUE,
            (
                level_2_x - 10,
                level_2_y - 10,
                level_2_text.get_width() + 20,
                level_2_text.get_height() + 20,
            ),
        )
        surface.blit(level_2_text, (level_2_x, level_2_y))

        pygame.draw.rect(
            surface,
            DARK_BLUE,
            (
                level_3_x - 10,
                level_3_y - 10,
                level_3_text.get_width() + 20,
                level_3_text.get_height() + 20,
            ),
        )
        surface.blit(level_3_text, (level_3_x, level_3_y))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (
                        level_1_x
                        <= event.pos[0]
                        <= level_1_x + level_1_text.get_width()
                        and level_1_y
                        <= event.pos[1]
                        <= level_1_y + level_1_text.get_height()
                    ):
                        return 1
                    elif (
                        level_2_x
                        <= event.pos[0]
                        <= level_2_x + level_2_text.get_width()
                        and level_2_y
                        <= event.pos[1]
                        <= level_2_y + level_2_text.get_height()
                    ):
                        return 2
                    elif (
                        level_3_x
                        <= event.pos[0]
                        <= level_3_x + level_3_text.get_width()
                        and level_3_y
                        <= event.pos[1]
                        <= level_3_y + level_3_text.get_height()
                    ):
                        return 3
