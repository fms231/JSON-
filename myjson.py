# Form implementation generated from reading ui file 'json.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_JSONFormat(object):
    def setupUi(self, JSONFormat):
        JSONFormat.setObjectName("JSONFormat")
        JSONFormat.resize(820, 637)
        self.verticalLayout = QtWidgets.QVBoxLayout(JSONFormat)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=JSONFormat)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit_JSON = QtWidgets.QPlainTextEdit(parent=JSONFormat)
        self.plainTextEdit_JSON.setObjectName("plainTextEdit_JSON")
        self.verticalLayout.addWidget(self.plainTextEdit_JSON)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_format = QtWidgets.QPushButton(parent=JSONFormat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_format.setFont(font)
        self.pushButton_format.setObjectName("pushButton_format")
        self.horizontalLayout.addWidget(self.pushButton_format)
        self.pushButton_unformat = QtWidgets.QPushButton(parent=JSONFormat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_unformat.setFont(font)
        self.pushButton_unformat.setObjectName("pushButton_unformat")
        self.horizontalLayout.addWidget(self.pushButton_unformat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_copyJSON = QtWidgets.QPushButton(parent=JSONFormat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_copyJSON.setFont(font)
        self.pushButton_copyJSON.setObjectName("pushButton_copyJSON")
        self.verticalLayout.addWidget(self.pushButton_copyJSON)

        self.retranslateUi(JSONFormat)
        QtCore.QMetaObject.connectSlotsByName(JSONFormat)

    def retranslateUi(self, JSONFormat):
        _translate = QtCore.QCoreApplication.translate
        JSONFormat.setWindowTitle(_translate("JSONFormat", "JSON格式化小工具"))
        self.label.setText(_translate("JSONFormat", "请输入粘贴JSON文本："))
        self.pushButton_format.setText(_translate("JSONFormat", "格式化JSON"))
        self.pushButton_unformat.setText(_translate("JSONFormat", "反格式化JSON"))
        self.pushButton_copyJSON.setText(_translate("JSONFormat", "复制JSON内容"))
