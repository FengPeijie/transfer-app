# -coding: utf-8-
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import (QApplication, QDesktopWidget,
                             QWidget,QToolTip,QPushButton,
                             QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import (QIcon,QFont)

class HomePage(QWidget):
    switch_ModePage1 = QtCore.pyqtSignal()#跳转信号
    switch_ModePage2 = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #设置字体
        QPushButton.setFont(self,QFont('宋体',12,60))
        QToolTip.setFont(QFont('仿宋', 10))#提示框字题

        #设置按钮
        #QPushButton.setStyleSheet(self,'border-radius: 10px;border: 2px groove gray') #圆角按钮
        btn1 = QPushButton('模式一', self)
        btn2 = QPushButton('模式二',self)
        btn1.setToolTip('这里写模式一是干啥的')
        btn2.setToolTip('这里写模式二是干啥的')

        btn1.clicked.connect(self.go_ModePage1)
        btn2.clicked.connect(self.go_ModePage2)

        #按钮水平位置
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addStretch(1)
        hbox.addWidget(btn2)
        hbox.addStretch(1)

        #按钮垂直位置
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        self.setLayout(hbox)

        #设置窗口参数
        self.resize(750, 600)
        self.center()
        self.setWindowTitle('风格迁移')
        self.setWindowIcon(QIcon('abs.png'))

    #窗口相对屏幕居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def go_ModePage1(self):
        self.switch_ModePage1.emit()

    def go_ModePage2(self):
        self.switch_ModePage2.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HomePage()
    ex.show()
    sys.exit(app.exec_())