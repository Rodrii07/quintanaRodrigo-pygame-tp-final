import pygame
from constants import *
from images import *

pygame.mixer.init()

# La clase Opciones administra la configuración de sonido y música en un juego y proporciona un método
# para mostrar e interactuar con el menú de opciones.


class Options:
    def __init__(self):
        """
        Maneja las opciones de sonido y música en un
        juego, lo que permite al usuario activar o desactivar el sonido y la música y mostrar las
        opciones en la pantalla.
        """
        self.sound_on = True
        self.music_on = True

    def play_sound(self, sound, loops=0, maxtime=0, fade_ms=0):
        if self.sound_on:
            sound.play(loops, maxtime, fade_ms)
            # print("Sonido reproducido")
        else:
            sound.stop()
            # print("Sonido detenido")

    def play_music(self):
        if self.music_on:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

    def display_options(self, surface, sound_on=True, music_on=True):
        surface.fill(DARK_BLUE)

        # Función auxiliar para cambiar el estado de music_on al hacer clic
        def toggle_music():
            self.music_on = not self.music_on

        # Función auxiliar para cambiar el estado de sound_on al hacer clic
        def toggle_sound():
            self.sound_on = not self.sound_on
            # print("Sonido: ", self.sound_on)

        # Renderizado del texto para la música
        if self.music_on:
            music_text = "Música: ON"
        else:
            music_text = "Música: OFF"
        music_on_text = FONT_SM.render(music_text, 1, C_BLACK)
        music_on_rect = music_on_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        surface.blit(music_on_text, music_on_rect)

        # Renderizado del texto para el sonido
        if self.sound_on:
            sound_text = "Sonido: ON"
        else:
            sound_text = "Sonido: OFF"
        sound_on_text = FONT_SM.render(sound_text, 1, C_BLACK)
        sound_on_rect = sound_on_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 60))
        surface.blit(sound_on_text, sound_on_rect)

        # Renderizado del botón Atrás
        back_text = FONT_SM.render("Atrás", 1, C_BLACK)
        back_rect = back_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 120))
        surface.blit(back_text, back_rect)

        # Detección de eventos de clic en el texto
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_on_rect.collidepoint(event.pos):
                    toggle_music()
                elif sound_on_rect.collidepoint(event.pos):
                    toggle_sound()
                elif back_rect.collidepoint(event.pos):
                    return "back"
        return None
