import sys
from datetime import date
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector as mysql

todaydate = date.today().strftime("%B %d, %Y")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('mood tracker')
        self.setFixedWidth(1080)
        self.setFixedHeight(720)
        self.MainUI()
        self.show()
    
    def creDBbutton(self):
        self.newwindow = CreateDBWindow()
        self.newwindow.show()
        self.newwindow.move(self.pos())

    def MainUI(self):
        heading = QLabel('home',self)
        heading.move(50,20)
        heading.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')
        heading.show()
        
        today = QLabel('today:',self)
        today.move(50,90)
        today.setStyleSheet('font-size: 24px; font-weight: thin; font-family: Verdana, sans-serif;')
        today.show()

        date = QLabel(todaydate,self)
        date.move(145,90)
        date.setStyleSheet('font-size: 24px; font-weight: thin; font-family: Verdana, sans-serif;')
        date.show()
        
        imagelabel = QLabel(self)
        image = QPixmap('House.png')
        nimage = image.scaled(QSize(120,120))
        imagelabel.setPixmap(nimage)
        imagelabel.move(900,20)
        imagelabel.show()

        mood = QLabel('good',self)
        mood.move(50,200)
        mood.setStyleSheet('font-size: 48px; color: #219653; font-weight: bold; font-family: Verdana,sans-serif;')
        mood.show()
        
        moodLabel = QLabel('current mood',self)
        moodLabel.move(50,270)
        moodLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        moodLabel.show()
        
        ads = QLabel('7.6',self)
        ads.move(400,200)
        ads.setStyleSheet('font-size: 48px; color: #DCAC00; font-weight: bold; font-family: Verdana,sans-serif;')
        ads.show()
        
        adsLabel = QLabel('average day score',self)
        adsLabel.move(400,270)
        adsLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        adsLabel.show()
        
        totentries = QLabel('123',self)
        totentries.move(800,200)
        totentries.setStyleSheet('font-size: 48px; font-weight: bold; font-family: Verdana,sans-serif;')
        totentries.show()

        totentriesLabel = QLabel('total entries',self)
        totentriesLabel.move(800,270)
        totentriesLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        totentriesLabel.show()
        
        actions = QLabel('actions',self)
        actions.move(50,370)
        actions.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')
        actions.show()

        actionsButtons=QScrollArea(self)
        actionsButtons.move(50,440)
        actionsButtons.resize(980,150)
        actionsButtons.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        actionsButtons.setWidgetResizable(True)
        actionsButtons.show()
        
        actionsBox = QGridLayout()
        creDB = QPushButton('create database',self)
        creDB.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        creDB.clicked.connect(self.creDBbutton)
        creDB.show()

        addEn = QPushButton('add an entry',self)
        addEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        addEn.show()
        
        editEn = QPushButton('edit an entry',self)
        editEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        editEn.show()
        
        viewEn = QPushButton('view entries',self)
        viewEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        viewEn.show()
        
        delEn = QPushButton('delete an entry',self)
        delEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        delEn.show()
        
        showSumm = QPushButton('show summary',self)
        showSumm.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        showSumm.show()
        
        actionsBox.addWidget(creDB,0,0)
        actionsBox.addWidget(addEn,0,1)
        actionsBox.addWidget(editEn,0,2)
        actionsBox.addWidget(viewEn,1,0)
        actionsBox.addWidget(delEn,1,1)
        actionsBox.addWidget(showSumm,1,2)

        new = QWidget()
        new.setLayout(actionsBox)
        actionsButtons.setWidget(new)
        actionsButtons.show()
        
        copyrightText = QLabel('© mood tracker 2023',self)
        copyrightText.move(480,690)
        copyrightText.setStyleSheet('font-weight:thin;font-family: Verdana,sans-serif; font-size: 16px;')
        copyrightText.show()

class CreateDBWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('mood tracker')
        self.setFixedWidth(1080)
        self.setFixedHeight(720)
        self.MainUI()
        self.show()

    def createDatabase(self):
        hostval = self.host.text()
        userval = self.user.text()
        passwordval = self.password.text()
        con = mysql.connect(host=hostval,user=userval,password=passwordval)
        cur = con.cursor()
        cur.execute('create database MoodTracker')
        print('Database created successfully')
        cur.execute('use moodtracker')
        cur.execute('create table mood (date date primary key, mood varchar(15), dayscore float(3,1), activities varchar(75), comments varchar(100))')
        print('Table created successfully')

    def MainUI(self):
        self.heading = QLabel('create database',self)
        self.heading.move(50,20)
        self.heading.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')
        self.heading.show()

        self.imagelabel = QLabel(self)
        self.image = QPixmap('Hammer.png')
        self.nimage = self.image.scaled(QSize(120,120))
        self.imagelabel.setPixmap(self.nimage)
        self.imagelabel.move(900,20)
        self.imagelabel.show()

        self.hostLabel = QLabel('host: ',self)
        self.hostLabel.move(50,150)
        self.hostLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.hostLabel.show()

        self.host = QLineEdit(self)
        self.host.move(190,150)
        self.host.setFixedWidth(500)
        self.host.setFixedHeight(40)
        self.host.setStyleSheet('font-size: 20px')
        self.host.show()

        self.userLabel = QLabel('user: ',self)
        self.userLabel.move(50,230)
        self.userLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.userLabel.show()

        self.user = QLineEdit(self)
        self.user.move(190,230)
        self.user.setFixedWidth(500)
        self.user.setFixedHeight(40)
        self.user.setStyleSheet('font-size: 20px')
        self.user.show()

        self.passwordLabel = QLabel('password: ',self)
        self.passwordLabel.move(50,310)
        self.passwordLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.passwordLabel.show()

        self.password = QLineEdit(self)
        self.password.move(190,310)
        self.password.setFixedWidth(500)
        self.password.setFixedHeight(40)
        self.password.setStyleSheet('font-size: 20px')
        self.password.show()

        # self.databaseLabel = QLabel('database: ',self)
        # self.databaseLabel.move(50,390)
        # self.databaseLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        # self.databaseLabel.show()

        # self.database = QLineEdit(self)
        # self.database.move(190,390)
        # self.database.setFixedWidth(500)
        # self.database.setFixedHeight(40)
        # self.database.setStyleSheet('font-size: 20px')
        # self.database.show()

        self.createDBbutton = QPushButton('create database',self)
        self.createDBbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        self.createDBbutton.move(50,480)
        self.createDBbutton.show()
        self.createDBbutton.clicked.connect(self.createDatabase)

        self.backbutton = QPushButton('back to home',self)
        self.backbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        self.backbutton.move(300,480)
        self.backbutton.show()
        self.backbutton.clicked.connect(lambda:self.close())

        self.copyrightText = QLabel('© mood tracker 2023',self)
        self.copyrightText.move(480,690)
        self.copyrightText.setStyleSheet('font-weight:thin;font-family: Verdana,sans-serif; font-size: 16px;')



app = QApplication([])
app.setStyle('Fusion')
mw = MainWindow()
app.exec_()