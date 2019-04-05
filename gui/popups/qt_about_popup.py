import sys

from PyQt5.QtWidgets import QGridLayout, QApplication, QMessageBox


class AboutDialog(QMessageBox):
    def __init__(self, name, parent):
        super(AboutDialog, self).__init__(parent=parent)
        self.setWindowTitle(name)
        self.findChild(QGridLayout).setColumnMinimumWidth(1, 550)
        self.version = "0.3.1"
        self.setText(f"<h3>Dungeon and Dragons 3.5 Character Sheet version {self.version}</h3>"
                     f"<h3>Copyright (C) 2019 by Mateusz Pruski</h3>"
                     f"<h3>Github repository: <a href='https://github.com/ShanSanear/DnDCharacterSheet'>Click here</a></h3>"
                     f"<h4>This application is designed for usage as interactive Character Sheet, based on SRD DnD 3.5</h4>"
                     f"<p>This program is free software: you can redistribute it and/or modify"
                     f" it under the terms of the GNU General Public License as published by"
                     f" the Free Software Foundation, either version 3 of the License, or"
                     f" (at your option) any later version.</p>"
                     f"<p>This program is distributed in the hope that it will be useful,"
                     f" but WITHOUT ANY WARRANTY; without even the implied warranty of"
                     f" MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
                     f" GNU General Public License for more details.</p>"
                     f"<p>You should have received a copy of the GNU General Public License"
                     f" along with this program.  If not, see <a href=https://www.gnu.org/licenses>here</a>.</p>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = AboutDialog(name="AboutDialog", parent=None)
    form.show()
    app.exec_()
