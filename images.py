from constants import *


# Funciones de ayuda
def load_image(file_path, width=GRID_SIZE, height=GRID_SIZE):
    img = pygame.image.load(file_path)
    img = pygame.transform.scale(img, (width, height))

    return img


"""
    El código anterior define una función para cargar imágenes y luego carga varias imágenes para
    diferentes elementos del juego, como el personaje del jugador, bloques, monedas, enemigos y jefes.
    
    :parametro file_path: El parámetro `file_path` es una cadena que representa la ruta al archivo de imagen
    que desea cargar. Debe incluir la extensión del archivo (por ejemplo, ".png")
    :param width: El parámetro `width` se usa para especificar el ancho deseado de la imagen cuando se
    carga. Se utiliza en la función `load_image` para escalar la imagen al ancho especificado
    :parametro height: El parámetro `height` en la función `load_image` se usa para especificar la altura
    deseada de la imagen. Se establece en el valor de `GRID_SIZE` por defecto, que es una constante
    definida en el módulo `constants`
    :return: El código devuelve un diccionario llamado `hero_images` que contiene diferentes imágenes
    para el personaje héroe en diferentes estados, como correr, saltar, inactivo y atacando. También
    devuelve un diccionario llamado `block_images` que contiene diferentes imágenes para diferentes
    tipos de bloques en el juego. Además, devuelve imágenes de monedas, corazones, one-ups, banderas,
    monstruos, alienígenas y el personaje principal.
"""

# Imagenes
hero_walk1 = load_image("assets\character\WALK_000.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_walk2 = load_image("assets\character\WALK_001.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_walk3 = load_image("assets\character\WALK_002.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_walk4 = load_image("assets\character\WALK_003.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_walk5 = load_image("assets\character\WALK_004.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_walk6 = load_image("assets\character\WALK_005.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_walk7 = load_image("assets\character\WALK_006.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_jump1 = load_image("assets\character\JUMP_000.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_jump2 = load_image("assets\character\JUMP_001.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_jump3 = load_image("assets\character\JUMP_002.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_jump4 = load_image("assets\character\JUMP_003.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_jump5 = load_image("assets\character\JUMP_004.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_idle = load_image("assets\character\IDLE_000.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_shoot1 = load_image("assets\character\SHOOT_002.png", PLAYER_WIDTH, PLAYER_HEIGHT)
hero_shoot2 = load_image("assets\character\SHOOT_003.png", PLAYER_WIDTH, PLAYER_HEIGHT)

hero_images = {
    "run": [
        hero_walk1,
        hero_walk2,
        hero_walk3,
        hero_walk4,
        hero_walk5,
        hero_walk6,
        hero_walk7,
    ],
    "jump": [
        hero_jump1,
        hero_jump2,
        hero_jump3,
        hero_jump4,
        hero_jump5,
    ],
    "idle": hero_idle,
    "attack": [
        hero_shoot1,
        hero_shoot2,
    ],
}


block_images = {
    "TL": load_image("assets/tiles/top_left.png"),
    "TM": load_image("assets/tiles/top_middle.png"),
    "TR": load_image("assets/tiles/top_right.png"),
    "ER": load_image("assets/tiles/end_right.png"),
    "EL": load_image("assets/tiles/end_left.png"),
    "TP": load_image("assets/tiles/top.png"),
    "CN": load_image("assets/tiles/center.png"),
    "LF": load_image("assets/tiles/lone_float.png"),
    "SP": load_image("assets/tiles/special.png"),
}

coin_img = load_image("assets/items/coin.png")
heart_img = load_image("assets/items/wine_bottle.png")
oneup_img = load_image("assets/items/first_aid.png")
flag_img = load_image("assets/items/flag_1.png", FLAG_SIZE, FLAG_SIZE)


monster_img1 = load_image("assets\enemies\Enemywalk1.png")
monster_img2 = load_image("assets\enemies\Enemywalk2.png")
monster_img3 = load_image("assets\enemies\Enemywalk3.png")
monster_img4 = load_image("assets\enemies\Enemywalk4.png")
monster_img5 = load_image("assets\enemies\Enemywalk5.png")

monster_images = [monster_img1, monster_img2, monster_img3, monster_img4, monster_img5]

alien_img = load_image("assets\enemies/0.png")
alien_img2 = load_image("assets\enemies/1.png")
alien_img3 = load_image("assets\enemies/2.png")
alien_img4 = load_image("assets\enemies/3.png")
alien_img5 = load_image("assets\enemies/4.png")
alien_img6 = load_image("assets\enemies/5.png")
alien_img7 = load_image("assets\enemies/6.png")
alien_img8 = load_image("assets\enemies/7.png")


alien_images = [
    alien_img,
    alien_img2,
    alien_img3,
    alien_img4,
    alien_img5,
    alien_img6,
    alien_img7,
    alien_img8,
]

boss_img = load_image("assets\enemies/boss\Walk_000.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img2 = load_image("assets\enemies/boss\Walk_001.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img3 = load_image("assets\enemies/boss\Walk_002.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img4 = load_image("assets\enemies/boss\Walk_003.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img5 = load_image("assets\enemies/boss\Walk_004.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img6 = load_image("assets\enemies/boss\Walk_005.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img7 = load_image("assets\enemies/boss\Walk_006.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img8 = load_image("assets\enemies/boss\Walk_007.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img9 = load_image("assets\enemies/boss\Walk_008.png", BOSS_WIDTH, BOSS_HEIGHT)
boss_img10 = load_image("assets\enemies/boss\Walk_009.png", BOSS_WIDTH, BOSS_HEIGHT)

boss_images = [
    boss_img,
    boss_img2,
    boss_img3,
    boss_img4,
    boss_img5,
    boss_img6,
    boss_img7,
    boss_img8,
    boss_img9,
    boss_img10,
]
