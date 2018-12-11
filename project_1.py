import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from PyQt5.QtCore import QDateTime, QDate, QTime

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 271, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(320, 30, 181, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.minutes_dial = QtWidgets.QDial(self.frame)
        self.minutes_dial.setGeometry(QtCore.QRect(80, 10, 81, 81))
        self.minutes_dial.setObjectName("minutes_dial")
        self.minutes_label = QtWidgets.QLabel(self.frame)
        self.minutes_label.setGeometry(QtCore.QRect(100, 90, 51, 16))
        self.minutes_label.setObjectName("minutes_label")
        self.hours_label = QtWidgets.QLabel(self.frame)
        self.hours_label.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.hours_label.setObjectName("hours_label")
        self.hours_dial = QtWidgets.QDial(self.frame)
        self.hours_dial.setGeometry(QtCore.QRect(10, 10, 81, 81))
        self.hours_dial.setObjectName("hours_dial")
        self.dateEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(10, 120, 161, 61))
        self.dateEdit.setObjectName("dateEdit")
        self.addEvent = QtWidgets.QPushButton(self.centralwidget)
        self.addEvent.setGeometry(QtCore.QRect(130, 410, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addEvent.setFont(font)
        self.addEvent.setObjectName("addEvent")
        self.descriptionText = QtWidgets.QTextEdit(self.centralwidget)
        self.descriptionText.setGeometry(QtCore.QRect(30, 270, 441, 101))
        self.descriptionText.setObjectName("descriptionText")
        self.event_description_label = QtWidgets.QLabel(self.centralwidget)
        self.event_description_label.setGeometry(QtCore.QRect(150, 230, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.event_description_label.setFont(font)
        self.event_description_label.setObjectName("event_description_label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 380, 481, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.frame.raise_()
        self.calendarWidget.raise_()
        self.addEvent.raise_()
        self.descriptionText.raise_()
        self.event_description_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionKek = QtWidgets.QAction(MainWindow)
        self.actionKek.setObjectName("actionKek")

        self.hours_dial.setSliderPosition(12)
        self.hours_dial.setRange(0, 23)

        self.minutes_dial.setSliderPosition(30)
        self.minutes_dial.setRange(0, 59)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minutes_label.setText(_translate("MainWindow", "Minutes"))
        self.hours_label.setText(_translate("MainWindow", "Hours"))
        self.addEvent.setText(_translate("MainWindow", "Изменить событие"))
        self.event_description_label.setText(_translate("MainWindow", "Название события"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionKek.setText(_translate("MainWindow", "  "))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createGoal = QtWidgets.QPushButton(self.centralwidget)
        self.createGoal.setGeometry(QtCore.QRect(450, 10, 271, 101))
        self.createGoal.setObjectName("createGoal")
        self.listGoals = QtWidgets.QListView(self.centralwidget)
        self.listGoals.setGeometry(QtCore.QRect(10, 220, 731, 301))
        self.listGoals.setObjectName("listGoals")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createGoal.setText(_translate("MainWindow", "Создать цель"))
        self.nearestGoals.setText(_translate("MainWindow", "Ближайшие цели"))






class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        global chng
        chng = ChangeGoal()
        chng.show()

class ChangeGoal(QMainWindow, Ui_ChangeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.calendarWidget.clicked.connect(self.selectDate)

        self.setFixedSize(521, 500)

        self.time = [12, 30]
        self.dateEdit.setTime(QTime(self.time[0], self.time[1]))
        self.dateEdit.setDate(QDate.currentDate())


        self.hours_dial.valueChanged.connect(self.destroy)
        self.minutes_dial.valueChanged.connect(self.destroy)

        self.dateEdit.dateChanged.connect(self.date_changed)

        self.dateEdit.timeChanged.connect(self.time_changed)

        self.addEvent.clicked.connect(self.event_add)

    def event_add(self):
        txt = self.descriptionText.toPlainText()
        if txt == '':
            return

        self.descriptionText.setText('')



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
