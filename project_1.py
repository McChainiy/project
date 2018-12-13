import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel

from PyQt5.QtCore import QDateTime, QDate, QTime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GoalWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(815, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.goalName = QtWidgets.QLabel(self.centralwidget)
        self.goalName.setGeometry(QtCore.QRect(300, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.goalName.setFont(font)
        self.goalName.setObjectName("goalName")
        self.desc_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.desc_text.setGeometry(QtCore.QRect(20, 160, 301, 251))
        self.desc_text.setObjectName("desc_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.editGoalButton = QtWidgets.QPushButton(self.centralwidget)
        self.editGoalButton.setGeometry(QtCore.QRect(10, 480, 131, 41))
        self.editGoalButton.setObjectName("editGoalButton")
        self.addNoteButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNoteButton.setGeometry(QtCore.QRect(600, 470, 181, 51))
        self.addNoteButton.setObjectName("addNoteButton")
        self.dateList = QtWidgets.QListWidget(self.centralwidget)
        self.dateList.setGeometry(QtCore.QRect(600, 160, 111, 291))
        self.dateList.setObjectName("dateList")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.chapterList = QtWidgets.QListWidget(self.centralwidget)
        self.chapterList.setGeometry(QtCore.QRect(400, 160, 191, 291))
        self.chapterList.setObjectName("chapterList")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(720, 160, 61, 291))
        self.listWidget.setObjectName("listWidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(360, 60, 20, 461))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 50, 811, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 430, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 470, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
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
        self.desc_text.setHtml(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Описание"))
        self.editGoalButton.setText(_translate("MainWindow", "Редактировать  цель"))
        self.addNoteButton.setText(_translate("MainWindow", "Добавить заметку"))
        self.label_3.setText(_translate("MainWindow", "Заметки"))
        self.label_4.setText(_translate("MainWindow", "Глава"))
        self.label_5.setText(_translate("MainWindow", "Дата"))
        self.label_6.setText(_translate("MainWindow", "Балл"))
        self.label_7.setText(_translate("MainWindow", "Дедлайн - "))
        self.label_8.setText(_translate("MainWindow", "Осталось - "))


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
        self.createGoal_button.setGeometry(QtCore.QRect(450, 10, 271, 121))
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
        self.nearestGoals.setGeometry(QtCore.QRect(451, 142, 131, 61))
        self.nearestGoals.setObjectName("nearestGoals")
        self.allGoals = QtWidgets.QPushButton(self.centralwidget)
        self.allGoals.setGeometry(QtCore.QRect(591, 142, 131, 61))
        self.allGoals.setObjectName("nearestGoals")
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
        self.allGoals.setText(_translate("MainWindow", "Все цели"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.goals_dict = {}
        self.createGoal_button.clicked.connect(self.create_goal)
        self.listGoals_name.itemDoubleClicked.connect(self.open_goal)

        self.nearestGoals.clicked.connect(self.nearest_goals_sort)
        self.allGoals.clicked.connect(self.all_goals_sort)

    def open_goal(self, item):
        self.goals_dict[item.text()].show()


    def create_goal(self):
        dial_data = ChangeGoal()
        dial_data.exec_()

        if not dial_data.notclosed:
            return

        gotten_text = dial_data.txt_name

        self.goals_dict[gotten_text] = Goal(dial_data.txt_name, dial_data.dateEdit.dateTime(),
                                            dial_data.dateEdit.text(), dial_data.txt_desc)

        self.listGoals_name.addItem(gotten_text)
        self.listGoals_date.addItem(self.goals_dict[gotten_text].date_text)
        self.listGoals_desc.addItem(self.print_description(self.goals_dict[gotten_text].desc))

    def nearest_goals_sort(self):
        self.cur_list_of_goals = sorted(self.goals_dict.items(),
                                        key=lambda kv: kv[1].date_q)[:20]

        self.full_list_cleaning()
        self.adding_items_to_list(self.cur_list_of_goals)

    def all_goals_sort(self):
        self.cur_list_of_goals = self.goals_dict.items()

        self.full_list_cleaning()
        self.adding_items_to_list(self.cur_list_of_goals)

    def print_description(self, text):
        return '{}{}'.format(text[:47], "..." if len(text) > 47 else '')

    def full_list_cleaning(self):
        self.listGoals_name.clear()
        self.listGoals_date.clear()
        self.listGoals_desc.clear()

    def adding_items_to_list(self, list_of_goals):
        self.listGoals_name.addItems([i[0] for i in list_of_goals])
        self.listGoals_date.addItems([i[1].date_text for i in list_of_goals])
        self.listGoals_desc.addItems([self.print_description(i[1].desc) for i in list_of_goals])


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

        #self.txt, self.dateEdit.text(), self.dateEdit.dateTime() - метаданные

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


class Goal(QMainWindow, Ui_GoalWindow):
    def __init__(self, name, date_q, date_text, desc):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.desc = desc
        self.date_q = date_q
        self.date_text = date_text


        self.goalName.setText(self.name)

        self.desc_text.setText(self.desc)

        self.label_7.setText('Дедлайн - {}'.format(self.date_text.split()[0]))

        self.label_8.setText('Осталось дней - {}'.format(self.delta_time(
            self.date_text, self.change_date_type(QDateTime.currentDateTime().__str__()))))
        print(self.date_text)
        print(self.change_date_type(QDateTime.currentDateTime().__str__()))
        print(self.delta_time(self.date_text, self.change_date_type(QDateTime.currentDateTime().__str__()) ))




        self.initUI()

    def initUI(self):
        pass

    def change_date_type(self, date):
        dt = date[23:-1].split(', ')
        return '{}.{}.{} {}:{}'.format(dt[2], dt[1], dt[0], dt[3], dt[4])

    def delta_time(self, time1, time2):
        time1 = [int(i) for i in time1.split()[0].split('.')]
        time2 = [int(i) for i in time2.split()[0].split('.')]

        return (time1[2] * 365 + time1[1] * 30 + time1[0]) - (
                time2[2] * 365 + time2[1] * 30 + time2[0])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
