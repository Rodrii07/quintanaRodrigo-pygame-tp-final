import pygame

pygame.mixer.init()
pygame.font.init()

# Fuentes
FONT_SM = pygame.font.Font("assets/fonts/minya_nouvelle_bd.ttf", 32)
FONT_MD = pygame.font.Font("assets/fonts/minya_nouvelle_bd.ttf", 64)
FONT_LG = pygame.font.Font("assets/fonts/thats_super.ttf", 50)

# Sonidos
JUMP_SOUND = pygame.mixer.Sound("assets/sounds/jump.wav")
COIN_SOUND = pygame.mixer.Sound("assets/sounds/pickup_coin.wav")
POWERUP_SOUND = pygame.mixer.Sound("assets/sounds/powerup.wav")
HURT_SOUND = pygame.mixer.Sound("assets/sounds/hurt.ogg")
DIE_SOUND = pygame.mixer.Sound("assets/sounds/death.wav")
LEVELUP_SOUND = pygame.mixer.Sound("assets\sounds\WUBBA LUBBA DUB DUB .mp3")
GAMEOVER_SOUND = pygame.mixer.Sound("assets/sounds/game_over.wav")
ATTACK_SOUND = pygame.mixer.Sound("assets/sounds/powerup.wav")

# Configuraciones de pantalla
TITLE = "Rick & Morty: El juego"
WIDTH = 960
HEIGHT = 640
FPS = 60
GRID_SIZE = 64
FLAG_SIZE = 100

# Configuraciones de jugador
PLAYER_HEIGHT = 64
PLAYER_WIDTH = 45

# Configuraciones del enemigo
BOSS_WIDTH = 110
BOSS_HEIGHT = 140

# Controles
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
JUMP = pygame.K_SPACE
PAUSE = pygame.K_p

# Colores
TRANSPARENT = (0, 0, 0, 0)
DARK_BLUE = (16, 86, 103)
WHITE = (255, 255, 255)
C_RED = (255, 0, 0)
C_GREEN = (0, 255, 0)
C_BLUE = (0, 0, 255)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_PINK = (255, 0, 160)
C_PEACH = (255, 118, 95)
C_BLUE_2 = (38, 0, 160)
C_YELLOW_2 = (255, 174, 0)
C_GREEEN_2 = (38, 137, 0)
C_ORANGE = (255, 81, 0)
