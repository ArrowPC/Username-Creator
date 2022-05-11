# This Python file uses the following encoding: utf-8
import sys
import random
import qdarktheme

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QPalette
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.lblFileName.setText("No file chosen")
        self.ui.btnSave.setEnabled(False)
        self.ui.btnChoose.clicked.connect(self.chooseFile)
        self.ui.btnSave.clicked.connect(self.saveFile)

    def chooseFile(self):
        fileName = QFileDialog.getOpenFileName(
            self, "Choose text file", "", "Text Files (*.txt)"
        )
        filePath = fileName[0]
        f = open(filePath, "r")
        fileFinal = filePath.rsplit("/", 1)[-1]

        if fileName:
            self.ui.listParsed.setText(format(fileName[0]))
            self.ui.lblFileName.setText(fileFinal)
            self.ui.lblFileName.adjustSize()
            global unparsed
            unparsed = f.read()
            self.ui.listUnparsed.setText(unparsed)
            self.ui.btnSave.setEnabled(True)

    def saveFile(self):
        message = unparsed
        parsed = message.split("\n")
        try:
            words = [parsed.split(" ", 1)[1] for parsed in parsed]
        except Exception:
            print("yo")
            msg = QMessageBox()
            msg.setText("Choose correct file format pls")
            msg.show()
        letters = [word[0] for word in parsed]
        number = random.sample(range(1001, 9999), len(parsed))
        fileName = QFileDialog.getSaveFileName(
            self, "Save formatted file", "SULES_Usernames", "Text Files (*.txt)"
        )
        f = open(fileName[0], "a", encoding="utf8")
        for (letters_, words_, number_) in zip(letters, words, number):
            f.write(letters_ + words_ + str(number_))
            f.write("\n")
            print(fileName)


def format(fileName):
    result = ""
    f = open(fileName, "r")
    message = f.read()

    parsed = message.split("\n")

    words = [parsed.split(" ", 1)[1] for parsed in parsed]
    letters = [word[0] for word in parsed]

    number = random.sample(range(1001, 9999), len(parsed))

    for (letters_, words_, number_) in zip(letters, words, number):
        result += letters_ + words_ + str(number_)
        result += "\n"
    return result


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    widget.show()
    sys.exit(app.exec())
