import time
import os
from datetime import datetime
import pkg_resources

class CustomLogger:
    # ANSI codes stored as class variables to reduce instance memory
    COLORS = {
        'yellow_bg': "\033[43m",
        'green_bg': "\033[42m",
        'dark_green_bg': "\033[48;5;22m",
        'blue_bg': "\033[44m",
        'red_bg': "\033[41m",
        'bold_white': "\033[1;37m",
        'underline': "\033[4m",
        'reset': "\033[0m",
        'dark_pink_bg': "\033[48;5;52m",
        'light_pink_bg': "\033[48;5;217m",
        'pink_bg': "\033[48;5;212m",
        'bright_purple_bg': "\033[48;5;129m",
        'dark_purple_bg': "\033[48;5;54m"
    }

    # Pre-rendered ASCII art stored as class variable
    DIGITS = {
            '1': [
                "    ███    ",
                " ██████    ",
                "    ███    ",
                "    ███    ",
                "    ███    ",
                "    ███    ",
                " ████████  "
            ],
            '2': [
                "██████████ ",
                "██      ██ ",
                "        ██ ",
                "██████████ ",
                "██         ",
                "██      ██ ",
                "██████████ "
            ],
            '3': [
                "██████████ ",
                "██      ██ ",
                "        ██ ",
                "   ███████ ",
                "        ██ ",
                "██      ██ ",
                "██████████ "
            ],
            '4': [
                "██      ██ ",
                "██      ██ ",
                "██      ██ ",
                "██████████ ",
                "        ██ ",
                "        ██ ",
                "        ██ "
            ],
            '5': [
                "██████████ ",
                "██         ",
                "██         ",
                "██████████ ",
                "        ██ ",
                "██      ██ ",
                "██████████ "
            ],
            '6': [
                "██████████ ",
                "██         ",
                "██         ",
                "██████████ ",
                "██      ██ ",
                "██      ██ ",
                "██████████ "
            ],
            '7': [
                "██████████ ",
                "        ██ ",
                "        ██ ",
                "        ██ ",
                "        ██ ",
                "        ██ ",
                "        ██ "
            ],
            '8': [
                "██████████ ",
                "██      ██ ",
                "██      ██ ",
                "██████████ ",
                "██      ██ ",
                "██      ██ ",
                "██████████ "
            ],
            '9': [
                "██████████ ",
                "██      ██ ",
                "██      ██ ",
                "██████████ ",
                "        ██ ",
                "        ██ ",
                "██████████ "
            ],
            '0': [
                "███████████",
                "██       ██",
                "██       ██",
                "██       ██",
                "██       ██",
                "██       ██",
                "███████████"
            ]
        }

    SAD_FACE = [
        "     ██████████████     ",
        "   ██              ██   ",
        " ██                  ██ ",
        "██   ████      ████   ██",
        "██   ████      ████   ██",
        "██                    ██",
        "██                    ██",
        "██     ██████████     ██",
        " ██     ████████     ██ ",
        "   ██              ██   ",
        "     ██████████████     "
    ]

    def __init__(self):
        self.columns = self._get_terminal_size()
        self._sound_initialized = False
        self._pygame = None

    @staticmethod
    def _get_terminal_size():
        try:
            return os.get_terminal_size().columns
        except:
            return 100

    @staticmethod
    def _format_timestamp():
        return datetime.now().isoformat()

    def _lazy_init_sound(self):
        if not self._sound_initialized:
            try:
                import pygame
                self._pygame = pygame
                pygame.mixer.init()
                self._sound_initialized = True
            except ImportError:
                self._sound_initialized = False

    def _play_sound(self, max_duration=2):
        if not self._sound_initialized:
            self._lazy_init_sound()
            if not self._sound_initialized:
                return

        try:
            sound_path = pkg_resources.resource_filename('custom_logger', f'media/error.mp3')
            self._pygame.mixer.music.load(sound_path)
            self._pygame.mixer.music.play()
            time.sleep(min(max_duration, 2))
            self._pygame.mixer.music.stop()
        except Exception:
            pass

    def _print_message(self, color, msg, seconds=0, overwrite=False, timestamp=True):
        format_start = f"{self.COLORS[color]}{self.COLORS['bold_white']}"
        format_end = self.COLORS['reset']

        if overwrite:
            print("\033[F" * 3)  # Move cursor up 3 lines
            print(f'\033[K{format_start}{self._format_timestamp()}{format_end} {format_start}{msg}{format_end}')
        else:
            if timestamp and not ("----" in msg or "█" in msg):
                print(f"{format_start}{self._format_timestamp()}{format_end} {format_start}{msg}{format_end}")
            else:
                print(f"{format_start}{msg}{format_end}")

        if seconds > 0:
            self._display_countdown(seconds, format_start, format_end)

    def _display_countdown(self, seconds, format_start, format_end):
        for i in range(seconds, 0, -1):
            for line_count in range(7):
                line = ''.join(self.DIGITS[digit][line_count] for digit in str(i))
                print(f'\033[K{format_start}{line}{format_end}')
            time.sleep(1)
            if i > 1:
                print("\033[F" * 8)

    def _print_line(self):
        print("-" * (self.columns - 1))

    def debug(self, msg, seconds=0, overwrite=False):
        self._print_message('dark_green_bg', msg, seconds, overwrite)
        self._print_line()

    def info(self, msg, seconds=0, overwrite=False):
        self._print_message('bright_purple_bg', msg, seconds, overwrite)
        self._print_line()

    def warning(self, msg, seconds=0, overwrite=False):
        self._print_message('pink_bg', msg, seconds, overwrite)
        self._print_line()

    def success(self, msg, seconds=0, overwrite=False):
        self._print_message('blue_bg', msg, seconds, overwrite)
        self._print_line()

    def error(self, msg, seconds=0, play_sound=True):
        self._print_message('red_bg', msg, seconds)
        if play_sound:
            self._play_sound()
        
        for line in self.SAD_FACE:
            self._print_message('red_bg', line, timestamp=False)
        
        self._print_line()