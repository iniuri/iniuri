# EN:
# In order to install colorama you will need:
# pip
# pycharm
# Press python Packages
# Press "search"
# Search for Colorama
# Press: "colorama"
# Press : install package
# -------------------------------------------------------------------------------------------------------------------------------------
import colorama as cl # -- импорт --
import time
from colorama import Fore, Back, Style
cl.init()
# Colorama, a somewhat popular tool for using colors in python
# It's not that hard to use, for example
print(Fore.YELLOW + "Im yellow!")
print(Fore.WHITE + "test")
# Fore = text color
time.sleep(1)
print(Back.YELLOW + "TEST $$$!")
# Back = Background color
# -------------------
#Resets all style
print(Style.RESET_ALL)