import time
import os
from datetime import datetime
import pkg_resources

class CustomLogger:
    def __init__(self):
        # ANSI escape codes
        self.yellow_background = "\033[43m"
        self.green_background = "\033[42m"
        self.dark_green_background = "\033[48;5;22m"
        self.blue_background = "\033[44m"
        self.red_background = "\033[41m"
        self.bold_white_text = "\033[1;37m"
        self.underline_text = "\033[4m"
        self.reset_formatting = "\033[0m"
        self.dark_pink_background = "\033[48;5;52m"
        self.light_pink_background = "\033[48;5;217m"
        self.pink_background = "\033[48;5;212m"
        self.bright_purple_background = "\033[48;5;129m"
        self.dark_purple_background = "\033[48;5;54m"

        self.DIGITS = {
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

        self.SAD_FACE = [
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

        try:
            self.columns, _ = os.get_terminal_size()
        except:
            self.columns = 100

    def play_sound(self, file_name):
        try:
            import pygame
            sound_path = pkg_resources.resource_filename('custom_logger', f'media/{file_name}')
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            
            last_position = 0
            hang_count = 0
            max_hang_time = 1
            total_wait_time = 2
            
            while pygame.mixer.music.get_busy():
                current_position = pygame.mixer.music.get_pos()
                
                if current_position == last_position:
                    hang_count += 1
                    if hang_count > max_hang_time:
                        pygame.mixer.music.stop()
                        break
                else:
                    hang_count = 0
                
                last_position = current_position
                time.sleep(1)
                total_wait_time -= 1
                
                if total_wait_time <= 0:
                    pygame.mixer.music.stop()
                    break

            pygame.mixer.music.stop()
        except Exception as e:
            self.warning(f"Error playing sound: {e}")

    def custom_print(self, start, msg, end, seconds=0, overwrite=False):
        try:
            if overwrite:
                print("\033[F" * 3)
                print(f'\033[K{start}{datetime.now().isoformat()}:: {msg}{end}')
            else:
                if "----" in msg or "█" in msg:
                    print(f'{start}{msg}{end}')
                else:
                    print(f'{start}{datetime.now().isoformat()}:: {msg}{end}')

            if seconds > 0:
                for i in range(seconds, 0, -1):
                    for lineCount in range(7):
                        line = ''.join(self.DIGITS[digit][lineCount] for digit in str(i))
                        print(f'\033[K{start}{line}{end}')
                    time.sleep(1)
                    if i > 1:
                        print("\033[F" * 8)
        except Exception as e:
            print(f"Error: {e}")

    def print_line(self):
        dash = "-" * (self.columns - 1)
        self.custom_print('', dash, '')

    def debug(self, msg, seconds=0, overwrite=False):
        self.custom_print(f"{self.dark_green_background}{self.bold_white_text}", f"{msg}", f"{self.reset_formatting}", seconds, overwrite)
        self.print_line()

    def info(self, msg, seconds=0, overwrite=False):
        self.custom_print(f"{self.bright_purple_background}{self.bold_white_text}", f"{msg}", f"{self.reset_formatting}", seconds, overwrite)
        self.print_line()

    def warning(self, msg, seconds=0):
        self.custom_print(f"{self.pink_background}{self.bold_white_text}", f"{msg}", f"{self.reset_formatting}", seconds)
        self.print_line()

    def success(self, msg, seconds=0):
        self.custom_print(f"{self.blue_background}{self.bold_white_text}", f"{msg}", f"{self.reset_formatting}", seconds)
        self.print_line()

    def error(self, msg, seconds=0, play_sound=True):
        self.custom_print(f"{self.red_background}{self.bold_white_text}", f"{msg}", f"{self.reset_formatting}", seconds)
        if play_sound:
            self.play_sound('error.mp3')
        
        for line in self.SAD_FACE:
            self.custom_print(f"{self.red_background}{self.bold_white_text}", line, f"{self.reset_formatting}")
        
        self.print_line()