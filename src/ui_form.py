# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(339, 309)
        icon = QIcon()
        icon.addFile("app.ico", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnChoose = QPushButton(Widget)
        self.btnChoose.setObjectName("btnChoose")

        self.horizontalLayout.addWidget(self.btnChoose)

        self.lblFileName = QLabel(Widget)
        self.lblFileName.setObjectName("lblFileName")
        font = QFont()
        font.setFamilies(["Arial"])
        font.setBold(False)
        self.lblFileName.setFont(font)

        self.horizontalLayout.addWidget(self.lblFileName)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QLabel(Widget)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listUnparsed = QTextEdit(Widget)
        self.listUnparsed.setObjectName("listUnparsed")
        self.listUnparsed.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.listUnparsed)

        self.listParsed = QTextEdit(Widget)
        self.listParsed.setObjectName("listParsed")
        self.listParsed.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.listParsed)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btnSave = QPushButton(Widget)
        self.btnSave.setObjectName("btnSave")

        self.verticalLayout_2.addWidget(self.btnSave)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(
            QCoreApplication.translate("Widget", "Username Creator", None)
        )
        # if QT_CONFIG(accessibility)
        Widget.setAccessibleName(
            QCoreApplication.translate("Widget", "Username Creator", None)
        )
        # endif // QT_CONFIG(accessibility)
        self.btnChoose.setText(
            QCoreApplication.translate("Widget", "Choose File", None)
        )
        self.lblFileName.setText("")
        self.label.setText(QCoreApplication.translate("Widget", "Input:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", "Output:", None))
        self.btnSave.setText(QCoreApplication.translate("Widget", "Save File", None))

    # retranslateUi
