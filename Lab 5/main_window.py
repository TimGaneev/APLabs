from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    """
    UI, созданный в qt designer
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(379, 302)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.choosecsv = QtWidgets.QPushButton(parent=Form)
        self.choosecsv.setObjectName("choosecsv")
        self.gridLayout_2.addWidget(self.choosecsv, 1, 0, 1, 1)
        self.nextimage = QtWidgets.QPushButton(parent=Form)
        self.nextimage.setObjectName("nextimage")
        self.gridLayout_2.addWidget(self.nextimage, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.image = QtWidgets.QLabel(parent=self.frame)
        self.image.setGeometry(QtCore.QRect(4, 9, 351, 251))
        self.image.setMaximumSize(QtCore.QSize(351, 251))
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.choosecsv.setText(_translate("Form", "Выберите файл аннотации"))
        self.nextimage.setText(_translate("Form", "След."))
