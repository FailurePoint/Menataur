# Imports PIP modules
import colorama
# Imports Custom Modules
import frankenstien
import mino_menu_titles

# :: Global Variables :: #
# Colour objects, used for nicer output
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
black = colorama.Fore.BLACK
white = colorama.Fore.WHITE
grey = colorama.Fore.LIGHTBLACK_EX

# Used to check the provided colors list in the "build_UX_menu" function
supported_colors = ["blue", "light_blue", 
                    "cyan", "light_cyan",
                    "red", "light_red",
                    "green", "light_green", 
                    "yellow", "light_yellow",
                    "magenta", "light_magenta"
                    "black", "white", "grey"
                ]

# TODO: Finish the destroyer_menus
# checks the menu_num to make sure its an integer or can be converted to one
def check_menu_num(mn):
    try:
        return int(mn)
    except:
        raise ValueError(f"{red}Menu_num must be an integer or an integer in string form!{reset} {blue}[EX: 1 or '1']{reset}")

# builds the UX menu along with its title and returns it
def m_builder(tool_num: int, smn: str, mops: dict, meds: dict, special_mops={}, special_mops_check=False) -> object:
    # Grabs the needed menu options, menu descriptions, and special menu options info
    _menu_opt_nums = list(mops.keys())
    _menu_opt_names = list(mops.values())
    _descriptions = list(meds.values())
    _special_opt_nums = list(special_mops.keys())
    _special_opt_names = list(special_mops.values())
    # Creates the menu object (frankenstien monster)
    frank = frankenstien.Frank()
    # Grabs the title and title bar for the menu
    title_frags = mino_menu_titles.grab_menu(tool_num)
    # Grabs the title from title_frags
    t = title_frags[0]
    # Grabs the title_bar from title_frags
    tb = title_frags[1]
    # Adds the title to the menu based on the name of the tool
    frank.add_limb("head", text=t, title_bar=tb, small_menu_name=smn)
    # Adds the exit option to the menu
    frank.add_limb("body", text="Exit", text_colour=grey, menu_item_num=0, accent_colour=grey)
    # Adds the general menu options and their descriptions to the menu
    for item in range(len(_menu_opt_nums)):
        frank.add_limb("guts", text=_descriptions[item], text_colour=blue)
        frank.add_limb("body", text=_menu_opt_names[item], text_colour=magenta, menu_item_num=_menu_opt_nums[item], accent_colour=yellow)
    # Adds the special menu options to the menu if there is any
    # NOTE: displayed in grey
    if special_mops_check == True:
        for item in range(len(_special_opt_nums)):
            frank.add_limb("body", text=_special_opt_names[item], text_colour=grey, menu_item_num=_special_opt_nums[item], accent_colour=grey)
        # Adds the previous menu option to the menu
        frank.add_limb("body", text="Previous Menu", text_colour=grey, menu_item_num=int(f"{_special_opt_nums[-1] + 1}"), accent_colour=grey)
        # Returns the menu object
        return frank
    else:
        pass
    # Adds the previous menu option to the menu
    frank.add_limb("body", text="Previous Menu", text_colour=grey, menu_item_num=int(f"{_menu_opt_nums[-1] + 1}"), accent_colour=grey)
    # Returns the menu object
    return frank

# Menus - TODO: Fix error preventing the menu titles from being printed (error unknown)

def main_menu():
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    options = {
        1: " Port Scanner", 2: " Subdomain Finder", 3: " XSS Vulnerability Scanner",
        4: " Directory Traversal Vulnerability Scanner", 5: " SQLI Vulnerability Scanners", 6: " Destroyer"
    }
    descriptions = {
        1: "scans port to see if they are open, closed, or filtered", 2: "finds the subdomains of a websites",
        3: "scans a website for XSS vulnerabilities", 4: "scans a website for directory traversal vulnerabilities",
        5: "scans a website for SQLI vulnerabilities", 6: "adds a junk data to a file, encrypts it with aes, then overwrites it and deletes it"
    }

# builds the UX menu along with its title and returns it
def menu_builder(tool_num: int, smn: str, mops: dict, meds: dict, special_mops={}, special_mops_check=False) -> object:
    # Grabs the needed menu options, menu descriptions, and special menu options info
    _menu_opt_nums = list(mops.keys())
    _menu_opt_names = list(mops.values())
    _descriptions = list(meds.values())
    _special_opt_nums = list(special_mops.keys())
    _special_opt_names = list(special_mops.values())
    # Creates the menu object (frankenstien monster)
    frank = frankenstien.Frank()
    # Grabs the title and title bar for the menu
    title_frags = mino_menu_titles.grab_menu(tool_num)
    # Grabs the title from title_frags
    t = title_frags[0]
    # Grabs the title_bar from title_frags
    tb = title_frags[1]
    # Adds the title to the menu based on the name of the tool
    frank.add_limb("head", text=t, title_bar=tb, small_menu_name=smn)
    # Adds the exit option to the menu
    frank.add_limb("body", text="Exit", text_colour=grey, menu_item_num=0, accent_colour=grey)
    # Adds the general menu options and their descriptions to the menu
    for item in range(len(_menu_opt_nums)):
        frank.add_limb("guts", text=_descriptions[item], text_colour=blue)
        frank.add_limb("body", text=_menu_opt_names[item], text_colour=magenta, menu_item_num=_menu_opt_nums[item], accent_colour=yellow)
    # Adds the special menu options to the menu if there is any
    # NOTE: displayed in grey
    if special_mops_check == True:
        for item in range(len(_special_opt_nums)):
            frank.add_limb("body", text=_special_opt_names[item], text_colour=grey, menu_item_num=_special_opt_nums[item], accent_colour=grey)
        # Adds the previous menu option to the menu
        frank.add_limb("body", text="Previous Menu", text_colour=grey, menu_item_num=int(f"{_special_opt_nums[-1] + 1}"), accent_colour=grey)
        # Returns the menu object
        return frank
    else:
        pass
    # Adds the previous menu option to the menu
    frank.add_limb("body", text="Previous Menu", text_colour=grey, menu_item_num=int(f"{_menu_opt_nums[-1] + 1}"), accent_colour=grey)
    # Returns the menu object
    return frank

# Menus - TODO: Fix error preventing the menu titles from being printed (error unknown)

def main_menu():
    # Used to build the menus
    # NOTE: if a new option needs to be added to the menu, simply add it the right dictionary
    options = {
        1: " Port Scanner", 2: " Subdomain Finder", 3: " XSS Vulnerability Scanner",
        4: " Directory Traversal Vulnerability Scanner", 5: " SQLI Vulnerability Scanners", 6: " Destroyer"
    }
    descriptions = {
        1: "scans port to see if they are open, closed, or filtered", 2: "finds the subdomains of a websites",
        3: "scans a website for XSS vulnerabilities", 4: "scans a website for directory traversal vulnerabilities",
        5: "scans a website for SQLI vulnerabilities", 6: "adds a junk data to a file, encrypts it with aes, then overwrites it and deletes it"
    }

"""
header/title = head
body/menu_item = body
descriptions = guts

"""

"""
Generates a UX menu in a block like manner, where each block represent a piece of a page of text (the Monster).
The page is referred to as the Monster.

Elements [private objects]:

<head>
    Header portion of the page. [EX: title]
<body>
    Body portion of the page. [EX: menu_item]
<guts>
    Simple text aligned to the left of the page. [EX: setting description]
<feet>
    Footer portion of the page. [EX: warning message]

Example Usage:
    menu = Frank()
    menu.add_limb("head", text="Toolbox", title_length=10)
    menu.add_limb("body", text="XSS Vuln Scanner", menu_item_num=1)
    menu.add_limb("guts", text="XSS Vuln Scanner Description.", text_colour=light_cyan)
    menu.add_limb("body", text="SQLI Vuln Scanner", menu_item_num=2)
    menu.add_limb("guts", text="SQLI Vuln Scanner Description.", text_colour=light_cyan)
    menu.add_limb("feet", text="[!] Warning: This is a test UX menu!", title_length=10)
    menu.shock()
"""