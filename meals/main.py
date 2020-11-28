import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainPage(QWidget):

    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):
        # Top side
        self.Weaklymeal_Generator = QPushButton('식단표 생성')

        # Left side
        # Group
        self.BMI_Checker = QGroupBox('BMI/기초대사량 계산기') # Group for BMI_Height, BMI_Weight, BMI_Confirm
        self.BMI_Show = QGroupBox('BMI') # Group for BMI_Label1, BMI_Label2, BMI_Figure
        self.Kcal_Show = QGroupBox('Kcal') # Group for Kcal_Label1, Kcal_label2, Kcal_Figure
        # BMI_Checker Group
        self.BC_label = QLabel('키&몸무게 입력')
        self.BMI_Height = QLineEdit()
        self.BMI_Height.setPlaceholderText('키(cm)')
        self.BMI_Weight = QLineEdit()
        self.BMI_Weight.setPlaceholderText('몸무게(kg)')
        self.BMI_Confirm = QPushButton('확인')
        # Set BMI_Checker layout
        self.BC_layout = QGridLayout()
        self.BC_layout.addWidget(self.BC_label, 0, 0)
        self.BC_layout.addWidget(self.BMI_Height, 1, 0, 2, 3)
        self.BC_layout.addWidget(self.BMI_Weight, 3, 0, 2, 3)
        self.BC_layout.addWidget(self.BMI_Confirm, 5, 0, 2, 3)
        self.BMI_Checker.setLayout(self.BC_layout)
        # BMI_Show Group
        self.BMI_Label1 = QLabel('당신의 BMI는')
        self.BMI_Figure = QLabel()
        self.BMI_Label2 = QLabel('입니다.')
        # Set BMI_Show layout
        self.BS_layout = QGridLayout()
        self.BS_layout.addWidget(self.BMI_Label1, 1, 0)
        self.BS_layout.addWidget(self.BMI_Figure, 3, 0)
        self.BS_layout.addWidget(self.BMI_Label2, 3, 3)
        self.BMI_Show.setLayout(self.BS_layout)
        # BMI_Show Group
        self.Kcal_Label1 = QLabel('당신의 기초대사량은')
        self.Kcal_Figure = QLabel()
        self.Kcal_Label2 = QLabel('입니다.')
        # Set BMI_Show layout
        self.KS_layout = QGridLayout()
        self.KS_layout.addWidget(self.Kcal_Label1, 1, 0)
        self.KS_layout.addWidget(self.Kcal_Figure, 3, 0)
        self.KS_layout.addWidget(self.Kcal_Label2, 3, 3)
        self.Kcal_Show.setLayout(self.KS_layout)

        # Right side
        # Group
        self.Food_Group = QGroupBox('음식') # Group for Food_List, Food_Adding
        # Food_Group
        self.FG_Label = QLabel('음식 리스트')
        self.Food_Adding = QPushButton('음식 추가')
        self.Food_List = QTableWidget()
        # Set Food_Group layout
        self.FG_layout = QGridLayout()
        self.FG_layout.addWidget(self.FG_Label, 1, 0, 1, 3)
        self.FG_layout.addWidget(self.Food_Adding, 1, 4)
        self.FG_layout.addWidget(self.Food_List, 3, 0, 8, 5)
        self.Food_Group.setLayout(self.FG_layout)

        # Down side
        # Group
        self.Weaklymeal_Group = QGroupBox() # Group for Weaklymeal_Sheet
        # Weaklymeal_Group
        self.Weaklymeal_label = QLabel("금주의 식단")
        self.Weaklymeal_Sheet = QTableWidget()
        # Set Weaklymeal_Group layout
        self.WG_layout = QGridLayout()
        self.WG_layout.addWidget(self.Weaklymeal_label, 0, 0)
        self.WG_layout.addWidget(self.Weaklymeal_Sheet, 1, 0, 1, 2)
        self.Weaklymeal_Group.setLayout(self.WG_layout)

        # Validator Setting - BMI
        self.BMI_Height.setValidator(QIntValidator(120, 240))
        self.BMI_Weight.setValidator(QIntValidator(20, 190))

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.Weaklymeal_Generator, 4, 0, 1, 0)
        self.layout.addWidget(self.BMI_Checker, 1, 0)
        self.layout.addWidget(self.BMI_Show, 2, 0)
        self.layout.addWidget(self.Kcal_Show, 3, 0)
        self.layout.addWidget(self.Food_Group, 1, 1, 3, 1)
        self.layout.addWidget(self.Weaklymeal_Group, 5, 0, 1, 2)

        self.setLayout(self.layout)

        self.setWindowTitle('오늘의 식단')

        # Signals
        self.BMI_Confirm.clicked.connect(self.BMI_Calculating)

    def BMI_Calculating(self):#if 조건으로 아무것도 안쳐질때 오류메시지 출력하
        height = self.BMI_Height.text()
        weight = self.BMI_Weight.text()
        heights = int(height)
        weights = int(weight)
        BMI = weights/((heights/100)*(heights/100))

        # debug calculating BMI
        print(BMI)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainPage()
    Main.show()
    sys.exit(app.exec_())
