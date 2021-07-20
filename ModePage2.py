import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import (QApplication, QDesktopWidget,
                             QWidget,QToolTip,QPushButton,
                             QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import (QIcon,QFont)

class ModePage2(QWidget):
    switch_HomePage = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #设置窗口参数
        self.resize(750, 600)
        self.center()
        self.setWindowTitle('模式二')
        self.setWindowIcon(QIcon('abs.png'))

        # 设置按钮
        # QPushButton.setStyleSheet(self,'border-radius: 10px;border: 2px groove gray') #圆角按钮
        btn1 = QPushButton('返回', self)
        btn1.setToolTip('返回到主页')

        btn1.clicked.connect(self.go_HomePage)

        # 按钮水平位置
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)

        # 按钮垂直位置
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(hbox)

    #窗口相对屏幕居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def go_HomePage(self):
        self.switch_HomePage.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModePage2()
    ex.show()
    sys.exit(app.exec_())