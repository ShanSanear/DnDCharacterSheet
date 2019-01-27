from PyQt5.QtWidgets import QDialog, QPlainTextEdit, QGridLayout


class DescriptionDialog(QDialog):
    def __init__(self, name, parent, feat):
        super(DescriptionDialog, self).__init__(parent=parent)
        self.setWindowTitle(name)
        layout = QGridLayout()
        self.feat = feat
        self.p = QPlainTextEdit()
        self.p.setPlainText(self.feat._full_description)
        self.p.setMinimumSize(200, 200)
        layout.addWidget(self.p)
        self.setBaseSize(300, 300)
        self.setLayout(layout)

    def closeEvent(self, evnt):
        self.feat._full_description = self.p.document().toPlainText()
        super(DescriptionDialog, self).closeEvent(evnt)
