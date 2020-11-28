import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainPage(QWidget):

    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):

        #  BMI_group
        self.BMI_group = QGroupBox('오늘의 식단')
        self.BMI_label = QLabel('사용자 정보')

        # BMI_components
        self.BMI_Height = QLineEdit()
        self.BMI_Height.setPlaceholderText('키(cm)')
        self.BMI_Weight = QLineEdit()
        self.BMI_Weight.setPlaceholderText('몸무게(kg)')
        self.BMI_Confirm = QPushButton('확인')

        #  BMI layout
        self.validator_layout = QGridLayout()
        self.validator_layout.addWidget(self.BMI_label, 0, 0)
        self.validator_layout.addWidget(self.BMI_Height, 1, 0, 2, 3)
        self.validator_layout.addWidget(self.BMI_Weight, 3, 0, 2, 3)
        self.validator_layout.addWidget(self.BMI_Confirm, 5, 0, 2, 3)
        self.BMI_group.setLayout(self.validator_layout)

        # Validator Setting - BMI
        self.BMI_Height.setValidator(QIntValidator(120, 240))
        self.BMI_Weight.setValidator(QIntValidator(20, 190))

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.BMI_group, 1, 0)

        self.setLayout(self.layout)

        self.setWindowTitle('오늘의 식단')

        # Signals
        self.BMI_Confirm.clicked.connect(self.BMI_Calculating)

    def BMI_Calculating(self):
        height = self.BMI_Height.text()
        weight = self.BMI_Weight.text()
        heights = int(height)
        weights = int(weight)
        BMI=weights/((heights/100)*(heights/100))

        # debug calculating BMI
        print(BMI)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainPage()
    Main.show()
    sys.exit(app.exec_())
