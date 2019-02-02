from PyQt5.QtWidgets import QDialog, QPlainTextEdit, QGridLayout


class DescriptionDialog(QDialog):
    def __init__(self, name, parent, element):
        super(DescriptionDialog, self).__init__(parent=parent)
        self.setWindowTitle(name)
        layout = QGridLayout()
        self.element = element
        self.p = QPlainTextEdit()
        self.p.setPlainText(self.element._full_description)
        self.p.setMinimumSize(200, 200)
        layout.addWidget(self.p)
        self.setBaseSize(300, 300)
        self.setLayout(layout)

    def closeEvent(self, evnt):
        self.element._full_description = self.p.document().toPlainText()
        super(DescriptionDialog, self).closeEvent(evnt)
