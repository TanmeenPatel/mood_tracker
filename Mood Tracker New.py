#Imported modules
import sys
from datetime import date
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
import mysql.connector as mysql

#Global variables needed throughout program
todaydate = date.today().strftime("%B %d, %Y")
hostval = ""
userval = ""
passwordval = ""

#Instructions for the Application
inst = 'Welcome to mood tracker, your secure space to save your thoughts and track your mood.'

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

    def addEnbutton(self):
        self.newwindow = AddEntryWindow()
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
        creDB = QPushButton('create database/log in',self)
        creDB.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        creDB.clicked.connect(self.creDBbutton)
        creDB.show()

        addEn = QPushButton('add an entry',self)
        addEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        addEn.clicked.connect(self.addEnbutton)
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
        try:
            global hostval
            global userval
            global passwordval
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
        except mysql.errors.InterfaceError:
            self.alert1.show()
            self.alert2.hide()
        except mysql.errors.ProgrammingError:
            self.alert1.show()
            self.alert2.hide()
        except mysql.errors.DatabaseError:
            if hostval == '':
                self.alert2.hide()
                self.alert1.show()
            else:
                self.alert2.show()
                self.alert1.hide()
        else:
            self.alert1.hide()
            self.alert2.hide()
            self.alert3.show()

    def logIn(self):
        try:
            global hostval
            global userval
            global passwordval
            hostval = self.host.text()
            userval = self.user.text()
            passwordval = self.password.text()
            con2 = mysql.connect(host=hostval,user=userval,password=passwordval)
            cur = con2.cursor()
            if con2.is_connected():
                self.alert1.hide()
                self.alert2.hide()
                self.alert3.hide()
                self.alert4.show()
            else:
                self.alert1.show()
                self.alert2.hide()
                self.alert3.hide()
                self.alert4.hide()
        except:
            self.alert1.show()
            self.alert2.hide()
            self.alert3.hide()
            self.alert4.hide()

    def MainUI(self):
        self.heading = QLabel('create database/log in',self)
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

        self.createDBbutton = QPushButton('create database',self)
        self.createDBbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        self.createDBbutton.move(50,480)
        self.createDBbutton.show()
        self.createDBbutton.clicked.connect(self.createDatabase)

        self.loginbutton = QPushButton('log in',self)
        self.loginbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        self.loginbutton.move(250,480)
        self.loginbutton.show()
        self.loginbutton.clicked.connect(self.logIn)

        self.backbutton = QPushButton('back to home',self)
        self.backbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        self.backbutton.move(345,480)
        self.backbutton.show()
        self.backbutton.clicked.connect(lambda:self.close())

        self.copyrightText = QLabel('© mood tracker 2023',self)
        self.copyrightText.move(480,690)
        self.copyrightText.setStyleSheet('font-weight:thin;font-family: Verdana,sans-serif; font-size: 16px;')

        self.alert1 = QLabel('Enter the correct data in all fields',self)
        self.alert1.move(50,550)
        self.alert1.setStyleSheet('color: #F04E4E; font-size: 24px;')
        self.alert1.hide()

        self.alert2 = QLabel('Database already created',self)
        self.alert2.move(50,550)
        self.alert2.setStyleSheet('color: #F04E4E; font-size: 24px;')
        self.alert2.hide()

        self.alert3 = QLabel('Database created successfully',self)
        self.alert3.move(50,550)
        self.alert3.setStyleSheet('color: #4bb85f; font-size: 24px;')
        self.alert3.hide()

        self.alert4 = QLabel('Logged in successfully',self)
        self.alert4.move(50,550)
        self.alert4.setStyleSheet('color: #4bb85f; font-size: 24px;')
        self.alert4.hide()

class AddEntryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('mood tracker')
        self.setFixedHeight(720)
        self.setFixedWidth(1080)
        self.MainUI()
        self.show()

    def addEntry(self):
        try:
            date = self.date.text()
            mood = self.mood.text()
            daysc = self.dayscore.text()
            acts = self.activities.text()
            comms = self.comments.text()
            con = mysql.connect(host=hostval,user=userval,password=passwordval,database='moodtracker')
            cur = con.cursor()
            q = "insert into mood values('{}','{}',{},'{}','{}')".format(date,mood,daysc,acts,comms)
            cur.execute(q)
            con.commit()
        except mysql.errors.ProgrammingError:
            self.alert3.hide()
            self.alert2.hide()
            self.alert4.hide()
            self.alert1.show()
        except mysql.errors.DataError:
            self.alert4.hide()
            self.alert1.hide()
            self.alert2.hide()
            self.alert3.show()
        except mysql.errors.IntegrityError:
            self.alert1.hide()
            self.alert2.hide()
            self.alert3.hide()
            self.alert4.show()
        else:
            self.alert1.hide()
            self.alert3.hide()
            self.alert4.hide()
            self.alert2.show()

    def MainUI(self):
        self.heading = QLabel('add entry',self)
        self.heading.move(50,20)
        self.heading.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')
        self.heading.show()

        self.imagelabel = QLabel(self)
        self.image = QPixmap('Memo.png')
        self.nimage = self.image.scaled(QSize(120,120))
        self.imagelabel.setPixmap(self.nimage)
        self.imagelabel.move(900,20)
        self.imagelabel.show()

        self.dateLabel = QLabel('date: ',self)
        self.dateLabel.move(50,150)
        self.dateLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.dateLabel.show()

        self.date = QLineEdit(self)
        self.date.move(200,150)
        self.date.setFixedWidth(500)
        self.date.setFixedHeight(40)
        self.date.setStyleSheet('font-size: 20px')
        self.date.show()

        self.moodLabel = QLabel('mood: ',self)
        self.moodLabel.move(50,230)
        self.moodLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.moodLabel.show()

        self.mood = QLineEdit(self)
        self.mood.move(200,230)
        self.mood.setFixedWidth(500)
        self.mood.setFixedHeight(40)
        self.mood.setStyleSheet('font-size: 20px')
        self.mood.show()

        self.dayscoreLabel = QLabel('day score: ',self)
        self.dayscoreLabel.move(50,310)
        self.dayscoreLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.dayscoreLabel.show()

        self.dayscore = QLineEdit(self)
        self.dayscore.move(200,310)
        self.dayscore.setFixedWidth(500)
        self.dayscore.setFixedHeight(40)
        self.dayscore.setStyleSheet('font-size: 20px')
        self.dayscore.show()

        self.activitiesLabel = QLabel('activities: ',self)
        self.activitiesLabel.move(50,390)
        self.activitiesLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.activitiesLabel.show()

        self.activities = QLineEdit(self)
        self.activities.move(200,390)
        self.activities.setFixedWidth(500)
        self.activities.setFixedHeight(40)
        self.activities.setStyleSheet('font-size: 20px')
        self.activities.show()

        self.commentsLabel = QLabel('comments: ',self)
        self.commentsLabel.move(50,470)
        self.commentsLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        self.commentsLabel.show()

        self.comments = QLineEdit(self)
        self.comments.move(200,470)
        self.comments.setFixedWidth(500)
        self.comments.setFixedHeight(120)
        self.comments.setStyleSheet('font-size: 20px;')

        self.addEnbutton = QPushButton('add entry',self)
        self.addEnbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        self.addEnbutton.move(50,620)
        self.addEnbutton.show()
        self.addEnbutton.clicked.connect(self.addEntry)

        self.backbutton = QPushButton('back to home',self)
        self.backbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        self.backbutton.move(200,620)
        self.backbutton.show()
        self.backbutton.clicked.connect(lambda:self.close())

        self.alert1 = QLabel('Enter the correct data in all fields',self)
        self.alert1.move(380,625)
        self.alert1.setStyleSheet('color: #F04E4E; font-size: 24px;')
        self.alert1.hide()

        self.alert2 = QLabel('Entry added successfully',self)
        self.alert2.move(380,625)
        self.alert2.setStyleSheet('color: #4bb85f; font-size: 24px;')
        self.alert2.hide()

        self.alert3 = QLabel("Check if entered data is in correct format/doesn't exceed word limit",self)
        self.alert3.move(380,625)
        self.alert3.setStyleSheet('color: #F04E4E; font-size: 24px;')
        self.alert3.hide()

        self.alert4 = QLabel('Entry for this date already exists',self)
        self.alert4.move(380,625)
        self.alert4.setStyleSheet('color: #F04E4E; font-size: 24px;')
        self.alert4.hide()

        self.copyrightText = QLabel('© mood tracker 2023',self)
        self.copyrightText.move(480,690)
        self.copyrightText.setStyleSheet('font-weight:thin;font-family: Verdana,sans-serif; font-size: 16px;')

#Running Application
if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    mw = MainWindow()
    sys.exit(app.exec_())
