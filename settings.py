import pygame

pygame.init()
pygame.font.init()

class Settings:
    BOARD_SIZE = 8
    WIDTH, HEIGHT = 800, 800
    WINDOW_ICON_SIZE = 30
    FPS = 60
    AI_DEPTH = 3
    THEMES = [
            # CORAL THEME
            {"dark": (112, 162, 163), "light": (173, 228, 185), "outline": (0, 0, 0)},
            # DUSK THEME
            {"dark": (112, 102, 119), "light": (204, 183, 174), "outline": (0, 0, 0)},
            # WHEAT THEME
            {"dark": (187, 190, 100), "light": (234, 240, 206), "outline": (0, 0, 0)},
            # SAND CASTLE THEME
            {"dark": (184, 139, 74), "light": (227, 193, 111), "outline": (0, 0, 0)},
            # CHESS.com THEME
            {"dark": (148, 111, 81), "light": (240, 217, 181), "outline": (0, 0, 0)},
            # GREEN THEME
            {"dark": (118, 148, 85), "light": (234, 238, 210), "outline": (0, 0, 0)},
        ]

    def __init__(self):
        self.resolution = (self.WIDTH, self.HEIGHT)
        self.top_offset = 20
        self.spot_size = (self.HEIGHT - self.top_offset) // self.BOARD_SIZE
        self.horizontal_offset = self.WIDTH // 2 - (self.spot_size * (self.BOARD_SIZE // 2))
        self.coord_font = pygame.font.SysFont("arial", 18, bold=True)
        self.highlight_outline = 5
        self.theme_index = -1

class SoundEffects:
    SOUND_FILES = {
        "capture": "./assets/sounds/capture_sound.mp3",
        "castle": "./assets/sounds/castle_sound.mp3",
        "check": "./assets/sounds/check_sound.mp3",
        "checkmate": "./assets/sounds/checkmate_sound.mp3",
        "game_over": "./assets/sounds/gameover_sound.mp3",
        "game_start": "./assets/sounds/start_sound.mp3",
        "move": "./assets/sounds/move_sound.mp3",
        "stalemate": "./assets/sounds/stalemate_sound.mp3",
        "pop": "./assets/sounds/pop.mp3",
    }

    def __init__(self):
        self.sounds = {name: pygame.mixer.Sound(path) for name, path in self.SOUND_FILES.items()}

Config = Settings()
sounds = SoundEffects()
