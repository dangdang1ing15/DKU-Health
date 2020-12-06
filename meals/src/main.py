# -*- coding: utf-8 -*-
import sys
import os
import sqlite3 as sq
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AddPage(QDialog):
    def __init__(self):
        super().__init__()
        self.AddUI()

    def AddUI(self):
        self.setWindowTitle('음식 추가')
        self.FA_Group = QGroupBox()
        self.Food_name = QLineEdit()
        self.Food_name.setPlaceholderText('음식 이름')
        self.Food_Kcal = QLineEdit()
        self.Food_Kcal.setPlaceholderText('칼로라(kcal)')
        self.Food_ingredient = QComboBox()
        self.Food_ingredient.addItem('1')
        self.Food_Submit = QPushButton('추가')

        FA_layout = QGridLayout()
        FA_layout.addWidget(self.Food_name, 0, 0)
        FA_layout.addWidget(self.Food_Kcal, 0, 1)
        FA_layout.addWidget(self.Food_ingredient, 0, 2)
        FA_layout.addWidget(self.Food_Submit, 0, 3)

        self.setLayout(FA_layout)

        self.Food_Kcal.setValidator(QIntValidator(0, 10000))
        self.Food_Submit.clicked.connect(self.InsertData)
        self.setTable()

    def setTable(self):
        # Table 가로(column) 갯수
        MainPage.food_List.setColumnCount(4)

        # Table 칼럼 헤더 라벨
        MainPage.food_List.setHorizontalHeaderLabels(['번호', '이름', '나이', '삭제'])

    def CreateTable(self):
        # sqlite3 db 파일 접속, 없으면 생성
        conn = sq.connect("foodlist.db")
        cur = conn.cursor()

        # db에 table라는 테이블이 있는지 sqlite3의 마스터 테이블에서 정보를 받아온다.
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name ='food'"
        cur.execute(sql)
        rows = cur.fetchall()

        # table 테이블이 없으면 새로 생성하고,  있으면 통과
        if not rows:
            sql = "CREATE TABLE food (idx INTEGER PRIMARY KEY, fname TEXT, fkcal INTEGER)"
            cur.execute(sql)
            conn.commit()

        conn.close()

    def InsertData(self):
        # 두개의 lineEdit에서 각각 이름과 나이를 받아온다.
        fname = self.Food_name.text()
        fkcal = self.Food_Kcal.text()

        conn = sq.connect("foodlist.db")
        cur = conn.cursor()

        sql = "INSERT INTO food (fname, fkcal) VALUES (?,?)"
        cur.execute(sql, (fname, fkcal))
        conn.commit()
        conn.close()

        # 데이터 입력 후 DB의 내용 불러와서 TableWidget에 넣기 위한 함수 호출
        self.SelectData()

    def SelectData(self):
        # 데이터베이스 내부 테이블의 내용을 모두 추출
        conn = sq.connect("foodlist.db")
        cur = conn.cursor()

        sql = "SELECT * FROM food"
        cur.execute(sql)
        rows = cur.fetchall()

        conn.close()

        # DB의 내용을 불러와서 TableWidget에 넣기 위한 함수 호출
        self.setTables(rows)

    def setTables(row):
        # DB내부에 저장된 결과물의 갯수를 저장한다.
        count = len(row)

        # 갯수만큼 테이블의 Row를 생성한다.
        MainPage.Food_List.setRowCount(count)

        # row 리스트만큼 반복하며 Table에 DB 값을 넣는다.
        for x in range(count):
            # 리스트 내부의 column쌍은 튜플로 반환하므로 튜플의 각 값을 변수에 저장
            idx, name, kcal = row[x]

            # 테이블의 각 셀에 값 입력
            MainPage.Food_List.setItem(x, 0, QTableWidgetItem(str(idx)))
            MainPage.Food_List.setItem(x, 1, QTableWidgetItem(name))
            MainPage.Food_List.setItem(x, 2, QTableWidgetItem(str(kcal)))



class MainPage(QWidget):

    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):
        # Top side
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
        self.BMI_Confirm.clicked.connect(self.ShowLeftsideFunction)
        self.BMI_Gender_Male.stateChanged.connect(self.gendercheckBoxState)
        self.BMI_Gender_Female.stateChanged.connect(self.gendercheckBoxState)
        self.Food_Adding.clicked.connect(self.AddUIOpenFunction)


    # Left side Functions
    def gendercheckBoxState(self):
        gendercounter = 0
        if self.BMI_Gender_Male.isChecked() == True:
            gendercounter = 1
        if self.BMI_Gender_Female.isChecked() == True:
            gendercounter = 2
        return gendercounter
    def BMICalculatingFunction(self):#if 조건으로 아무것도 안쳐질때 오류메시지 출력하는 함수로 변경하기
        height = self.BMI_Height.text()
        weight = self.BMI_Weight.text()
        heights = int(height)
        weights = int(weight)
        BMI = weights/((heights/100)*(heights/100))
        return BMI
    def KcalCalculatingFunction(self):
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
    def ShowBMIFunction(self):
        BMI = self.BMICalculatingFunction()
        self.BMI_Figure.setNum(round(BMI,2))
    def ShowKcalFunction(self):
        Kcal = self.KcalCalculatingFunction()
        self.Kcal_Figure.setNum(int(Kcal))
    def ShowLeftsideFunction(self):
        self.ShowBMIFunction()
        self.ShowKcalFunction()
    # Right side function
    def AddUIOpenFunction(self):
        dlg = AddPage()
        dlg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainPage()
    Add = AddPage()
    Main.show()
    sys.exit(app.exec_())