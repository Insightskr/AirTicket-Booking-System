# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_passenger.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookPassengerForm(object):
    def setupUi(self, BookPassengerForm):
        BookPassengerForm.setObjectName("BookPassengerForm")
        BookPassengerForm.resize(544, 404)
        self.gridLayout = QtWidgets.QGridLayout(BookPassengerForm)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(BookPassengerForm)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/常旅客.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(BookPassengerForm)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(486, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 20, 0, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_pass = QtWidgets.QPushButton(BookPassengerForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.new_pass.setFont(font)
        self.new_pass.setObjectName("new_pass")
        self.horizontalLayout.addWidget(self.new_pass)
        self.update_pas = QtWidgets.QPushButton(BookPassengerForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.update_pas.setFont(font)
        self.update_pas.setObjectName("update_pas")
        self.horizontalLayout.addWidget(self.update_pas)
        self.book = QtWidgets.QPushButton(BookPassengerForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.book.setFont(font)
        self.book.setObjectName("book")
        self.horizontalLayout.addWidget(self.book)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.passengertable = QtWidgets.QTableWidget(BookPassengerForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.passengertable.setFont(font)
        self.passengertable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.passengertable.setAlternatingRowColors(True)
        self.passengertable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.passengertable.setRowCount(10)
        self.passengertable.setObjectName("passengertable")
        self.passengertable.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.passengertable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.passengertable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.passengertable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.passengertable.setHorizontalHeaderItem(3, item)
        self.passengertable.horizontalHeader().setCascadingSectionResizes(False)
        self.passengertable.horizontalHeader().setStretchLastSection(True)
        self.passengertable.verticalHeader().setVisible(False)
        self.passengertable.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.passengertable, 2, 0, 1, 1)

        self.retranslateUi(BookPassengerForm)
        QtCore.QMetaObject.connectSlotsByName(BookPassengerForm)

    def retranslateUi(self, BookPassengerForm):
        _translate = QtCore.QCoreApplication.translate
        BookPassengerForm.setWindowTitle(_translate("BookPassengerForm", "常用旅客"))
        self.label.setText(_translate("BookPassengerForm", "常用旅客"))
        self.new_pass.setText(_translate("BookPassengerForm", "新增旅客"))
        self.update_pas.setText(_translate("BookPassengerForm", "修改资料"))
        self.book.setText(_translate("BookPassengerForm", "购买"))
        item = self.passengertable.horizontalHeaderItem(0)
        item.setText(_translate("BookPassengerForm", "旅客姓名"))
        item = self.passengertable.horizontalHeaderItem(1)
        item.setText(_translate("BookPassengerForm", "性别"))
        item = self.passengertable.horizontalHeaderItem(2)
        item.setText(_translate("BookPassengerForm", "身份证号"))
        item = self.passengertable.horizontalHeaderItem(3)
        item.setText(_translate("BookPassengerForm", "电话"))

