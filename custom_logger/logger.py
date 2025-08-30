import time
import os
from datetime import datetime

class CustomLogger:
    # ANSI codes stored as class variables to reduce instance memory
    COLORS = {
        # Refined color palette - more professional and visually appealing
        'indigo_bg': "\033[48;5;54m",          # Debug - deep, thoughtful
        'ocean_blue_bg': "\033[48;5;18m",      # Info - clear, professional
        'coral_bg': "\033[48;5;203m",          # Warning - warm but serious
        'emerald_bg': "\033[48;5;22m",         # Success - vibrant, positive
        'burgundy_bg': "\033[48;5;88m",        # Error - serious, attention-getting
        'bold_white': "\033[1;37m",
        'underline': "\033[4m",
        'reset': "\033[0m",
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

    @staticmethod
    def _get_terminal_size():
        try:
            return os.get_terminal_size().columns
        except:
            return 100

    @staticmethod
    def _format_timestamp():
        return datetime.now().isoformat()

    def _play_sound(self):
        try:
            import subprocess
            sound_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'media/error.mp3'
            )
            subprocess.Popen(
                ["mpg123", "-q", sound_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception as e:
            print(f"Sound play failed: {e}")

    def _print_message(self, color, msg, seconds=0, overwrite=False, timestamp=True):
        self.add_to_file(msg)
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

    def add_to_file(self, text):
        try:
            with open(os.getenv("LOG_FILE_PATH"), 'a') as file:
                file.write(text + '\n')
        except: pass

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
        self._print_message('indigo_bg', msg, seconds, overwrite)
        self._print_line()

    def info(self, msg, seconds=0, overwrite=False):
        self._print_message('ocean_blue_bg', msg, seconds, overwrite)
        self._print_line()

    def warning(self, msg, seconds=0, overwrite=False):
        self._print_message('coral_bg', msg, seconds, overwrite)
        self._print_line()

    def success(self, msg, seconds=0, overwrite=False):
        self._print_message('emerald_bg', msg, seconds, overwrite)
        self._print_line()

    def error(self, msg, seconds=0):
        self._print_message('burgundy_bg', msg, seconds)
        if os.getenv("CUSTOM_LOGGER_PLAY_ERROR_SOUND", "") == "" or os.getenv("CUSTOM_LOGGER_PLAY_ERROR_SOUND", "True") == "True":
            self._play_sound()

        for line in self.SAD_FACE:
            self._print_message('burgundy_bg', line, timestamp=False)

        self._print_line()