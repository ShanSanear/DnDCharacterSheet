"""
This will be the main entry point, connecting GUI with the backend created earlier.
"""

import core
import qt_gui


def main():
    char = core.character.Character("Shan")
    attrs = dict(str=12, dex=12, con=12, int=12, wis=12, cha=16)
    char.attributes.set_attributes(attrs)

    qt_gui.init_gui(char)

if __name__ == '__main__':
    main()
