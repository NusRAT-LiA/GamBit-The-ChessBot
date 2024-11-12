# import pygame

# pygame.init()
# pygame.font.init()

# class Settings:
#     # BOARD_SIZE = 8
#     WIDTH, HEIGHT = 800, 800
#     WINDOW_ICON_SIZE = 30
#     FPS = 60
#     AI_DEPTH = 3
#     THEMES = [
#             # CORAL THEME
#             {"dark": (112, 162, 163), "light": (173, 228, 185), "outline": (0, 0, 0)},
#             # DUSK THEME
#             {"dark": (112, 102, 119), "light": (204, 183, 174), "outline": (0, 0, 0)},
#             # WHEAT THEME
#             {"dark": (187, 190, 100), "light": (234, 240, 206), "outline": (0, 0, 0)},
#             # SAND CASTLE THEME
#             {"dark": (184, 139, 74), "light": (227, 193, 111), "outline": (0, 0, 0)},
#             # CHESS.com THEME
#             {"dark": (148, 111, 81), "light": (240, 217, 181), "outline": (0, 0, 0)},
#             # GREEN THEME
#             {"dark": (118, 148, 85), "light": (234, 238, 210), "outline": (0, 0, 0)},
#         ]

#     def __init__(self):
#         self.resolution = (self.WIDTH, self.HEIGHT)
#         self.top_offset = 20
#         self.spot_size = (self.HEIGHT - self.top_offset) // self.BOARD_SIZE
#         self.horizontal_offset = self.WIDTH // 2 - (self.spot_size * (self.BOARD_SIZE // 2))
#         self.coord_font = pygame.font.SysFont("arial", 18, bold=True)
#         self.highlight_outline = 5
#         self.theme_index = -1

# class SoundEffects:
#     SOUND_FILES = {
#         "capture": "./assets/sounds/capture_sound.mp3",
#         "castle": "./assets/sounds/castle_sound.mp3",
#         "check": "./assets/sounds/check_sound.mp3",
#         "checkmate": "./assets/sounds/checkmate_sound.mp3",
#         "game_over": "./assets/sounds/gameover_sound.mp3",
#         "game_start": "./assets/sounds/start_sound.mp3",
#         "move": "./assets/sounds/move_sound.mp3",
#         "stalemate": "./assets/sounds/stalemate_sound.mp3",
#         "pop": "./assets/sounds/pop.mp3",
#     }

#     def __init__(self):
#         self.sounds = {name: pygame.mixer.Sound(path) for name, path in self.SOUND_FILES.items()}

# Config = Settings()
# sounds = SoundEffects()
import pygame

# Game Setup
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 550
SQ_SIZE = 60
DIMENSION_X = 5
DIMENSION_Y = 6
FPS = 60

# Colors
BACKGROUND = pygame.Color('azure')
BOARD_COLOR_A = (239, 239, 239)
BOARD_COLOR_B = (149, 141, 148)
HOVER_COLOR = (210, 140, 80)
PLAY_BUTTON_COLOR = pygame.Color('green4')
PLAY_BUTTON_HOVER_COLOR = pygame.Color('chartreuse1')
RESTART_BUTTON_COLOR = pygame.Color('orangered')
RESTART_BUTTON_HOVER_COLOR = pygame.Color('brown4')
BUTTON_TEXT_COLOR = pygame.Color('white')
TOGGLE_BUTTON_COLOR = pygame.Color('purple')

# Button dimensions and positions
BUTTON_WIDTH = 40
BUTTON_HEIGHT = 40
PLAY_BUTTON_POS = (250, 380)
RESTART_BUTTON_POS = (250, 430)
TOGGLE_BUTTON_1_POS = (150, 380)
TOGGLE_BUTTON_2_POS = (100, 380)
TOGGLE_BUTTON_3_POS = (150, 430)
TOGGLE_BUTTON_4_POS = (100, 430)

# Button attributes
# BUTTON_FONT = pygame.font.SysFont('Arial', 20, bold=True)
BUTTON_RADIUS = 8

# Move tracking
MOVE_COUNT = 0
MAX_MOVES = 100
BLACK_AI = False
BLACK_MAN = False
WHITE_AI = False
WHITE_MAN = False
GAME_STARTED = False

# Paths to assets
PIECE_IMAGES_PATH = "./assets/images/"

def load_piece_images():
    pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    colors = ['black', 'white']
    piece_images = {}

    for color in colors:
        for piece in pieces:
            image_name = f"{color}_{piece}"
            image_path = f"{PIECE_IMAGES_PATH}{image_name}.png"
            piece_images[image_name] = pygame.image.load(image_path)

    return piece_images

def load_sound_effects():
    effects = {
        'move': pygame.mixer.Sound('./audios/move_sound.mp3'),
        # 'undo': pygame.mixer.Sound('./audios/undo_moves.wav'),
        'checkmate': pygame.mixer.Sound('./audios/checkmate_sound.mp3')
    }
    return effects
