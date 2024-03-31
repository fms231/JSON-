from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import sys
import myjson
import json

class MyJsonFormat(myjson.Ui_JSONFormat, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_format.clicked.connect(
            self.do_format_json("format")
        )

        self.pushButton_unformat.clicked.connect(
            self.do_format_json("unformat")
        )

        self.pushButton_copyJSON.clicked.connect(
            self.do_copy_json
        )

    def do_copy_json(self):
        board = QApplication.clipboard()
        board.setText(self.plainTextEdit_JSON.toPlainText())
        QMessageBox.information(self, "提示", "复制成功")

    def do_format_json(self,action):
        def inner_format():
            json_cont = self.plainTextEdit_JSON.toPlainText()
            if not json_cont:
                QMessageBox.warning(self, "警告", "请输入JSON文本")
                return
            try:
                if action == "format":
                    new_cont = json.dumps(json.loads(json_cont), indent=4,ensure_ascii=False)
                else:
                    new_cont = json.dumps(json.loads(json_cont), ensure_ascii=False)
                
                self.plainTextEdit_JSON.setPlainText(new_cont)
            except Exception as e:
                QMessageBox.warning(self, "警告", f"JSON格式错误:{e}")
                return
            QMessageBox.information(self, "提示", "操作完成")

        return inner_format

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myjsonformat = MyJsonFormat()
    
    sys.exit(app.exec())