# External imports
import colorama
import os

# :: Global Variables :: #

# Used to check the provided colors to insure they are supported by the program
supported_colors = ["blue", "light_blue", 
                    "cyan", "light_cyan",
                    "red", "light_red",
                    "green", "light_green", 
                    "yellow", "light_yellow",
                    "magenta", "light_magenta"
                    "black", "white", "grey"
                ]

# color objects, used for nicer output
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

# Checks a list of colors in order to make sure the colors provided are valid and supported by the program
def check_colors(provided_colors: list):
    # Converts every alphabetical characters to its lowercase form and ensures every color is a string
    for current_position, color in enumerate(provided_colors):
        provided_colors[current_position] = str(color).lower()
        if color in supported_colors:
            pass
        else:
            print(f"""
            \n{red}[!] Minotaur Error: {yellow}'{color}'{light_red} is an unsupported or invalid color.
            \n{magenta}Supported Colors:{green}
            \nblue, light_blue
            \ncyan, light_cyan
            \nred, light_red
            \ngreen, light_green
            \nyellow, light_yellow
            \nmagenta, light_magenta
            \nblack, white grey
            """)
            exit()

def validate_element_params(element_type, text, menu_option_number, menu_option, accent_color, text_color, title_colors, os_support_color, program_version_color, title_length, title_bar, small_title, program_version_num, os_support_info):
    # Validates the element_type
    if isinstance(element_type, str):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'element_type'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the text type
    if isinstance(text, str):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'text'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the menu_option_number
    if isinstance(menu_option_number, int):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'menu_option_number{light_red} must be type: {yellow}int{reset}")
        exit()
    # Validates the menu_option
    if isinstance(menu_option, str):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'menu_option{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the accent_color
    if isinstance(accent_color, str):
        check_colors([accent_color])
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'accent_color'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the text_color
    if isinstance(text_color, str):
        check_colors([text_color])
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'text color'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the title_colors
    if isinstance(title_colors, list):
        check_colors([title_colors])
    else:
        print(f"{red}[!] Minotaur Erorr: {yellow}'title_colors'{light_red} must be type: {yellow}list{reset}")
        exit()
    # Validates the os_support_color
    if isinstance(os_support_color, str):
        check_colors([os_support_color])
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'os_support_color'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the program_version_color
    if isinstance(program_version_color, str):
        check_colors([program_version_color])
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'program_version_color'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the title_length
    if isinstance(title_length, int):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'title_length'{light_red} must be type: {yellow}int{reset}")
        exit()
    # Validates the title_bar
    if isinstance(title_bar, str):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'title_bar'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the small_title
    if isinstance(small_title, str):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'small_title'{light_red} must be type: {yellow}str{reset}")
        exit()
    # Validates the program_version_num
    if isinstance(program_version_num, float):
        pass
    elif isinstance(program_version_num, int):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'program_version_num'{light_red} must be type: {yellow}float or int{reset}")
        exit()
    # Validates the os_support_info
    if isinstance(os_support_info, str):
        pass
    else:
        print(f"{red}[!] Minotaur Error: {yellow}'os_support_info'{light_red} must be type: {yellow}str{reset}")
        exit()

# Used to set the color to the actual color
def determine_color(provided_color: str) -> str:
    if provided_color == "blue":
        provided_color = blue
    elif provided_color == "light_blue":
        provided_color = light_blue
    elif provided_color == "cyan":
        provided_color = cyan
    elif provided_color == "light_cyan":
        provided_color = light_cyan
    elif provided_color == "red":
        provided_color = red
    elif provided_color == "light_red":
        provided_color = light_red
    elif provided_color == "green":
        provided_color = green
    elif provided_color == "light_green":
        provided_color = light_green
    elif provided_color == "yellow":
        provided_color = yellow
    elif provided_color == "light_yellow":
        provided_color = light_yellow
    elif provided_color == "magenta":
        provided_color = magenta
    elif provided_color == "light_magenta":
        provided_color = light_magenta
    elif provided_color == "black":
        provided_color = black
    elif provided_color == "white":
        provided_color = white
    elif provided_color == "grey":
        provided_color = grey
    return provided_color

def determine_multi_colors(provided_colors: list) -> list:
    for current_pos, provided_color in enumerate(provided_colors):
        if provided_color == "blue":
            provided_color = blue
        elif provided_color == "light_blue":
            provided_color = light_blue
        elif provided_color == "cyan":
            provided_color = cyan
        elif provided_color == "light_cyan":
            provided_color = light_cyan
        elif provided_color == "red":
            provided_color = red
        elif provided_color == "light_red":
            provided_color = light_red
        elif provided_color == "green":
            provided_color = green
        elif provided_color == "light_green":
            provided_color = light_green
        elif provided_color == "yellow":
            provided_color = yellow
        elif provided_color == "light_yellow":
            provided_color = light_yellow
        elif provided_color == "magenta":
            provided_color = magenta
        elif provided_color == "light_magenta":
            provided_color = light_magenta
        elif provided_color == "black":
            provided_color = black
        elif provided_color == "white":
            provided_color = white
        elif provided_color == "grey":
            provided_color = grey
        provided_colors[current_pos] = provided_color
    return provided_colors

class Menu():
    def __init__(self):
        # Placeholder for the menu text
        self._placeholder = ""
        # Placeholder for the menu format strings
        self._header = "{title}\n{title_bar}\n{program_version_color}{program_version_num}\n{os_support_color}{os_support_info}{reset}"
        self._body = "{accent_color}{menu_option_number}) {text_color}{menu_option}{reset}"
        self._paragraph = "{text_color}{text}{reset}"
        self._footer = "{text_color}{space}{text}{space}{reset}"
    # Adds a new element to the menu interface
    def _include(self, element):
        self._placeholder = self._placeholder + f"{element}\n"
    
    def add_element(self, element_type: str, title: str, text="Python Rocks!", menu_option_number=0, menu_option="an option", accent_color="yellow", text_color="blue", title_colors=["white"], os_support_color="yellow", program_version_color="blue", title_length=30, title_bar="_/", small_title="Minotaur", program_version_num=1.0, os_support_info="Linux"):
        # Preforms some basic input validation
        # validate_element_params(element_type, text, menu_option_number, menu_option, accent_color, text_color, title_colors, os_support_color, program_version_color, title_length, title_bar, small_title, program_version_num, os_support_info)
        # Creates the colors
        accent_color = determine_color(accent_color)
        text_color = determine_color(text_color)
        title_colors = determine_multi_colors(title_colors)
        # If the element_type is a header...
        if element_type == "header" and title_colors[0] == None:
            rainbow_colors = [red, yellow, green, cyan, blue, magenta]
            rainbow_title = ''.join(rainbow_colors[char % len(rainbow_colors)] + title[char] for char in range(len(title)))
            self._include(self._header.format(
                title=rainbow_title,
                title_bar=title_bar,
                program_version_color=program_version_color,
                program_version_num=program_version_num,
                os_support_color=os_support_color,
                os_support_info=os_support_info,
                reset=reset
            ))
        elif element_type == "header" and title_colors[0] != None:
            colorful_title = ''.join(title_colors[char % len(title_colors)] + title[char] for char in range(len(title)))
            self._include(self._header.format(
                title=colorful_title,
                title_bar=title_bar,
                program_version_color=program_version_color,
                program_version_num=program_version_num,
                os_support_color=os_support_color,
                os_support_info=os_support_info,
                reset=reset
            ))
        # If the element type is a body...
        elif element_type == "body":
            self._include(self._body.format(
                accent_color=accent_color,
                menu_option_number=menu_option_number,
                text_color=text_color,
                menu_option=menu_option,
                reset=reset
            ))
        elif element_type == "paragraph":
            self._include(self._paragraph.format(
                text_color=text_color,
                text=text,
                reset=reset
            ))
        elif element_type == "footer":
            self._include(self._footer.format(
                text_color=text_color,
                # Issue: Python won't display the spaces despite there being no issue with the syntax
                space=" " * (len(title_bar) // 2 - len(text)),
                text=text,
                reset=reset
            ))


# Example usage of the Menu class

# Create an instance of the Menu class
menu = Menu()

# Add a header to the menu
menu.add_element(
    element_type="header",
    title="Toolbox",
    title_length=10,
    title_colors=["red", "white", "blue"],
    program_version_num=1.0,
    os_support_info="Linux"
)

# Add body elements (menu options)
menu.add_element(
    title="Minotaur",
    element_type="body",
    menu_option_number=1,
    menu_option="XSS Vuln Scanner",
    accent_color="light_green",
    text_color="white"
)

menu.add_element(
    title="Minotaur",
    element_type="paragraph",
    text="XSS Vuln Scanner Description.",
    text_color="light_cyan"
)

menu.add_element(
    title="Minotaur",
    element_type="body",
    menu_option_number=2,
    menu_option="SQLI Vuln Scanner",
    accent_color="light_blue",
    text_color="white"
)

menu.add_element(
    title="Minotaur",
    element_type="paragraph",
    text="SQLI Vuln Scanner Description.",
    text_color="light_cyan"
)

# Add a footer to the menu
menu.add_element(
    title="Minotaur",
    element_type="footer",
    text="[!] Warning: This is a test UX menu!",
    title_length=10,
    text_color="grey",
    title_bar="_/"
)

# Print the constructed menu
print(menu._placeholder)