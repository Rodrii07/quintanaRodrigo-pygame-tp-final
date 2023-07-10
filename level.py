import pygame
import json
from constants import *
from options import *
from items import Block, Coin, OneUp, Heart, Flag
from enemy import Enemy, Alien, Monster, Boss
from images import *

# La clase Level representa un nivel en un juego y contiene información sobre los bloques, los
# enemigos, las monedas, los potenciadores y el fondo del nivel.


class Level:
    def __init__(self, file_path):
        self.starting_blocks = []

        self.starting_enemies = []

        self.starting_coins = []

        self.starting_powerups = []

        self.starting_flag = []

        self.blocks = pygame.sprite.Group()

        self.enemies = pygame.sprite.Group()

        self.coins = pygame.sprite.Group()

        self.powerups = pygame.sprite.Group()

        self.flag = pygame.sprite.Group()

        self.active_sprites = pygame.sprite.Group()

        self.inactive_sprites = pygame.sprite.Group()

        with open(file_path, "r") as f:
            data = f.read()

        map_data = json.loads(data)

        self.width = map_data["width"] * GRID_SIZE

        self.height = map_data["height"] * GRID_SIZE

        self.start_x = map_data["start"][0] * GRID_SIZE

        self.start_y = map_data["start"][1] * GRID_SIZE

        for item in map_data["blocks"]:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            img = block_images[item[2]]

            self.starting_blocks.append(Block(x, y, img))

        for item in map_data["aliens"]:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_enemies.append(Alien(x, y, alien_images))

        for item in map_data["monsters"]:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            self.starting_enemies.append(Monster(x, y, monster_images))

        if map_data["name"] == "World 3":
            for item in map_data["boss"]:
                x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

                self.starting_enemies.append(Boss(x, y, boss_images, 15))

        for item in map_data["coins"]:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            self.starting_coins.append(Coin(x, y, coin_img))

        for item in map_data["oneups"]:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            self.starting_powerups.append(OneUp(x, y, oneup_img))

        for item in map_data["hearts"]:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            self.starting_powerups.append(Heart(x, y, heart_img))

        for i, item in enumerate(map_data["flag"]):
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            if i == 0:
                img = flag_img

            self.starting_flag.append(Flag(x, y, img))

        self.background_layer = pygame.Surface(
            [self.width, self.height], pygame.SRCALPHA, 32
        )

        self.scenery_layer = pygame.Surface(
            [self.width, self.height], pygame.SRCALPHA, 32
        )

        self.inactive_layer = pygame.Surface(
            [self.width, self.height], pygame.SRCALPHA, 32
        )

        self.active_layer = pygame.Surface(
            [self.width, self.height], pygame.SRCALPHA, 32
        )

        if map_data["background-color"] != "":
            self.background_layer.fill(map_data["background-color"])

        if map_data["background-img"] != "":
            background_img = pygame.image.load(
                map_data["background-img"]
            ).convert_alpha()

            if map_data["background-fill-y"]:
                h = background_img.get_height()

                w = int(background_img.get_width() * HEIGHT / h)

                background_img = pygame.transform.scale(background_img, (w, HEIGHT))

            if "top" in map_data["background-position"]:
                start_y = 0

            elif "bottom" in map_data["background-position"]:
                start_y = self.height - background_img.get_height()

            if map_data["background-repeat-x"]:
                for x in range(0, self.width, background_img.get_width()):
                    self.background_layer.blit(background_img, [x, start_y])

            else:
                self.background_layer.blit(background_img, [0, start_y])

        if map_data["scenery-img"] != "":
            scenery_img = pygame.image.load(map_data["scenery-img"]).convert_alpha()

            if map_data["scenery-fill-y"]:
                h = scenery_img.get_height()

                w = int(scenery_img.get_width() * HEIGHT / h)

                scenery_img = pygame.transform.scale(scenery_img, (w, HEIGHT))

            if "top" in map_data["scenery-position"]:
                start_y = 0

            elif "bottom" in map_data["scenery-position"]:
                start_y = self.height - scenery_img.get_height()

            if map_data["scenery-repeat-x"]:
                for x in range(0, self.width, scenery_img.get_width()):
                    self.scenery_layer.blit(scenery_img, [x, start_y])

            else:
                self.scenery_layer.blit(scenery_img, [0, start_y])

        pygame.mixer.music.load(map_data["music"])

        self.gravity = map_data["gravity"]

        self.terminal_velocity = map_data["terminal-velocity"]

        self.completed = False

        self.blocks.add(self.starting_blocks)
        self.enemies.add(self.starting_enemies)
        self.coins.add(self.starting_coins)

        self.powerups.add(self.starting_powerups)
        self.flag.add(self.starting_flag)

        self.active_sprites.add(self.coins, self.enemies, self.powerups)

        self.inactive_sprites.add(self.blocks, self.flag)

        for s in self.active_sprites:
            s.image.convert()

        for s in self.inactive_sprites:
            s.image.convert()

        self.inactive_sprites.draw(self.inactive_layer)

        self.background_layer.convert()

        self.scenery_layer.convert()

        self.inactive_layer.convert()

        self.active_layer.convert()

    def reset(self):
        self.enemies.add(self.starting_enemies)
        self.coins.add(self.starting_coins)

        self.powerups.add(self.starting_powerups)

        self.active_sprites.add(self.coins, self.enemies, self.powerups)

        for e in self.enemies:
            e.reset()
