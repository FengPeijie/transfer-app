# -coding: utf-8-
import sys
from HomePage import HomePage
from ModePage1 import ModePage1
from ModePage2 import ModePage2
from PyQt5.QtWidgets import QApplication

class Controller:
    def __int__(self):
        pass
    def show_HomePage(self):
        self.Home = HomePage()
        self.Page1 = ModePage1()
        self.Page2 = ModePage2()
        self.Page1.close()
        self.Page2.close()
        self.Home.switch_ModePage1.connect(self.show_ModePage1)
        self.Home.switch_ModePage2.connect(self.show_ModePage2)
        self.Home.show()
    def show_ModePage1(self):
        self.Page1 = ModePage1()
        self.Page1.switch_HomePage.connect(self.show_HomePage)
        self.Home.hide()
        self.Page1.show()
    def show_ModePage2(self):
        self.Page2 = ModePage2()
        self.Page2.switch_HomePage.connect(self.show_HomePage)
        self.Home.hide()
        self.Page2.show()

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_HomePage()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

