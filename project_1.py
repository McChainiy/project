import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel

from PyQt5.QtCore import QDateTime, QDate, QTime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GoalWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.goalName = QtWidgets.QLabel(self.centralwidget)
        self.goalName.setGeometry(QtCore.QRect(240, 0, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.goalName.setFont(font)
        self.goalName.setObjectName("goalName")
        self.desc_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.desc_text.setGeometry(QtCore.QRect(20, 130, 291, 341))
        self.desc_text.setObjectName("desc_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.editGoalButton = QtWidgets.QPushButton(self.centralwidget)
        self.editGoalButton.setGeometry(QtCore.QRect(10, 550, 131, 41))
        self.editGoalButton.setObjectName("editGoalButton")
        self.addNoteButtom = QtWidgets.QPushButton(self.centralwidget)
        self.addNoteButtom.setGeometry(QtCore.QRect(480, 540, 181, 51))
        self.addNoteButtom.setObjectName("addNoteButtom")
        self.dateList = QtWidgets.QListWidget(self.centralwidget)
        self.dateList.setGeometry(QtCore.QRect(550, 130, 111, 401))
        self.dateList.setObjectName("dateList")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.chapterList = QtWidgets.QListWidget(self.centralwidget)
        self.chapterList.setGeometry(QtCore.QRect(350, 130, 191, 401))
        self.chapterList.setObjectName("chapterList")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 490, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.goalName.setText(_translate("MainWindow", "**НАЗВАНИЕ**"))
        self.desc_text.setHtml(_translate("MainWindow", '**description**'))
        self.label_2.setText(_translate("MainWindow", "Описание"))
        self.editGoalButton.setText(_translate("MainWindow", "Редактировать  цель"))
        self.addNoteButtom.setText(_translate("MainWindow", "Добавить заметку"))
        self.label_3.setText(_translate("MainWindow", "Заметки"))
        self.label_4.setText(_translate("MainWindow", "Глава"))
        self.label_5.setText(_translate("MainWindow", "Дата"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 801)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 271, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.minutes_dial = QtWidgets.QDial(Dialog)
        self.minutes_dial.setGeometry(QtCore.QRect(400, 40, 81, 81))
        self.minutes_dial.setObjectName("minutes_dial")
        self.hours_dial = QtWidgets.QDial(Dialog)
        self.hours_dial.setGeometry(QtCore.QRect(320, 40, 80, 80))
        self.hours_dial.setObjectName("hours_dial")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(320, 160, 171, 61))
        self.dateEdit.setObjectName("dateEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.addEvent = QtWidgets.QPushButton(Dialog)
        self.addEvent.setGeometry(QtCore.QRect(160, 650, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.addEvent.setFont(font)
        self.addEvent.setObjectName("addEvent")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 740, 321, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.nameTextLine = QtWidgets.QLineEdit(Dialog)
        self.nameTextLine.setGeometry(QtCore.QRect(40, 280, 441, 41))
        self.nameTextLine.setObjectName("nameTextLine")
        self.nameTextLine.setMaxLength(26)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.descriptionText = QtWidgets.QPlainTextEdit(Dialog)
        self.descriptionText.setGeometry(QtCore.QRect(40, 380, 441, 241))
        self.descriptionText.setObjectName("descriptionText")

        self.hours_dial.setSliderPosition(12)
        self.hours_dial.setRange(0, 23)

        self.minutes_dial.setSliderPosition(30)
        self.minutes_dial.setRange(0, 59)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hours"))
        self.label_2.setText(_translate("Dialog", "Minutes"))
        self.label_3.setText(_translate("Dialog", "Название события"))
        self.addEvent.setText(_translate("Dialog", "Принять"))
        self.label_5.setText(_translate("Dialog", "Описание"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(755, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createGoal_button = QtWidgets.QPushButton(self.centralwidget)
        self.createGoal_button.setGeometry(QtCore.QRect(450, 10, 271, 101))
        self.createGoal_button.setObjectName("createGoal_button")

        self.listGoals_name = QtWidgets.QListWidget(self.centralwidget)
        self.listGoals_name.setGeometry(QtCore.QRect(10, 240, 201, 301))
        self.listGoals_name.setObjectName("listGoals")

        self.listGoals_date = QtWidgets.QListWidget(self.centralwidget)
        self.listGoals_date.setGeometry(QtCore.QRect(551, 240, 191, 301))
        self.listGoals_date.setObjectName("listGoals_date")

        self.listGoals_desc = QtWidgets.QListWidget(self.centralwidget)
        self.listGoals_desc.setGeometry(QtCore.QRect(221, 240, 321, 301))
        self.listGoals_desc.setObjectName("listGoals_desc")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)

        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Название')
        self.lbl_name.move(61, 210)
        self.lbl_name.setFont(font)

        self.lbl_description = QLabel(self)
        self.lbl_description.setText('Описание')
        self.lbl_description.move(311, 210)
        self.lbl_description.setFont(font)

        self.lbl_date = QLabel(self)
        self.lbl_date.setText('Дата')
        self.lbl_date.move(631, 210)
        self.lbl_date.setFont(font)



        self.mainCalendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.mainCalendar.setGeometry(QtCore.QRect(20, 10, 401, 191))
        self.mainCalendar.setObjectName("mainCalendar")
        self.nearestGoals = QtWidgets.QPushButton(self.centralwidget)
        self.nearestGoals.setGeometry(QtCore.QRect(470, 142, 231, 51))
        self.nearestGoals.setObjectName("nearestGoals")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.createGoal_button.setText(_translate("MainWindow", "Создать цель"))
        self.nearestGoals.setText(_translate("MainWindow", "Ближайшие цели"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.goals_dict = {}
        self.createGoal_button.clicked.connect(self.create_goal)
        self.listGoals_name.itemDoubleClicked.connect(self.get_smth)

    def get_smth(self):
        print('lol')

    def create_goal(self):
        self.goals_dict[False] = ChangeGoal()
        self.goals_dict[False].exec_()

        if not self.goals_dict[False].notclosed:
            return

        gotten_text = self.goals_dict[False].txt_name

        self.goals_dict[gotten_text] = self.goals_dict[False]
        del self.goals_dict[False]


        self.listGoals_name.addItem(gotten_text)
        self.listGoals_date.addItem(self.goals_dict[gotten_text].dateEdit.text())
        self.listGoals_desc.addItem('{}{}'.format(self.goals_dict[gotten_text].txt_desc[:47],
                            "..." if len(self.goals_dict[gotten_text].txt_desc) > 47 else ''))





class ChangeGoal(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.notclosed = False
        self.calendarWidget.clicked.connect(self.selectDate)

        self.setFixedSize(521, 791)

        self.time = [12, 30]
        self.dateEdit.setTime(QTime(self.time[0], self.time[1]))
        self.dateEdit.setDate(QDate.currentDate())

        self.hours_dial.valueChanged.connect(self.destroy)
        self.minutes_dial.valueChanged.connect(self.destroy)

        self.dateEdit.dateChanged.connect(self.date_changed)

        self.dateEdit.timeChanged.connect(self.time_changed)

        self.addEvent.clicked.connect(self.event_add)

    def event_add(self):
        self.txt_name = self.nameTextLine.text()
        self.txt_desc = self.descriptionText.toPlainText()
        self.txt_desc = ''.join(list(map(lambda x: ' ' if x == '\n' else x, list(self.txt_desc))))
        self.label_4.setText('Ошибка: не введено название события')
        if self.txt_name == '':
            return

        #self.txt, self.dateEdit.text() - метаданные


        if self.txt_name in ex.goals_dict.keys():
            self.label_4.setText('Ошибка: событие с таким названием уже имеется')
            return
        self.notclosed = True
        self.close()

    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        self.datef = QDate(date.year(), date.month(), date.day())
        self.dateEdit.setDate(self.datef)

    def destroy(self):
        if self.sender() == self.hours_dial:
            self.time[0] = self.sender().value()
        else:
            self.time[1] = self.sender().value()
        self.timef = QTime(self.time[0], self.time[1])
        self.dateEdit.setTime(self.timef)

    def date_changed(self):
        self.calendarWidget.setSelectedDate(self.dateEdit.date())

    def time_changed(self):
        self.time = self.dateEdit.text()
        self.time = [int(i) for i in self.time.split()[1].split(':')]

        self.hours_dial.setSliderPosition(self.time[0])
        self.minutes_dial.setSliderPosition(self.time[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
