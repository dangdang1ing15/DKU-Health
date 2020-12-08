import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainPage(QWidget): # Main page Class

    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):
        # Top side
        self.Title = QLabel('오늘의 식단')
        self.Weaklymeal_Generator = QPushButton('식단표 생성')

        # Left side
        # Group
        self.BMI_Checker = QGroupBox('BMI/기초대사량 계산기') # Group for BMI_Gender, BMI_Age, BMI_Height, BMI_Weight, BMI_Confirm
        self.BMI_Show = QGroupBox('BMI') # Group for BMI_Label1, BMI_Label2, BMI_Figure
        self.Kcal_Show = QGroupBox('Kcal') # Group for Kcal_Label1, Kcal_label2, Kcal_Figure
        # BMI_Checker Group
        self.BC_label = QLabel('사전정보 입력')
        self.BMI_Gender_Male = QCheckBox('남성')
        self.BMI_Gender_Female = QCheckBox('여성')
        self.BMI_Age = QLineEdit()
        self.BMI_Age.setPlaceholderText('나이(세)')
        self.BMI_Height = QLineEdit()
        self.BMI_Height.setPlaceholderText('키(cm)')
        self.BMI_Weight = QLineEdit()
        self.BMI_Weight.setPlaceholderText('몸무게(kg)')
        self.BMI_Confirm = QPushButton('제출')
        # Set BMI_Checker layout
        self.BC_layout = QGridLayout()
        self.BC_layout.addWidget(self.BC_label, 0, 0)
        self.BC_layout.addWidget(self.BMI_Gender_Male, 1, 0)
        self.BC_layout.addWidget(self.BMI_Gender_Female, 1, 1)
        self.BC_layout.addWidget(self.BMI_Age, 2, 0, 2, 3)
        self.BC_layout.addWidget(self.BMI_Height, 4, 0, 2, 3)
        self.BC_layout.addWidget(self.BMI_Weight, 6, 0, 2, 3)
        self.BC_layout.addWidget(self.BMI_Confirm, 8, 0, 2, 3)
        self.BMI_Checker.setLayout(self.BC_layout)
        # BMI_Show Group
        self.BMI_Label1 = QLabel('당신의 BMI는')
        self.BMI_Figure = QLabel('0')
        self.BMI_Label2 = QLabel('입니다.')
        # Set BMI_Show layout
        self.BS_layout = QGridLayout()
        self.BS_layout.addWidget(self.BMI_Label1, 1, 0)
        self.BS_layout.addWidget(self.BMI_Figure, 3, 0)
        self.BS_layout.addWidget(self.BMI_Label2, 3, 1)
        self.BMI_Show.setLayout(self.BS_layout)
        # Kcal_Show Group
        self.Kcal_Label1 = QLabel('당신의 기초대사량은')
        self.Kcal_Figure = QLabel('0')
        self.Kcal_Label2 = QLabel('입니다.')
        # Set Kcal_Show layout
        self.KS_layout = QGridLayout()
        self.KS_layout.addWidget(self.Kcal_Label1, 1, 0)
        self.KS_layout.addWidget(self.Kcal_Figure, 3, 0)
        self.KS_layout.addWidget(self.Kcal_Label2, 3, 1)
        self.Kcal_Show.setLayout(self.KS_layout)

        # Right side
        # Group
        self.Food_Group = QGroupBox('음식리스트') # Group for Food_List, Food_Adding
        # Food_Group
        self.FA_Group = QGroupBox('음식추가')
        self.Food_List = QListWidget()
        # FA_Group
        self.Food_name = QLineEdit()
        self.Food_name.setPlaceholderText('음식 이름')
        self.Food_Submit = QPushButton('추가')
        self.Food_Delete = QPushButton('삭제')
        # Set Food_Group layout
        self.FG_layout = QGridLayout()
        self.FG_layout.addWidget(self.Food_List, 3, 0, 8, 5)
        self.Food_Group.setLayout(self.FG_layout)
        # Set FA_Group layout
        FA_layout = QGridLayout()
        FA_layout.addWidget(self.Food_name, 0, 0)
        FA_layout.addWidget(self.Food_Submit, 0, 1)
        FA_layout.addWidget(self.Food_Delete, 0, 2)
        self.FA_Group.setLayout(FA_layout)

        # Down side
        # Group
        self.Weaklymeal_Group = QGroupBox() # Group for Weaklymeal_Sheet
        # Weaklymeal_Group
        self.Weaklymeal_label = QLabel("금주의 식단")
        self.Weaklymeal_Sheet = QTableWidget()
        # sheet setting
        self.Weaklymeal_Sheet.setRowCount(3)
        self.Weaklymeal_Sheet.setColumnCount(7)
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
        self.layout.addWidget(self.Title, 0, 0, 1, 0)
        self.layout.addWidget(self.Weaklymeal_Generator, 4, 0, 1, 0)
        self.layout.addWidget(self.BMI_Checker, 1, 0)
        self.layout.addWidget(self.BMI_Show, 2, 0)
        self.layout.addWidget(self.Kcal_Show, 3, 0)
        self.layout.addWidget(self.Food_Group, 1, 1, 3, 1)
        self.layout.addWidget(self.FA_Group, 0, 1)
        self.layout.addWidget(self.Weaklymeal_Group, 5, 0, 1, 2)
        self.setLayout(self.layout)

        # extra window setting
        self.resize(780, 730)
        self.setWindowTitle('오늘의 식단')

        # Signals, This makes widget to function
        self.BMI_Confirm.clicked.connect(self.ShowLeftsideFunction)
        self.BMI_Gender_Male.stateChanged.connect(self.gendercheckBoxState)
        self.BMI_Gender_Female.stateChanged.connect(self.gendercheckBoxState)
        self.Food_Submit.clicked.connect(self.AddListFunction)
        self.Food_Delete.clicked.connect(self.DeleteListFunction)
        self.Weaklymeal_Generator.clicked.connect(self.generateFunction)

    def gendercheckBoxState(self):# checking gender
        gendercounter = 0
        if self.BMI_Gender_Male.isChecked() == True:
            gendercounter = 1
        if self.BMI_Gender_Female.isChecked() == True:
            gendercounter = 2
        return gendercounter

    def BMICalculatingFunction(self): # calculating BMI
        height = self.BMI_Height.text()
        weight = self.BMI_Weight.text()
        heights = int(height)
        weights = int(weight)
        BMI = weights/((heights/100)*(heights/100))
        return BMI

    def KcalCalculatingFunction(self): # calculating Kcal
        gendercounter = self.gendercheckBoxState()
        age = self.BMI_Age.text()
        height = self.BMI_Height.text()
        weight = self.BMI_Weight.text()
        ages = int(age)
        heights = int(height)
        weights = int(weight)
        if gendercounter == 1:
            Kcal = 66.47 + (13.75 * weights) + (5 * heights) - (6.76 * ages)
            return Kcal
        if gendercounter == 2:
            Kcal = 655.1 + (9.56 * weights) + (1.85 * heights) - (4.68 * ages)
            return Kcal
        else:
            return 0

    def ShowBMIFunction(self): # Bring BMI from BMICalculatingFunction and set BMI to BMI_Figure
        BMI = self.BMICalculatingFunction()
        self.BMI_Figure.setNum(round(BMI,2))

    def ShowKcalFunction(self): # Bring Kcal from KcalCalculatingFunction and set Kcal to Kcal_Figure
        Kcal = self.KcalCalculatingFunction()
        self.Kcal_Figure.setNum(int(Kcal))

    def ShowLeftsideFunction(self): # When Button Clicked, this running and processing BMI and Kcal
        self.ShowBMIFunction()
        self.ShowKcalFunction()

    def AddListFunction(self):  # When Food_Submit Clicked, Add lineedit to list
        self.foodText = self.Food_name.text()
        self.Food_List.addItem(self.foodText)
        self.Food_name.setText("")

    def DeleteListFunction(self): # When Food_Delete Clicked, Delete selected list
        self.removeItemRow = self.Food_List.currentRow()
        self.Food_List.takeItem(self.removeItemRow)

    def generateFunction(self): # Adding random meal sheet
        selectedList = self.Food_List
        items = []
        for i in range(selectedList.count()):
            items.append(selectedList.item(i).text())
        for x in range(3):
            for y in range(7):
                Rmeal = random.choice(items)
                self.Weaklymeal_Sheet.setItem(x, y, QTableWidgetItem(Rmeal))




if __name__ == '__main__': # run the GUI
    app = QApplication(sys.argv)
    Main = MainPage()
    Main.show()
    sys.exit(app.exec_())