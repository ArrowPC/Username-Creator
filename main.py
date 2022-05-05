# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import random

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
        self.ui = loader.load(ui_file, self)
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
            self.ui.lblFileName.setText(fileFinal)
            self.ui.lblFileName.adjustSize()
            global unparsed
            unparsed = f.read()
            self.ui.listView.setText(unparsed)
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
        f = open(fileName[0], "x", encoding="utf8")
        for (letters_, words_, number_) in zip(letters, words, number):
            f.write(letters_ + words_ + str(number_))
            f.write("\n")
            print(fileName)


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
