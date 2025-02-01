# Imports
import colorama

# Initialize Colorama
colorama.init()

# :: Global Variables :: #

# Color objects, used for nicer output
reset = colorama.Fore.RESET
blue = colorama.Fore.BLUE
light_blue = colorama.Fore.LIGHTBLUE_EX
cyan = colorama.Fore.CYAN
light_cyan = colorama.Fore.LIGHTCYAN_EX
red = colorama.Fore.RED
light_red = colorama.Fore.LIGHTRED_EX
green = colorama.Fore.GREEN
light_green = colorama.Fore.LIGHTGREEN_EX
yellow = colorama.Fore.YELLOW
light_yellow = colorama.Fore.LIGHTYELLOW_EX
magenta = colorama.Fore.MAGENTA
light_magenta = colorama.Fore.LIGHTMAGENTA_EX
white = colorama.Fore.WHITE
grey = colorama.Fore.LIGHTBLACK_EX
black = colorama.Fore.BLACK

# Used to check the provided colors to ensure they are supported by the program and set the color value if its supported
supported_colors = {
    "blue": blue, "light_blue": light_blue, 
    "cyan": cyan, "light_cyan": light_cyan,
    "red": red, "light_red": light_red,
    "green": green, "light_green": light_green, 
    "yellow": yellow, "light_yellow": light_yellow,
    "magenta": magenta, "light_magenta": light_magenta,
    "black": black, "white": white, "grey": grey
}

# Validates the colors provided by the user
def validate_color(color: str):
    supported_color_strings = supported_colors.keys()
    # Returns the color value if the color was valid, else an error message is printed to the console
    color = color.lower()
    if color in supported_color_strings:
        return supported_colors[color]
    else:
        print(f"{red}[!] Minotaur Error (line 45): {yellow}{color}{light_red} is not a valid color or is unsupported.{reset}")
        print(f"{green}The following colors are supported:{reset}")
        for color_str in supported_color_strings:
            print(f"{blue}{color_str}{reset}")
        exit()

# Menu Builder Class
class Minotaur():
    def __init__(self):
        # Placeholder for the menu text
        self._placeholder = ""
        # Placeholder Format Strings
        self._header = "{title}\n{title_bar}\n{program_version_color}{program_version_num}\n{os_support_message_color}{os_support_highlight_color}{os_support_color}{os_support_info}{highlight_reset}{reset}"
        self._body = "{accent_color}{menu_option_number}) {menu_option_color}{menu_option}{reset}"
        self._paragraph = "{text_color}{text}{reset}"
        # NOTE: The footer is simular to the paragraph but its text is centered based on the width of the title (default: 5 chars)
        self._footer = "{text_color}{text}{reset}"

    # Adds a new element to the menu
    def _include(self, element):
        self._placeholder = self._placeholder + f"{element}\n"

    # Adds a header element to the menu
    def add_header(self, title: str, title_colors: list, title_width: int, title_bar: list, program_version_color: str, program_version_num: str, os_support_message_color: str, os_support_highlight_color: str, os_support_color: str, os_support_info: list):
        # Validates the colors in the title colors list and gets the real color if they are valid
        for current_pos, color in enumerate(title_colors):
            title_colors[current_pos] = validate_color(color)
        # Creates the title bar using the title width (total_chars = title_width + 5)
        # NOTE: title_width should be an integer representing the character width of the title
        # NOTE: title_bar[0] is the main portion of the title_bar and title_bar[1] is the finishing touch
        title_bar = f"{title_bar[0] * (title_width + 4)}{title_bar[1]}"
        # Validates the os_support_highlight_color and sets its value
        valid_colors = supported_colors.keys()
        os_support_highlight_color = os_support_highlight_color.lower()
        if os_support_highlight_color in valid_colors and os_support_highlight_color != "grey":
            os_support_highlight_color = colorama.Back.os_support_highlight_color
        elif os_support_highlight_color in valid_colors and os_support_highlight_color == "grey":
            os_support_highlight_color = colorama.Back.LIGHTBLACK_EX
        else:
            print(f"{red}[!] Minotaur Error (line 79): {yellow}{os_support_highlight_color}{light_red} is not a valid color or is unsupported.{reset}")
            print(f"{green}The following colors are supported:{reset}")
            for color_str in valid_colors:
                print(f"{blue}{color_str}{reset}")
            exit()
        # Creates a colorful title using the provided title and title colors
        colorful_title = ''.join(title_colors[char % len(title_colors)] + title[char] for char in range(len(title)))
        os_support_info_str = ''.join(os_support_info)  # Join the list into a string
        # Adds the header elements (title, os support information, etc.) to the menu
        self._include(self._header.format(
            title=colorful_title,
            title_bar=title_bar,
            program_version_color=validate_color(program_version_color),
            program_version_num=program_version_num,
            os_support_message_color=validate_color(os_support_message_color),
            os_support_highlight_color=os_support_highlight_color,
            os_support_color=validate_color(os_support_color),
            os_support_info=os_support_info_str,
            highlight_reset=colorama.Back.RESET,
            reset=reset
        ))
    # Adds the body elements (menu options) to the menu
    def add_body(self, accent_color: str, menu_option_number: int, menu_option_color: str, menu_option: str):
        self._include(self._body.format(
            accent_color=validate_color(accent_color),
            menu_option_number=menu_option_number,
            menu_option_color=validate_color(menu_option_color),
            menu_option=menu_option,
            reset=reset
        ))
    # Adds the paragraph elements (descriptions) to the menu
    def add_paragraph(self, text_color: str, text: str, title_width=5):
        self._include(self._paragraph.format(
            text_color=validate_color(text_color),
            text=text,
            reset=reset
        ))
    # Adds the footer element (warning message, thank you message, etc.) to the menu
    def add_footer(self, text_color: str, text: str, title_width=5):
        # Checks the title width to ensure it is an integer
        if isinstance(title_width, int):
            pass
        else:
            print(f"{red}[!] Minotaur Error (line 122): {yellow}title_width {light_red}must be type: {yellow}int{reset}")
        text = f"{' ' * (title_width // 2)}{text}{' ' * (title_width // 2)}"
        # Centers the text on the page based on the current title width, default is 5 characters if the title width is not provided
        self._include(self._paragraph.format(
            text_color=validate_color(text_color),
            text=text,
            reset=reset
        ))