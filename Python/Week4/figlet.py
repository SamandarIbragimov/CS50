from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    word = input("Input: ")
    figlet.setFont(font=choice(fonts))
    print(figlet.renderText(word))
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f","--font"] and sys.argv[2] in fonts:
        word = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(word))
    else:
        sys.exit("Invalid Usage")
else:
    sis.exit("Invalid Usage")

