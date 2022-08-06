from PyQt5.Qt import Qt,QMouseEvent
from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter
from reportlab.lib import colors
import itertools
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Table, Spacer, TableStyle, SimpleDocTemplate,PageBreak,PageTemplate,NextPageTemplate
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
import sqlite3,sys,time,os,csv,io,pdfkit,shutil,datetime
from io import StringIO
from reportlab.pdfgen import canvas
import pandas as pd
import numpy as np
import tempfile
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SRMS")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1076, 586)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1076, 586))
        MainWindow.setBaseSize(QtCore.QSize(1076, 586))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setToolTipDuration(1)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TABS = QtWidgets.QTabWidget(self.centralwidget)
        self.TABS.setGeometry(QtCore.QRect(1, 0, 1300, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TABS.sizePolicy().hasHeightForWidth())
        self.TABS.setSizePolicy(sizePolicy)
        self.TABS.setMinimumSize(QtCore.QSize(800, 500))
        self.TABS.setMaximumSize(QtCore.QSize(1300, 16777215))
        self.TABS.setSizeIncrement(QtCore.QSize(40, 0))
        self.TABS.setBaseSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(20)
        font.setWeight(50)
        self.TABS.setFont(font)
        self.TABS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TABS.setStyleSheet("background-color:rgb(172, 248, 154);")
        self.TABS.setTabPosition(QtWidgets.QTabWidget.North)
        self.TABS.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.TABS.setDocumentMode(True)
        self.TABS.setMovable(True)
        self.TABS.setObjectName("TABS")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.sch_logo_frame = QtWidgets.QFrame(self.main_tab)
        self.sch_logo_frame.setGeometry(QtCore.QRect(130, 9, 161, 161))
        self.sch_logo_frame.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.sch_logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sch_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sch_logo_frame.setObjectName("sch_logo_frame")
        self.school_frame = QtWidgets.QFrame(self.main_tab)
        self.school_frame.setGeometry(QtCore.QRect(470, 10, 1071, 51))
        self.school_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.school_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.school_frame.setObjectName("school_frame")
        self.sch_inf_label = QtWidgets.QLabel(self.school_frame)
        self.sch_inf_label.setGeometry(QtCore.QRect(80, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setWeight(75)
        self.sch_inf_label.setFont(font)
        self.sch_inf_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sch_inf_label.setScaledContents(True)
        self.sch_inf_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sch_inf_label.setObjectName("sch_inf_label")
        self.frame_14 = QtWidgets.QFrame(self.main_tab)
        self.frame_14.setGeometry(QtCore.QRect(10, 220, 421, 301))
        self.frame_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_14.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.sch_name_label = QtWidgets.QLabel(self.frame_14)
        self.sch_name_label.setGeometry(QtCore.QRect(20, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sch_name_label.setFont(font)
        self.sch_name_label.setObjectName("sch_name_label")
        self.sch_type_label = QtWidgets.QLabel(self.frame_14)
        self.sch_type_label.setGeometry(QtCore.QRect(20, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sch_type_label.setFont(font)
        self.sch_type_label.setObjectName("sch_type_label")
        self.sch_categ_label = QtWidgets.QLabel(self.frame_14)
        self.sch_categ_label.setGeometry(QtCore.QRect(20, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sch_categ_label.setFont(font)
        self.sch_categ_label.setObjectName("sch_categ_label")
        self.sch_level_label = QtWidgets.QLabel(self.frame_14)
        self.sch_level_label.setGeometry(QtCore.QRect(20, 160, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sch_level_label.setFont(font)
        self.sch_level_label.setObjectName("sch_level_label")
        self.sch_type_entry = QtWidgets.QComboBox(self.frame_14)
        sch_types = ["BOYS","GIRLS","MIXED"]
        for i in sch_types:
                self.sch_type_entry.addItem(i)
        self.sch_type_entry.setGeometry(QtCore.QRect(160, 60, 201, 22))
        self.sch_type_entry.setObjectName("sch_type_entry")
        self.sch_categ_entry = QtWidgets.QComboBox(self.frame_14)
        sch_categ = ["DAY","BOARDING","BOARDING/DAY"]
        for i in sch_categ:
                self.sch_categ_entry.addItem(i)
        self.sch_categ_entry.setGeometry(QtCore.QRect(160, 110, 201, 22))
        self.sch_categ_entry.setObjectName("sch_categ_entry")
        self.sch_name_entry = QtWidgets.QLineEdit(self.frame_14)
        self.sch_name_entry.setGeometry(QtCore.QRect(160, 10, 201, 20))
        self.sch_name_entry.setObjectName("sch_name_entry")
        self.sch_level_entry = QtWidgets.QComboBox(self.frame_14)
        sch_level = ["SUB COUNTY","COUNTY","EXTRA COUNTY","NATIONAL"]
        for x in sch_level:
                self.sch_level_entry.addItem(x)
        self.sch_level_entry.setGeometry(QtCore.QRect(160, 160, 201, 22))
        self.sch_level_entry.setObjectName("sch_level_entry")
        self.sch_address_entry = QtWidgets.QLineEdit(self.frame_14)
        self.sch_address_entry.setGeometry(QtCore.QRect(160, 210, 201, 20))
        self.sch_address_entry.setObjectName("sch_address_entry")
        self.sch_address_label = QtWidgets.QLabel(self.frame_14)
        self.sch_address_label.setGeometry(QtCore.QRect(20, 210, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sch_address_label.setFont(font)
        self.sch_address_label.setObjectName("sch_address_label")
        self.save_sch_info_but = QtWidgets.QPushButton(self.frame_14)
        self.save_sch_info_but.setGeometry(QtCore.QRect(110, 250, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_sch_info_but.setFont(font)
        self.save_sch_info_but.setStyleSheet("color: rgb(55, 55, 55);")
        self.save_sch_info_but.setFlat(True)
        self.save_sch_info_but.setObjectName("save_sch_info_but")
        self.sch_logo_but = QtWidgets.QCommandLinkButton(self.main_tab)
        self.sch_logo_but.setGeometry(QtCore.QRect(130, 180, 168, 31))
        self.sch_logo_but.setObjectName("sch_logo_but")
        self.frame_15 = QtWidgets.QFrame(self.main_tab)
        self.frame_15.setGeometry(QtCore.QRect(440, -1, 20, 531))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.sch_info_disply_frame = QtWidgets.QFrame(self.main_tab)
        self.sch_info_disply_frame.setGeometry(QtCore.QRect(470, 70, 601, 391))
        self.sch_info_disply_frame.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.sch_info_disply_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sch_info_disply_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sch_info_disply_frame.setObjectName("sch_info_disply_frame")
        self.exit_area_frame = QtWidgets.QFrame(self.main_tab)
        self.exit_area_frame.setGeometry(QtCore.QRect(500, 470, 531, 51))
        self.exit_area_frame.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.exit_area_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exit_area_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exit_area_frame.setObjectName("frame_25")
        self.download_analysis_but = QtWidgets.QPushButton(self.exit_area_frame)
        self.download_analysis_but.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.download_analysis_but.setFont(font)
        self.download_analysis_but.setFlat(True)
        self.download_analysis_but.setObjectName("blank_but")
        self.about_dev_but = QtWidgets.QPushButton(self.exit_area_frame)
        self.about_dev_but.setGeometry(QtCore.QRect(80, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.about_dev_but.setFont(font)
        self.about_dev_but.setFlat(True)
        self.about_dev_but.setObjectName("blank_but_2")
        self.exit_button = QtWidgets.QPushButton(self.exit_area_frame)
        self.exit_button.setGeometry(QtCore.QRect(380, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setFlat(True)
        self.exit_button.setObjectName("exit_button")
        self.TABS.addTab(self.main_tab, "")
        self.learners_tab = QtWidgets.QWidget()
        self.learners_tab.setObjectName("learners_tab")
        self.frame_5 = QtWidgets.QFrame(self.learners_tab)
        self.frame_5.setGeometry(QtCore.QRect(10, 70, 421, 461))
        self.frame_5.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.gender_label = QtWidgets.QLabel(self.frame_5)
        self.gender_label.setGeometry(QtCore.QRect(30, 270, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.gender_label.setFont(font)
        self.gender_label.setObjectName("gender_label")
        self.gender_combo = QtWidgets.QComboBox(self.frame_5)
        self.gender_combo.addItems(["Select Gender","MALE","FEMALE","OTHER"])
        self.gender_combo.setGeometry(QtCore.QRect(150, 270, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gender_combo.setFont(font)
        self.gender_combo.setObjectName("gender_combo")
        self.class_label = QtWidgets.QLabel(self.frame_5)
        self.class_label.setGeometry(QtCore.QRect(30, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.class_label.setFont(font)
        self.class_label.setObjectName("class_label")
        self.adm_label = QtWidgets.QLabel(self.frame_5)
        self.adm_label.setGeometry(QtCore.QRect(30, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.adm_label.setFont(font)
        self.adm_label.setObjectName("adm_label")
        self.adm_entry = QtWidgets.QLineEdit(self.frame_5)
        self.adm_entry.setPlaceholderText("Learner's Admission Number")
        self.adm_entry.setGeometry(QtCore.QRect(150, 70, 241, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.adm_entry.setFont(font)
        self.adm_entry.setObjectName("adm_entry")
        self.parent_label = QtWidgets.QLabel(self.frame_5)
        self.parent_label.setGeometry(QtCore.QRect(30, 380, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.parent_label.setFont(font)
        self.parent_label.setObjectName("parent_label")
        self.stream_label = QtWidgets.QLabel(self.frame_5)
        self.stream_label.setGeometry(QtCore.QRect(30, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.stream_label.setFont(font)
        self.stream_label.setObjectName("stream_label")
        self.leaner_label = QtWidgets.QLabel(self.frame_5)
        self.leaner_label.setGeometry(QtCore.QRect(30, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.leaner_label.setFont(font)
        self.leaner_label.setLineWidth(0)
        self.leaner_label.setObjectName("leaner_label")
        self.category_label = QtWidgets.QLabel(self.frame_5)
        self.category_label.setGeometry(QtCore.QRect(30, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.category_label.setFont(font)
        self.category_label.setObjectName("category_label")
        self.parent_entry = QtWidgets.QLineEdit(self.frame_5)
        self.parent_entry.setPlaceholderText("Parent/Guardian's Name")
        self.parent_entry.setGeometry(QtCore.QRect(150, 380, 241, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parent_entry.setFont(font)
        self.parent_entry.setObjectName("parent_entry")
        self.categ_combo = QtWidgets.QComboBox(self.frame_5)
        categories = ["Select Category","BOARDING","DAY SCHOOL"]
        for i in categories:
            self.categ_combo.addItem(i)
        self.categ_combo.setGeometry(QtCore.QRect(150, 220, 241, 20))
        self.county_label = QtWidgets.QLabel(self.frame_5)
        self.county_label.setGeometry(QtCore.QRect(30, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.county_label.setFont(font)
        self.county_label.setObjectName("county_label")
        self.county_combo = QtWidgets.QComboBox(self.frame_5)
        counties_list = ["Select County","SIAYA","MIGORI","BONDO","EMBU","KISUMU","NAIROBI","NAKURU","KWALE","MOMBASA","BUNGOMA","KILIFI","KAJIADO","BUSIA","KAKAMEGA","OTHER"]
        for i in counties_list:
            self.county_combo.addItem(i)
        self.county_combo.setGeometry(QtCore.QRect(150, 330, 241, 22))
        font = QtGui.QFont()
        font.setWeight(75)
        self.county_combo.setFont(font)
        self.county_combo.setObjectName("county_combo")
        self.stream_combo_2 = QtWidgets.QComboBox(self.frame_5)
        streams = ["Select Stream","EAGLE","HAWK"]
        for i in streams:
            self.stream_combo_2.addItem(i)
        self.stream_combo_2.setGeometry(QtCore.QRect(150, 170, 241, 22))
        font = QtGui.QFont()
        font.setWeight(75)
        self.stream_combo_2.setFont(font)
        self.stream_combo_2.setObjectName("stream_combo_2")
        self.parent_contact_label = QtWidgets.QLabel(self.frame_5)
        self.parent_contact_label.setGeometry(QtCore.QRect(30, 430, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        self.parent_contact_label.setFont(font)
        self.parent_contact_label.setObjectName("parent_contact_label")
        self.parent_contact_entry = QtWidgets.QLineEdit(self.frame_5)
        self.parent_contact_entry.setPlaceholderText("Parent/Guardian's Phone Number")
        self.parent_contact_entry.setGeometry(QtCore.QRect(150, 430, 241, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        self.parent_contact_entry.setFont(font)
        self.parent_contact_entry.setObjectName("parent_contact_entry")
        self.class_combo_2 = QtWidgets.QComboBox(self.frame_5)
        classes_list = ["Select Class","FORM I","FORM II","FORM III","FORM IV"]
        for i in classes_list:
                self.class_combo_2.addItem(i)
        self.class_combo_2.setGeometry(QtCore.QRect(150, 120, 241, 22))
        font = QtGui.QFont()
        font.setWeight(75)
        self.class_combo_2.setFont(font)
        self.class_combo_2.setObjectName("class_combo_2")
        self.leaner_entry = QtWidgets.QLineEdit(self.frame_5)
        self.leaner_entry.setPlaceholderText("Learner's Full Name")
        self.leaner_entry.setGeometry(QtCore.QRect(150, 20, 241, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        self.leaner_entry.setFont(font)
        self.leaner_entry.setObjectName("leaner_entry")
        self.frame_6 = QtWidgets.QFrame(self.learners_tab)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 421, 61))
        self.frame_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.727273, y1:0.097, x2:0.847, y2:0.903773, stop:0.225 rgba(30, 43, 97, 73), stop:0.420455 rgba(124, 115, 53, 146), stop:0.585227 rgba(86, 99, 7, 133), stop:0.767045 rgba(136, 106, 22, 126), stop:0.835227 rgba(118, 99, 32, 124), stop:0.935 rgba(72, 56, 13, 70), stop:1 rgba(35, 40, 3, 255));")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.feed_deta_label = QtWidgets.QLabel(self.frame_6)
        self.feed_deta_label.setGeometry(QtCore.QRect(90, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.feed_deta_label.setFont(font)
        self.feed_deta_label.setAcceptDrops(True)
        self.feed_deta_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.9375, x2:1, y2:0, stop:0 rgba(41, 70, 41, 214), stop:1 rgba(255, 255, 255, 255));")
        self.feed_deta_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.feed_deta_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.feed_deta_label.setScaledContents(True)
        self.feed_deta_label.setAlignment(QtCore.Qt.AlignCenter)
        self.feed_deta_label.setWordWrap(True)
        self.feed_deta_label.setObjectName("feed_deta_label")
        self.frame_16 = QtWidgets.QFrame(self.learners_tab)
        self.frame_16.setGeometry(QtCore.QRect(470, 10, 601, 511))
        self.frame_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.727273, y1:0.097, x2:0.847, y2:0.903773, stop:0.225 rgba(30, 43, 97, 73), stop:0.420455 rgba(124, 115, 53, 146), stop:0.585227 rgba(86, 99, 7, 133), stop:0.767045 rgba(136, 106, 22, 126), stop:0.835227 rgba(118, 99, 32, 124), stop:0.935 rgba(72, 56, 13, 70), stop:1 rgba(35, 40, 3, 255));")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.add_learner_frame = QtWidgets.QFrame(self.frame_16)
        self.add_learner_frame.setGeometry(QtCore.QRect(40, 409, 521, 91))
        self.add_learner_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.add_learner_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.add_learner_frame.setLineWidth(5)
        self.add_learner_frame.setMidLineWidth(-4)
        self.add_learner_frame.setObjectName("add_learner_frame")
        self.add_leaner_but = QtWidgets.QPushButton(self.add_learner_frame)
        self.add_leaner_but.setGeometry(QtCore.QRect(70, 30, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_leaner_but.setFont(font)
        self.add_leaner_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_leaner_but.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_leaner_but.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.add_leaner_but.setObjectName("add_leaner_but")
        self.frame_7 = QtWidgets.QFrame(self.frame_16)
        self.frame_7.setGeometry(QtCore.QRect(40, 10, 521, 371))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(1)
        self.frame_7.setMidLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.upload_photo_frame = QtWidgets.QFrame(self.frame_7)
        self.upload_photo_frame.setGeometry(QtCore.QRect(140, 50, 231, 221))
        self.upload_photo_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.upload_photo_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.upload_photo_frame.setLineWidth(5)
        self.upload_photo_frame.setObjectName("upload_photo_frame")
        self.upload_photo_but = QtWidgets.QCommandLinkButton(self.frame_7)
        self.upload_photo_but.setGeometry(QtCore.QRect(180, 300, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.upload_photo_but.setFont(font)
        self.upload_photo_but.setStatusTip("")
        self.upload_photo_but.setAutoExclusive(True)
        self.upload_photo_but.setAutoDefault(True)
        self.upload_photo_but.setDefault(True)
        self.upload_photo_but.setObjectName("upload_photo_but")
        self.frame_19 = QtWidgets.QFrame(self.learners_tab)
        self.frame_19.setGeometry(QtCore.QRect(440, -10, 21, 541))
        font = QtGui.QFont()
        font.setWeight(50)
        self.frame_19.setFont(font)
        self.frame_19.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.frame_19.setAcceptDrops(True)
        self.frame_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_19.setLineWidth(1)
        self.frame_19.setObjectName("frame_19")
        self.TABS.addTab(self.learners_tab, "")
        self.marks_tab = QtWidgets.QWidget()
        self.marks_tab.setObjectName("marks_tab")
        self.marks_table = QtWidgets.QTableWidget(self.marks_tab)
        self.marks_table.setGeometry(QtCore.QRect(10, 80, 1061, 401))
        self.marks_table.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(10)
        font.setWeight(10)
        self.marks_table.setFont(font)
        self.marks_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.marks_table.setFrameShape(QtWidgets.QFrame.Box)
        self.marks_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.marks_table.setLineWidth(2)
        self.marks_table.setMidLineWidth(2)
        self.marks_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.marks_table.setAlternatingRowColors(True)
        self.marks_table.setGridStyle(QtCore.Qt.SolidLine)
        self.marks_table.setObjectName("marks_table")
        self.marks_table.setColumnCount(16)
        self.marks_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks_table.setHorizontalHeaderItem(15, item)
        self.frame_9 = QtWidgets.QFrame(self.marks_tab)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 1061, 61))        
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setLineWidth(2)
        self.frame_9.setMidLineWidth(1)
        self.frame_9.setObjectName("frame_9")
        self.year_combo = QtWidgets.QComboBox(self.frame_9)
        self.years=["Year","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030",'2031','2032','2033','2034','2035','2036','2037','2038','2039','2040']
        for i in self.years:
            self.year_combo.addItem(i)
        self.year_combo.setGeometry(QtCore.QRect(500, 20, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_combo.setFont(font)
        self.year_combo.setObjectName("year_combo")
        self.class_combo = QtWidgets.QComboBox(self.frame_9)
        self.year_combo.currentTextChanged.connect(self.select_year)
        self.classes = ["Select class","FORM I","FORM II","FORM III","FORM IV"]
        for x in self.classes:
            self.class_combo.addItem(x)
        self.class_combo.setGeometry(QtCore.QRect(80, 20, 111, 22))
        font.setPointSize(10)
        self.class_combo.setFont(font)
        self.class_combo.setObjectName("class_combo")
        '''
        self.stream_combo = QtWidgets.QComboBox(self.frame_9)
        self.streams = ["Select stream","EAGLE","HAWK"]

        for any in self.streams:
            self.stream_combo.addItem(any)
        self.stream_combo.setGeometry(QtCore.QRect(300, 20, 111, 22))
        font.setPointSize(10)
        self.stream_combo.setFont(font)
        self.stream_combo.setObjectName("stream_combo")
        self.stream_combo.currentTextChanged.connect(self.view_marks_streamwise)
        '''
        self.term_combo = QtWidgets.QComboBox(self.frame_9)
        self.terms = ["Select term","TERM I","TERM I(MID)","TERM II","TERM II(MID)","TERM III","TERM III(MID),",'KCSE']
        for any in self.terms:
            self.term_combo.addItem(any)
        self.term_combo.setGeometry(QtCore.QRect(280, 20, 111, 22))
        font.setPointSize(10)
        self.term_combo.setFont(font)
        self.term_combo.setObjectName("term_combo")
        self.term_combo.currentTextChanged.connect(self.terms_per_year)
        self.exam_combo = QtWidgets.QComboBox(self.frame_9)
        self.exam_combo.addItems(["Exams to analyze","1","2","3"])
        self.exam_combo.setGeometry(QtCore.QRect(710, 20, 111, 21))
        self.exam_combo.setObjectName("exam_combo")
        self.exam_combo.currentTextChanged.connect(self.select_exam_combo)
        self.label_33 = QtWidgets.QLabel(self.frame_9)
        self.label_33.setGeometry(QtCore.QRect(660, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setLineWidth(3)
        self.label_33.setObjectName("label_33")
        self.label_31 = QtWidgets.QLabel(self.frame_9)
        self.label_31.setGeometry(QtCore.QRect(10, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(3)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_9)
        self.label_32.setGeometry(QtCore.QRect(220, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setLineWidth(3)
        self.label_32.setObjectName("label_32")
        self.term_label = QtWidgets.QLabel(self.frame_9)
        self.term_label.setGeometry(QtCore.QRect(440, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.term_label.setFont(font)
        self.term_label.setLineWidth(3)
        self.term_label.setObjectName("term_label")
        self.uploadfromexcel_but = QtWidgets.QCommandLinkButton(self.frame_9)
        self.uploadfromexcel_but.setGeometry(QtCore.QRect(890, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.uploadfromexcel_but.setFont(font)
        self.uploadfromexcel_but.setObjectName("upload_from_excel_but")
        self.save_marks_but = QtWidgets.QPushButton(self.marks_tab)
        self.save_marks_but.setGeometry(QtCore.QRect(340, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_marks_but.setFont(font)
        self.save_marks_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_marks_but.setObjectName("save_marks_but")
        self.delete_marks_but = QtWidgets.QPushButton(self.marks_tab)
        self.delete_marks_but.setGeometry(QtCore.QRect(550, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_marks_but.setFont(font)
        self.delete_marks_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_marks_but.setMouseTracking(True)
        self.delete_marks_but.setTabletTracking(True)
        self.delete_marks_but.setObjectName("delete_marks_but")
        self.TABS.addTab(self.marks_tab, "")
        self.analysi_tab = QtWidgets.QWidget()
        self.analysi_tab.setObjectName("analysi_tab")
        self.analyze_area_frame = QtWidgets.QFrame(self.analysi_tab)
        self.analyze_area_frame.setGeometry(QtCore.QRect(10, 10, 1061, 511))
        self.analyze_area_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analyze_area_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyze_area_frame.setObjectName("frame_10")
        self.analysis_frame = QtWidgets.QFrame(self.analyze_area_frame)
        self.analysis_frame.setGeometry(QtCore.QRect(10, 60, 1041, 371))
        self.analysis_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.analysis_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.analysis_frame.setObjectName("analysis_frame")
        self.analyz_but_frame = QtWidgets.QFrame(self.analyze_area_frame)
        self.analyz_but_frame.setGeometry(QtCore.QRect(70, 440, 931, 51))
        self.analyz_but_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analyz_but_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyz_but_frame.setObjectName("analyz_but_frame")
        self.analysis_table = QTableWidget(self.analysis_frame)
        self.analysis_table.setGeometry(QtCore.QRect(10, 10, 1021, 350))
        self.analysis_table.setAlternatingRowColors(True)
        self.generate_but = QtWidgets.QPushButton(self.analyz_but_frame)
        self.generate_but.setGeometry(QtCore.QRect(620, 12, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generate_but.setFont(font)
        self.generate_but.setObjectName("generate_but")
        self.get_results_but = QtWidgets.QPushButton(self.analyz_but_frame)
        self.get_results_but.setGeometry(QtCore.QRect(360, 12, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.get_results_but.setFont(font)
        self.get_results_but.setObjectName("get_results_but")
        self.analyze_but = QtWidgets.QPushButton(self.analyz_but_frame)
        self.analyze_but.setGeometry(QtCore.QRect(100, 12, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.analyze_but.setFont(font)
        self.analyze_but.setObjectName("analyze_but")
        self.frame_22 = QtWidgets.QFrame(self.analyze_area_frame)
        self.frame_22.setGeometry(QtCore.QRect(80, 10, 891, 41))
        self.frame_22.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.choose_class_label = QtWidgets.QLabel(self.frame_22)
        self.choose_class_label.setGeometry(QtCore.QRect(50, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.choose_class_label.setFont(font)
        self.choose_class_label.setObjectName("choose_class_label")
        self.choose_class_combo = QtWidgets.QComboBox(self.frame_22)
        self.choose_class_combo.addItems(["Select class","FORM I","FORM II","FORM III","FORM IV"])
        self.choose_class_combo.setGeometry(QtCore.QRect(120, 10, 91, 21))
        self.choose_class_combo.setObjectName("choose_class_combo")
        self.choose_class_combo.currentTextChanged.connect(self.choose_class_comboh)
        '''
        self.choose_stream_label = QtWidgets.QLabel(self.frame_22)
        self.choose_stream_label.setGeometry(QtCore.QRect(260, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.choose_stream_label.setFont(font)
        self.choose_stream_label.setObjectName("choose_stream_label")
        
        self.choose_stream_combo = QtWidgets.QComboBox(self.frame_22)
        self.choose_stream_combo.addItems(["Select stream","EAGLE","HAWK"])
        self.choose_stream_combo.setGeometry(QtCore.QRect(330, 10, 91, 21))
        self.choose_stream_combo.setObjectName("choose_stream_combo")
        self.choose_stream_combo.currentTextChanged.connect(self.choose_stream_comboh)
        
        self.choose_term_label = QtWidgets.QLabel(self.frame_22)
        self.choose_term_label.setGeometry(QtCore.QRect(460, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.choose_term_label.setFont(font)
        self.choose_term_label.setObjectName("choose_term_label")
        '''
        self.choose_term_combo = QtWidgets.QComboBox(self.frame_22)
        self.choose_term_combo.addItems(["Select term","TERM I","TERM I(MID)","TERM II","TERM II(MID)","TERM III","TERM III(MID)",'KCSE'])
        self.choose_term_combo.setGeometry(QtCore.QRect(370, 10, 121, 21))
        self.choose_term_combo.setObjectName("choose_term_combo")
        self.choose_term_combo.currentTextChanged.connect(self.choose_term)
        '''
        self.choose_year_label = QtWidgets.QLabel(self.frame_22)
        self.choose_year_label.setGeometry(QtCore.QRect(680, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.choose_year_label.setFont(font)
        self.choose_year_label.setObjectName("choose_year_label")
        '''
        self.choose_year_combo = QtWidgets.QComboBox(self.frame_22)
        self.choose_year_combo.addItems(["Year","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030",'2031','2032','2033','2034','2035','2036','2037','2038','2039','2040'])
        self.choose_year_combo.setGeometry(QtCore.QRect(650, 10, 91, 21))
        self.choose_year_combo.setObjectName("choose_year_combo")
        self.choose_year_combo.currentTextChanged.connect(self.choose_year)
        self.TABS.addTab(self.analysi_tab, "")
        self.teachers_tab = QtWidgets.QWidget()
        self.teachers_tab.setObjectName("teachers_tab")
        self.frame = QtWidgets.QFrame(self.teachers_tab)
        self.frame.setGeometry(QtCore.QRect(10, 20, 331, 51))
        self.frame.setStyleSheet("background-color: rgb(129, 130, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(3)
        self.frame.setObjectName("frame")
        self.teacher_data_lab = QtWidgets.QLabel(self.frame)
        self.teacher_data_lab.setGeometry(QtCore.QRect(90, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.teacher_data_lab.setFont(font)
        self.teacher_data_lab.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.teacher_data_lab.setFrameShadow(QtWidgets.QFrame.Plain)
        self.teacher_data_lab.setLineWidth(0)
        self.teacher_data_lab.setMidLineWidth(1)
        self.teacher_data_lab.setObjectName("teacher_data_lab")
        self.teacher_data_frame = QtWidgets.QFrame(self.teachers_tab)
        self.teacher_data_frame.setGeometry(QtCore.QRect(10, 80, 331, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teacher_data_frame.setFont(font)
        self.teacher_data_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.teacher_data_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.teacher_data_frame.setMidLineWidth(1)
        self.teacher_data_frame.setObjectName("teacher_data_frame")
        self.t_label = QtWidgets.QLabel(self.teacher_data_frame)
        self.t_label.setGeometry(QtCore.QRect(20, 60, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_label.setFont(font)
        self.t_label.setObjectName("t_label")
        self.sub1_label = QtWidgets.QLabel(self.teacher_data_frame)
        self.sub1_label.setGeometry(QtCore.QRect(20, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sub1_label.setFont(font)
        self.sub1_label.setObjectName("sub1_label")
        self.sub2_label = QtWidgets.QLabel(self.teacher_data_frame)
        self.sub2_label.setGeometry(QtCore.QRect(20, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sub2_label.setFont(font)
        self.sub2_label.setObjectName("sub2_label")
        self.t_emp_label = QtWidgets.QLabel(self.teacher_data_frame)
        self.t_emp_label.setGeometry(QtCore.QRect(20, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_emp_label.setFont(font)
        self.t_emp_label.setObjectName("t_emp_label")
        self.t_gender_label = QtWidgets.QLabel(self.teacher_data_frame)
        self.t_gender_label.setGeometry(QtCore.QRect(20, 260, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_gender_label.setFont(font)
        self.t_gender_label.setObjectName("t_gender_label")
        self.t_add_but = QtWidgets.QPushButton(self.teacher_data_frame)
        self.t_add_but.setGeometry(QtCore.QRect(60, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.t_add_but.setFont(font)
        self.t_add_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.t_add_but.setObjectName("t_add_but")
        self.t_edit_but = QtWidgets.QPushButton(self.teacher_data_frame)
        self.t_edit_but.setGeometry(QtCore.QRect(204, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.t_edit_but.setFont(font)
        self.t_edit_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.t_edit_but.setObjectName("t_edit_but")
        self.t_delete_but = QtWidgets.QPushButton(self.teacher_data_frame)
        self.t_delete_but.clicked.connect(self.delete_teacher)
        self.t_delete_but.setGeometry(QtCore.QRect(30, 400, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.t_delete_but.setFont(font)
        self.t_delete_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.t_delete_but.setObjectName("t_delete_but")

        self.t_print_but = QtWidgets.QPushButton(self.teacher_data_frame)
        self.t_print_but.setGeometry(QtCore.QRect(234, 400, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.t_print_but.setFont(font)
        self.t_print_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.t_print_but.setObjectName("t_print_but")

        self.t_contact_label = QtWidgets.QLabel(self.teacher_data_frame)
        self.t_contact_label.setGeometry(QtCore.QRect(20, 310, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)                    
        font.setWeight(75)
        self.t_contact_label.setFont(font)
        self.t_contact_label.setObjectName("t_contact_label")
        self.t_name_entry = QtWidgets.QLineEdit(self.teacher_data_frame)###########################################################
        self.t_name_entry.setGeometry(QtCore.QRect(120, 60, 191, 20))
        self.t_name_entry.setObjectName("t_name_entry")
        self.t_name_entry.setPlaceholderText("Teacher's full name")
        self.t_contact_entry = QtWidgets.QLineEdit(self.teacher_data_frame)
        self.t_contact_entry.setGeometry(QtCore.QRect(120, 310, 191, 20))
        self.t_contact_entry.setObjectName("t_contact_entry")
        self.t_contact_entry.setPlaceholderText("Phone Number")
        self.t_gender_combo = QtWidgets.QComboBox(self.teacher_data_frame)
        self.t_gender_combo.setGeometry(QtCore.QRect(120, 260, 191, 20))
        self.t_gender_combo.setObjectName("t_gender_combo")#end
        tgender_list = ["Select Gender","MALE","FEMALE","OTHER"]
        for i in tgender_list:
            self.t_gender_combo.addItem(i)
        self.t_emp_combo = QtWidgets.QComboBox(self.teacher_data_frame)
        self.t_emp_combo.setGeometry(QtCore.QRect(120, 210, 194, 22))
        self.t_emp_combo.setObjectName("t_emp_combo")
        employer_list = ["Choose Employer","TSC","BOM","TSC INTERN","TP","OTHER"]
        for i in employer_list:
            self.t_emp_combo.addItem(i)
        self.sub2_combo = QtWidgets.QComboBox(self.teacher_data_frame)
        self.sub2_combo.setGeometry(QtCore.QRect(120, 160, 194, 22))
        self.sub2_combo.setObjectName("sub2_combo")
        subject2_list = ["Select Subject II","ENGLISH","KISWAHILI","MATHS","BIOLOGY","PHYSICS","CHEMISTRY","HISTORY","GEOGRAPHY","CRE","IRE","AGRICULTURE","H/SCIENCE","B/STUDIES","COMPUTER","FRENCH","GERMAN","MUSIC","LITERATURE","P.E","LIFE SKILLS","OTHER"]
        for i in subject2_list:
            self.sub2_combo.addItem(i)
        self.sub1_combo = QtWidgets.QComboBox(self.teacher_data_frame)
        self.sub1_combo.setGeometry(QtCore.QRect(120, 110, 194, 22))
        self.sub1_combo.setObjectName("sub1_combo")
        subject1_list = ["Select a subject","BIOLOGY","ENGLISH","KISWAHILI","MATHS","PHYSICS","CHEMISTRY","HISTORY","GEOGRAPHY","CRE","IRE","AGRICULTURE","H/SCIENCE","B/STUDIES","COMPUTER","FRENCH","GERMAN","MUSIC","LITERATURE","P.E","LIFE SKILLS","OTHER"]
        for i in subject1_list:
            self.sub1_combo.addItem(i)
        self.t_code_entry = QtWidgets.QLineEdit(self.teacher_data_frame)
        self.t_code_entry.setGeometry(QtCore.QRect(120, 10, 191, 20))
        self.t_code_entry.setObjectName("t_code_entry")
        self.t_code_entry.setPlaceholderText("Teacher's Code")
        self.t_code = QtWidgets.QLabel(self.teacher_data_frame)
        self.t_code.setGeometry(QtCore.QRect(20, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_code.setFont(font)
        self.t_code.setObjectName("t_code")
        self.frame_3 = QtWidgets.QFrame(self.teachers_tab)
        self.frame_3.setGeometry(QtCore.QRect(370, 20, 701, 501))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.teachers_table = QtWidgets.QTableWidget(self.frame_3)
        self.teachers_table.setGeometry(QtCore.QRect(10, 60, 681, 431))
        self.teachers_table.setMinimumSize(QtCore.QSize(30, 0))
        self.teachers_table.setFrameShape(QtWidgets.QFrame.Box)
        self.teachers_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.teachers_table.setLineWidth(1)
        self.teachers_table.setMidLineWidth(1)
        self.teachers_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.teachers_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.teachers_table.setAlternatingRowColors(True)
        self.teachers_table.setObjectName("teachers_table")
        self.teachers_table.setColumnCount(7)
        self.teachers_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.teachers_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.teachers_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.teachers_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.teachers_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.teachers_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.teachers_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.teachers_table.setHorizontalHeaderItem(6, item)
        self.teachers_table.horizontalHeader().setDefaultSectionSize(100)
        self.teachers_table.verticalHeader().setMinimumSectionSize(18)
        self.t_search_by_combo = QtWidgets.QComboBox(self.frame_3)
        self.t_search_by_combo.addItems(["Code","Name"])
        self.t_search_by_combo.setGeometry(QtCore.QRect(110, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        self.t_search_by_combo.setFont(font)
        self.t_search_by_combo.setObjectName("t_search_by_combo")
        self.t_search_entry = QtWidgets.QLineEdit(self.frame_3)
        self.t_search_entry.setGeometry(QtCore.QRect(280, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        self.t_search_entry.setFont(font)
        self.t_search_entry.setObjectName("t_search_entry")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(10, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.t_search_but = QtWidgets.QPushButton(self.frame_3)
        self.t_search_but.clicked.connect(self.search_each_teacher)
        self.t_search_but.setGeometry(QtCore.QRect(490, 20, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_search_but.setFont(font)
        self.t_search_but.setObjectName("t_search_but")
        self.t_showall_but = QtWidgets.QPushButton(self.frame_3)
        self.t_showall_but.clicked.connect(self.fetch_teacher_data)
        self.t_showall_but.setGeometry(QtCore.QRect(590, 20, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_showall_but.setFont(font)
        self.t_showall_but.setObjectName("t_showall_but")
        self.TABS.addTab(self.teachers_tab, "")
        self.classes_tab = QtWidgets.QWidget()
        self.classes_tab.setObjectName("classes_tab")
        self.frame_11 = QtWidgets.QFrame(self.classes_tab)
        self.frame_11.setGeometry(QtCore.QRect(10, 10, 1061, 511))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        '''
        self.view_leaners_label = QtWidgets.QLabel(self.frame_11)
        self.view_leaners_label.setGeometry(QtCore.QRect(100, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.view_leaners_label.setFont(font)
        self.view_leaners_label.setObjectName("view_leaners_label")
        '''
        self.view_learners_combo = QtWidgets.QComboBox(self.frame_11)
        self.classes_to_view = ["Select class to view","FORM I","FORM II","FORM III","FORM IV"]
        for a in self.classes_to_view:
            self.view_learners_combo.addItem(a)
        self.view_learners_combo.setGeometry(QtCore.QRect(150, 10, 131, 31))
        self.view_learners_combo.setObjectName("view_learners_combo")
        self.view_learners_combo.currentTextChanged.connect(self.view_all_combo)
        self.class_combo.currentTextChanged.connect(self.view_class_combo)###################
        self.frame_23 = QtWidgets.QFrame(self.frame_11)
        self.frame_23.setGeometry(QtCore.QRect(10, 50, 1041, 451))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.classes_table = QtWidgets.QTableWidget(self.frame_23)
        self.classes_table.setGeometry(QtCore.QRect(10, 10, 1021, 441))
        self.classes_table.setRowCount(0)
        self.classes_table.setColumnCount(10)
        self.classes_table.setObjectName("classes_table")
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(9, item)
        self.classes_table.horizontalHeader().setDefaultSectionSize(104)
        self.view_all_learners_but = QtWidgets.QPushButton(self.frame_11)
        self.view_all_learners_but.setGeometry(QtCore.QRect(500, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.view_all_learners_but.setFont(font)
        self.view_all_learners_but.setAutoRepeat(True)
        self.view_all_learners_but.setFlat(True)
        self.view_all_learners_but.setObjectName("view_all_learners_but")
        #print but
        self.print_but = QtWidgets.QPushButton(self.frame_11)
        self.print_but.setGeometry(QtCore.QRect(850, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.print_but.setFont(font)
        self.print_but.setAutoRepeat(True)
        self.print_but.setFlat(True)
        self.print_but.setObjectName("print but")
        
        self.TABS.addTab(self.classes_tab, "")
        ###########################
        #self.hbox = QHBoxLayout(self.centralwidget)
        #self.stretch()
        #self.hbox.addWidget(self.TABS)
        #self.hbox.addWidget(self.averages_table)
        #self.stretch()
        #self.setLayout(self.hbox)
      
        #self.horizontalLayout.addWidget(self.table2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TABS.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SRMS ver 2.0.1"))
        self.sch_inf_label.setText(_translate("MainWindow", "SCHOOL INFORMATION"))
        self.sch_name_label.setText(_translate("MainWindow", "SCHOOL NAME"))
        self.sch_type_label.setText(_translate("MainWindow", "TYPE"))
        self.sch_categ_label.setText(_translate("MainWindow", "CATEGORY"))
        self.sch_level_label.setText(_translate("MainWindow", "LEVEL"))
        self.sch_address_label.setText(_translate("MainWindow", "ADDRESS"))
        self.save_sch_info_but.setText(_translate("MainWindow", "SAVE SCHOOL INFORMATION"))
        self.sch_logo_but.setText(_translate("MainWindow", "Choose School logo"))
        #self.download_analysis_but.setText(_translate("MainWindow", "Download Analysis"))
        #self.download_analysis_but.clicked.connect(self.download_analysis)
        self.about_dev_but.setText(_translate("MainWindow", "About Developer"))
        self.about_dev_but.clicked.connect(self.about_dev)
        self.exit_button.setText(_translate("MainWindow", "CLOSE"))
        self.exit_button.clicked.connect(self.exit_but)
        self.TABS.setTabText(self.TABS.indexOf(self.main_tab), _translate("MainWindow", "    MAIN   "))
        self.gender_label.setText(_translate("MainWindow", "GENDER"))
        self.class_label.setText(_translate("MainWindow", "CLASS"))
        self.adm_label.setText(_translate("MainWindow", "ADM"))
        self.parent_label.setText(_translate("MainWindow", "PARENT"))
        self.stream_label.setText(_translate("MainWindow", "STREAM"))
        self.leaner_label.setText(_translate("MainWindow", "NAME"))
        self.category_label.setText(_translate("MainWindow", "CATEGORY"))
        self.county_label.setText(_translate("MainWindow", "COUNTY"))
        self.parent_contact_label.setText(_translate("MainWindow", "PARENT PHONE"))
        self.feed_deta_label.setText(_translate("MainWindow", "  FEED LEARNER DETAILS"))
        #self.upload_learner_photo_lbl.setText(_translate("MainWindow", ''))
        #self.upload_learner_photo_lbl.setGeometry(QtCore.QRect(90, 10, 241, 41))
        #self.upload_learner_photo_lbl.setPixmap(_translate("MainWindow",(pixmap)))
        #self.upload_learner_photo_lbl.setText(_translate("MainWindow", ""))
        self.add_leaner_but.setText(_translate("MainWindow", "SAVE DETAILS"))
        self.add_leaner_but.clicked.connect(self.add_learner)
        self.upload_photo_but.setText(_translate("MainWindow", "Upload photo"))
        self.upload_photo_but.clicked.connect(self.learner_photo)
        self.TABS.setTabText(self.TABS.indexOf(self.learners_tab), _translate("MainWindow", "    LEARNERS   "))
        self.marks_table.setSortingEnabled(True)
        self.classes_table.setSortingEnabled(True)
        self.classes_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.analysis_table.setSortingEnabled(True)
        self.analysis_table.setEditTriggers(QAbstractItemView.NoEditTriggers) #Makes the table ineditable
        header0 = self.analysis_table.horizontalHeader()
        header1 = self.marks_table.horizontalHeader()
        header2 = self.classes_table.horizontalHeader()
        header3 = self.teachers_table.horizontalHeader()
        header0.setSectionResizeMode(QHeaderView.ResizeToContents)
        header1.setSectionResizeMode(QHeaderView.Stretch)
        header1.setSectionResizeMode(2,QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(QHeaderView.Stretch)
        header2.setSectionResizeMode(0,QHeaderView.ResizeToContents)
        header3.setSectionResizeMode(QHeaderView.Stretch)
        header3.setSectionResizeMode(0,QHeaderView.ResizeToContents)
        header3.setSectionResizeMode(1,QHeaderView.ResizeToContents)
        item = self.marks_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STREAM"))
        item = self.marks_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ADM"))
        item = self.marks_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.marks_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "KCPE"))
        item = self.marks_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ENG"))
        item = self.marks_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "KIS"))
        item = self.marks_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "MAT"))
        item = self.marks_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "BIO"))
        item = self.marks_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "PHY"))
        item = self.marks_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "CHE"))
        item = self.marks_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "HIS"))
        item = self.marks_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "GEO"))
        item = self.marks_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "CRE"))
        item = self.marks_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "AGR"))
        item = self.marks_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "H/SC"))
        item = self.marks_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "BST"))
        #self.label_33.setText(_translate("MainWindow", "YEAR"))
        #self.label_31.setText(_translate("MainWindow", "CLASS"))
        #self.choose_term_label.setText(_translate("MainWindow", "TERM"))
        #self.choose_year_label.setText(_translate("MainWindow", "YEAR"))
        #self.label_32.setText(_translate("MainWindow", "STREAM"))
        #self.term_label.setText(_translate("MainWindow", "TERM"))
        self.uploadfromexcel_but.setText(_translate("MainWindow", "Upload Exams"))
        self.uploadfromexcel_but.clicked.connect(self.upload_marks)
        self.save_marks_but.setText(_translate("MainWindow", "SAVE"))
        self.save_marks_but.clicked.connect(self.save_qtable)
        self.delete_marks_but.setText(_translate("MainWindow", "DELETE"))
        self.delete_marks_but.clicked.connect(self.delete_marks)
        self.TABS.setTabText(self.TABS.indexOf(self.marks_tab), _translate("MainWindow", "    MARKS   "))
        self.generate_but.setText(_translate("MainWindow", "Report Forms"))
        self.generate_but.clicked.connect(self.download_report)
        self.analyze_but.setText(_translate("MainWindow", "Analyze"))
        self.analyze_but.clicked.connect(self.analyze)
        self.get_results_but.setText(_translate("MainWindow", "Get Results"))
        self.get_results_but.clicked.connect(self.get_results)
        #self.choose_class_label.setText(_translate("MainWindow", "CLASS"))
        #self.choose_stream_label.setText(_translate("MainWindow", "STREAM"))
        self.TABS.setTabText(self.TABS.indexOf(self.analysi_tab), _translate("MainWindow", "   ANALYSIS     "   ))
        self.teacher_data_lab.setText(_translate("MainWindow", "TEACHER DATA"))
        self.t_label.setText(_translate("MainWindow", "NAME"))
        self.sub1_label.setText(_translate("MainWindow", "SUBJECT I"))
        self.sub2_label.setText(_translate("MainWindow", "SUBJECT II"))
        self.t_emp_label.setText(_translate("MainWindow", "EMPLOYER"))
        self.t_gender_label.setText(_translate("MainWindow", "GENDER"))
        self.t_add_but.setText(_translate("MainWindow", "ADD"))
        self.t_add_but.setStatusTip("Add")
        self.t_add_but.clicked.connect(self.add_teacher)######################teacher add but 
        self.t_edit_but.setText(_translate("MainWindow", "EDIT"))
        self.t_edit_but.clicked.connect(self.edit_teacher)
        self.t_delete_but.setText(_translate("MainWindow", "DELETE"))
        self.t_print_but.setText(_translate("MainWindow", "PRINT"))
        self.t_print_but.clicked.connect(self.print_teacher_details)
        self.t_contact_label.setText(_translate("MainWindow", "CONTACT"))
        self.t_code.setText(_translate("MainWindow", "CODE"))
        self.teachers_table.setSortingEnabled(True)
        self.teachers_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        item = self.teachers_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CODE"))
        item = self.teachers_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.teachers_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SUBJECT I"))
        item = self.teachers_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SUBJECT II"))
        item = self.teachers_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "EMPLOYER"))
        item = self.teachers_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "GENDER"))
        item = self.teachers_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CONTACT"))
        self.t_search_by_combo.setCurrentText(_translate("MainWindow", "Choose an option"))
        self.label_25.setText(_translate("MainWindow", "Search by"))
        self.t_search_but.setText(_translate("MainWindow", "SEARCH"))
        self.t_showall_but.setText(_translate("MainWindow", "SHOW ALL"))
        self.TABS.setTabText(self.TABS.indexOf(self.teachers_tab), _translate("MainWindow", "     STAFF      "))
        item = self.classes_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.classes_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ADM"))
        item = self.classes_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CLASS"))
        item = self.classes_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "STREAM"))
        item = self.classes_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CATEGORY"))
        item = self.classes_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "GENDER"))
        item = self.classes_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "COUNTY"))
        item = self.classes_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "PARENT"))
        item = self.classes_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "PARENT PHONE"))
        item = self.classes_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "PHOTO"))
        self.view_all_learners_but.setText(_translate("MainWindow", "View All Learners"))
        self.view_all_learners_but.clicked.connect(self.fetch_all_learner_data)
        self.print_but.setText(_translate("MainWindow", "Print"))
        self.print_but.clicked.connect(self.print_learner_details)
        self.TABS.setTabText(self.TABS.indexOf(self.classes_tab), _translate("MainWindow", "       VIEW      "))
        self.create_teacher_table()
        self.create_learner_table()
        self.fetch_teacher_data()
        self.fetch_learner_data()
        self.fetch_all_learner_data()
        #self.tget_cursor()
        #self.teachers_table.bind("<ButtonRelease-1>", self.tget_cursor)
    def create_teacher_table(self):
        try:
            conn = sqlite3.connect("mydb.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS teacher_data(t_code_info,t_name_info,t_sub1_info,
                t_sub2_info,t_emp_info,t_gender_info,t_contact_info,PRIMARY KEY(t_code_info))''');
            conn.commit()
            conn.close()
        except:
            QMessageBox.warning(MainWindow,"Failed","Teachers table has not been created. Call support on +254-725-109-389(Ptar*)")
    def create_learner_table(self):
        try:
            conn = sqlite3.connect("mydb.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS learner_data(ADM INT NOT NULL,NAME TEXT NOT NULL,
                CLASS TEXT NOT NULL,STREAM TEXT NOT NULL,CATEGORY TEXT NOT NULL,GENDER TEXT NOT NULL,COUNTY TEXT NOT NULL,
                PARENT TEXT NOT NULL,PARENT_PHONE TEXT NOT NULL,PHOTO BLOB NOT NULL,PRIMARY KEY(ADM))''')
            conn.commit()
            conn.close()
        except:
            QMessageBox.warning(MainWindow,"Failed","Learners table not created.Call support on +254-725-109-389(Ptar*)")
    def add_learner(self):
        if self.leaner_entry.text() == "":
            QMessageBox.information(MainWindow,"Warning","Learner's Full Name is mandatory.")
        elif self.adm_entry.text() == "":
            QMessageBox.information(MainWindow,"Warning","Learner's admission number is missing.")
        elif self.class_combo_2.currentText()== "Select Class":
            QMessageBox.information(MainWindow,"Warning","Select Class")
        elif self.stream_combo_2.currentText() == "Select Stream":
            QMessageBox.information(MainWindow,"Warning","Select Stream.")
        elif self.gender_combo.currentText() == "Select Gender":
            QMessageBox.information(MainWindow,"Warning","Select Gender")
        elif self.categ_combo.currentText() == "Select Category":
            QMessageBox.information(MainWindow,"Warning","Select Category")
        elif self.county_combo.currentText() == "Select County":
            QMessageBox.information(MainWindow,"Warning","Select County")
        elif self.parent_contact_entry.text() == "":
            QMessageBox.information(MainWindow,"Warning","Parent/Guardian's contact is mandatory")
        else:
            try:
                learner_info = self.leaner_entry.text()
                adm_info = self.adm_entry.text()
                class_info = self.class_combo_2.currentText()
                stream_info = self.stream_combo_2.currentText()
                categ_info = self.categ_combo.currentText()
                gender_info = self.gender_combo.currentText()
                county_info = self.county_combo.currentText()
                parent_info = self.parent_entry.text()
                parent_contact_info = self.parent_contact_entry.text()
                l_photo = self.photo.text()
                l_photo = self.convertToBinaryData()

                conn= sqlite3.connect("mydb.db")
                cur = conn.cursor()
                cur.execute("INSERT INTO learner_data(ADM,NAME,\
                    CLASS,STREAM,CATEGORY,GENDER,COUNTY,PARENT,PARENT_PHONE, PHOTO) VALUES(?,?,?,?,?,?,?,?,?,?)",(adm_info,learner_info,
                    class_info,stream_info,categ_info,gender_info,county_info,parent_info,parent_contact_info,l_photo))
                QMessageBox.information(MainWindow,"Success","Learner details successfully added.")
                conn.commit()
                self.fetch_learner_data()
                self.fetch_all_learner_data()
                self.clear()
                conn.close()
            except:
                QMessageBox.warning(MainWindow,"Warning","Learner not captured")
    def print_teacher_details(self):
        #This function grabs the currently displayed items in a table and saves as an excel file
        try:
            col_count = self.teachers_table.columnCount()
            row_count = self.teachers_table.rowCount()
            headers = [str(self.teachers_table.horizontalHeaderItem(i).text()) for i in range(col_count)]
            df_list = []
            for row in range(row_count):
                df_list2 = []
                for col in range(col_count):
                    table_item = self.teachers_table.item(row, col)
                    df_list2.append('' if table_item is None else str(table_item.text()))
                df_list.append(df_list2)
            print_t = pd.DataFrame(df_list, columns=headers)
            #Saving the data in a temporary file
            t_chers = tempfile.NamedTemporaryFile()
            print_t.to_csv(t_chers.name + '.csv',index=False)
            t_chers.flush()
            t_chers.seek(0)
            t_chers = t_chers.name + '.csv'
            #Saving the file ina user preferred location
            save_as_name = QFileDialog.getSaveFileName(MainWindow,"Save teachers list", os.path.expanduser("~/Documents"),"Save excel(*.csv))")
            if save_as_name:
                try:
                    with open(t_chers, 'r') as t_list, open(save_as_name[0], 'w') as named:
                        for line in t_list:
                            named.writelines(line)
                    QMessageBox.information(MainWindow, "Success", "Successfully saved.")
                except IOError:
                    QMessageBox.information(MainWindow, "******", "Nothing saved.")   
        except:
            QMessageBox.warning(MainWindow, "Failed", "Unsuccessfull.")
    def print_learner_details(self):
        #This function grabs the currently displayed items in a table and saves as an excel file
        try:
            col_count = self.classes_table.columnCount()
            row_count = self.classes_table.rowCount()
            headers = [str(self.classes_table.horizontalHeaderItem(i).text()) for i in range(col_count)]
            df_list = []
            for row in range(row_count):
                df_list2 = []
                for col in range(col_count):
                    table_item = self.classes_table.item(row, col)
                    df_list2.append('' if table_item is None else str(table_item.text()))
                df_list.append(df_list2)
            print_learner = pd.DataFrame(df_list, columns=headers)
            #Saving the data in a temporary file
            save_learner = tempfile.NamedTemporaryFile()
            print_learner.to_csv(save_learner.name + '.csv',index=False)
            save_learner.flush()
            save_learner.seek(0)
            save_learner = save_learner.name + '.csv'
            #Saving the file ina user preferred location
            save_as_learner = QFileDialog.getSaveFileName(MainWindow,"Save learners list", os.path.expanduser("~/Documents"),"Save excel(*.csv))")
            if save_as_learner:
                try:
                    with open(save_learner, 'r') as t_list, open(save_as_learner[0], 'w') as namesis:
                        for line in t_list:
                            namesis.writelines(line)
                    QMessageBox.information(MainWindow, "Success", "Successfully saved.")
                except IOError:
                    QMessageBox.information(MainWindow, "******", "Nothing saved.")
        except:
            QMessageBox.warning(MainWindow, "Failed", "Unsuccessfull.")
    def about_dev(self):      
        QMessageBox.information(MainWindow,"Developer"," 0725109389 - For enquiries and concerns.")
    def learner_photo(self):
        global imagePath
        fname = QFileDialog.getOpenFileName(MainWindow, 'Select learner photo',os.getenv('HOME'),"Image files (*.TIFF *.psd *.jpg *.gif *.png *.jpeg *.raw)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath).scaled(230,220)
        self.photo = QLabel(self.upload_photo_frame)
        self.photo.setPixmap(QPixmap(pixmap))
        self.photo.show()
    def convertToBinaryData(self):
        with open(imagePath, 'rb') as file:
            blobData = file.read()
        return blobData
    def fetch_all_learner_data(self):
        connection = sqlite3.connect("mydb.db")
        querry = "SELECT NAME,ADM,CLASS,STREAM,CATEGORY,GENDER,COUNTY,PARENT,PARENT_PHONE,PHOTO   FROM learner_data"
        result = connection.execute(querry)
        self.classes_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.classes_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                it = QTableWidgetItem()
                if column_number == 9:
                    pixmap = QPixmap()
                    pixmap.loadFromData(data)
                    it.setIcon(QIcon(pixmap))
                else:
                    it.setText(str(data))
                self.classes_table.setItem(row_number, column_number, it)
        connection.commit()
        connection.close()
    def choose_class_comboh(self):
        connection= sqlite3.connect("mydb.db")
        querry = "SELECT * FROM learner_data where CLASS = '" + self.choose_class_combo.currentText() + "'"
        result = connection.execute(querry)
        connection.commit()
        connection.close()
        '''
    def choose_stream_comboh(self):
        connection= sqlite3.connect("mydb.db")
        querry = "SELECT * FROM learner_data where STREAM = '" + self.choose_stream_combo.currentText() + "'"
        result = connection.execute(querry)
        connection.commit()
        connection.close()
        '''
    def terms_per_year(self):
        pass
    def select_year(self):
        pass
    def choose_year(self):
        pass
    def choose_term(self):
        pass
    def select_exam_combo(self):
        pass
    '''
    def view_marks_streamwise(self):
        connection= sqlite3.connect("mydb.db")
        querry = "SELECT STREAM,ADM,NAME FROM learner_data where STREAM = '" + self.stream_combo.currentText() + "'"
        result = connection.execute(querry)
        self.marks_table.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.marks_table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.marks_table.setItem(row_number,column_number,QTableWidgetItem(str(data))) 
        connection.commit()
        connection.close()
    '''
    def view_all_combo(self):
        connection= sqlite3.connect("mydb.db")
        querry = "SELECT NAME,ADM,CLASS,STREAM,CATEGORY,GENDER,COUNTY,PARENT,PARENT_PHONE FROM learner_data where \
        CLASS = '" + self.view_learners_combo.currentText() + "'"
        result = connection.execute(querry)
        self.classes_table.setRowCount(0)
        for row_number,row_data in enumerate(result):
                self.classes_table.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.classes_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        connection.commit()
        connection.close()
    def view_class_combo(self):
        connection= sqlite3.connect("mydb.db")
        querry = "SELECT STREAM,ADM,NAME FROM learner_data where CLASS = '" + self.class_combo.currentText() + "'"
        result = connection.execute(querry)
        self.marks_table.setRowCount(0)
        for row_number,row_data in enumerate(result):
                self.marks_table.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.marks_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        connection.commit()
        connection.close()
    def fetch_learner_data(self):
        connection= sqlite3.connect("mydb.db")
        querry = "SELECT STREAM,ADM,NAME FROM learner_data"
        result = connection.execute(querry)
        self.marks_table.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.marks_table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.marks_table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.commit()
        connection.close()
    def add_teacher(self):
        try:
            conn = sqlite3.connect("mydb.db")
            cur = conn.cursor()
            if self.t_code_entry.text() == "":
                QMessageBox.information(MainWindow,"Warning","Teacher's code is mandatory.")
            elif self.t_name_entry.text() == "":
                QMessageBox.information(MainWindow,"Warning","Teacher's name is missing.")
            elif self.sub1_combo.currentText() == "Select a subject":
                QMessageBox.information(MainWindow,"Warning","Select a subject.")
            elif self.sub2_combo.currentText() == "Select Subject II":
                QMessageBox.information(MainWindow,"Warning","Select a second subject.")
            elif self.t_emp_combo.currentText() == "Choose Employer":
                QMessageBox.information(MainWindow,"Warning","Choose Employer.")
            elif self.t_gender_combo.currentText() == "Select Gender":
                QMessageBox.information(MainWindow,"Warning","Select Gender.")
            else:
                try:
                    t_code_info = self.t_code_entry.text()
                    t_name_info = self.t_name_entry.text()
                    t_sub1_info = self.sub1_combo.currentText()
                    t_sub2_info = self.sub2_combo.currentText()
                    t_emp_info = self.t_emp_combo.currentText()
                    t_gender_info = self.t_gender_combo.currentText()
                    t_contact_info = self.t_contact_entry.text()
                    cur.execute("INSERT INTO teacher_data VALUES(?,?,?,?,?,?,?)",(t_code_info ,t_name_info,t_sub1_info,
                        t_sub2_info,t_emp_info,t_gender_info,t_contact_info)) 
                    QMessageBox.information(MainWindow,"Success","Teacher successfully added.")
                    conn.commit()
                    self.fetch_teacher_data()
                    #self.clear()
                    conn.close()
                except:
                    QMessageBox.warning(MainWindow,"Warning","Teacher not added.")
                    '''
                    conn = sqlite3.connect("mydb.db")
                    cur = conn.cursor()
                    cur.execute("UPDATE teacher_data SET t_name_info=?,t_sub1_info=?,t_sub2_info=?,t_emp_info=?,t_gender_info=?,t_code_info=?",
                        (t_name_info,t_sub1_info,t_sub2_info,t_emp_info,t_gender_info,t_contact_info)) #,(t_code_info ,t_name_info,t_sub1_info,t_sub2_info,t_emp_info,t_gender_info,t_contact_info))
                    QMessageBox.information(MainWindow,"Success","Edited details saved.")
                
                    conn.commit()
                    self.fetch_teacher_data()
                    self.clear()
                    conn.close()
                finally:
                    QMessageBox.warning(MainWindow,"Warning","Teacher not added.")
                    '''
        except:
            pass
    def tget_cursor(self):
        cursor_row = self.teachers_table.currentRow()
        item1 = self.teachers_table.item(cursor_row, 0) 
        self.t_code_entry.setText(item1.text() if item1 is not None else "")
        item2 = self.teachers_table.item(cursor_row, 1) 
        self.t_name_entry.setText(item2.text() if item2 is not None else "")
        item3 = self.teachers_table.item(cursor_row, 2) 
        self.sub1_combo.setCurrentText(item3.text() if item3 is not None else "")
        item4 = self.teachers_table.item(cursor_row, 3) 
        self.sub2_combo.setCurrentText(item4.text() if item4 is not None else "")
        item5 = self.teachers_table.item(cursor_row, 4) 
        self.t_emp_combo.setCurrentText(item5.text() if item5 is not None else "")
        item6 = self.teachers_table.item(cursor_row, 5) 
        self.t_gender_combo.setCurrentText(item6.text() if item6 is not None else "")
        item7 = self.teachers_table.item(cursor_row, 6) 
        self.t_contact_entry.setText(item7.text() if item7 is not None else "")
    def edit_teacher(self):
        self.tget_cursor()
    def search_each_teacher(self):
        try:
            self.search_info = self.t_search_entry.text()
            connection= sqlite3.connect("mydb.db")
            querry = "SELECT * FROM teacher_data WHERE t_code_info = '"+str(self.search_info)+"'"
            result = connection.execute(querry)
            self.teachers_table.setRowCount(0)
            for row_number,row_data in enumerate(result):
                self.teachers_table.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.teachers_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
            connection.commit()
            connection.close()
        except:
            QMessageBox.warning(MainWindow, "Failed", "Failed.")  
    def delete_marks(self):
        try:
            self.marks_table.removeRow(self.marks_table.currentRow())
            QMessageBox.information(MainWindow, "Successfull", "Erased")
        except:
            QMessageBox.warning(MainWindow, "Failed", "Failed.")
    def delete_teacher(self):
        try:
            conn= sqlite3.connect("mydb.db")
            querry = "DELETE FROM teacher_data WHERE t_code_info = '"+str(self.t_search_entry.text())+"'"
            result = conn.execute(querry)
            self.teachers_table.setRowCount(0)
            for row_number,row_data in enumerate(result):
                self.teachers_table.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.teachers_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
            conn.commit()
            conn.close()
            QMessageBox.information(MainWindow, "Successfull", "Teacher details erased")
            self.fetch_teacher_data()
        except:
            QMessageBox.warning(MainWindow, "Failed", "Failed.")
    def clear(self):
        self.photo.setText("                                   Photo")
        self.t_code_entry.setText("")
        self.t_name_entry.setText("")
        self.t_contact_entry.setText("")
        self.leaner_entry.setText("")
        self.adm_entry.setText("")
        self.parent_entry.setText("")
        self.parent_contact_entry.setText("")
    def exit_but(self):
        QMessageBox.information(MainWindow,"Exiting","Welcome back next time")
        sys.exit()
    def save_qtable(self):
        global saving_marks
        try:
            if self.class_combo.currentText() == "Select class" or self.term_combo.currentText()== "Select term" or self.year_combo.currentText()=="Year":
                QMessageBox.warning(MainWindow,"Impossible","Select appropriate options and try again")
            else:
                col_count = self.marks_table.columnCount()
                row_count = self.marks_table.rowCount()
                headers = [str(self.marks_table.horizontalHeaderItem(i).text()) for i in range(col_count)]
                df_list = []
                for row in range(row_count):
                    df_list2 = []
                    for col in range(col_count):
                        table_item = self.marks_table.item(row,col)
                        df_list2.append('' if table_item is None else str(table_item.text()))
                    df_list.append(df_list2)
                df = pd.DataFrame(df_list, columns=headers)
                #####ATTEMPTING TO SAVE THE DATAFRAME TO SQLITE3######
                saving_marks = self.class_combo.currentText()+" " + self.term_combo.currentText() + " "+ self.year_combo.currentText() + " marks"
                conn = sqlite3.connect('mydb.db')
                cur = conn.cursor()
                cur.execute("DROP TABLE IF EXISTS '" + str(saving_marks) + "' ")
                cur.execute("CREATE TABLE '" + str(
                saving_marks) + "' (STREAM TEXT NOT NULL,ADM INT NOT NULL,NAME TEXT NOT NULL,KCPE INT NOT NULL,ENG INT NOT NULL,KIS INT NOT NULL,MAT INT NOT NULL,BIO INT NOT NULL,PHY INT NOT NULL,CHE INT NOT NULL,HIS INT NOT NULL,GEO INT NOT NULL,CRE INT NOT NULL,AGR INT NOT NULL,HSC INT NOT NULL,BST INT NOT NULL)")
                cols = "`,`".join([str(i) for i in df.columns.tolist()])
                for i, row in df.iterrows():
                    sql = "INSERT INTO '" + str(saving_marks) + "' (`" + cols + "`) VALUES (" + "?," * (
                                len(row) - 1) + "?)"
                    cur.execute(sql, tuple(row))
                conn.commit()
                conn.close()

                QMessageBox.information(MainWindow,"Success","Data successfully saved to database.")
        except:
            QMessageBox.warning(MainWindow,"Failed","Operation failed.")
    def upload_marks(self):
        try:
            if self.class_combo.currentText() == "Select class":
                QMessageBox.information(MainWindow,"Check","Select class.") 
            elif self.term_combo.currentText() == "Select term":
                QMessageBox.information(MainWindow,"Check","Select term.") 
            elif self.year_combo.currentText() == "Year":
                QMessageBox.information(MainWindow,"Check", "Choose year.")
            elif self.exam_combo.currentText() == "Exams to analyze":
                QMessageBox.information(MainWindow,"Check", "Choose the number of exams to analyze.")
            elif self.exam_combo.currentText()=="1":
                try:
                    df = QFileDialog.getOpenFileName(MainWindow, 'Upload marks',os.path.expanduser("~/Documents"), 'excel(*.xlsx);;csv(*.csv)')#.setFileMode(QFileDialog.AnyFile)
                    path = df[0]
                    df1 = pd.read_excel(path)
                    headers = list(df1)
                    self.marks_table.setRowCount(df1.shape[0])
                    self.marks_table.setColumnCount(df1.shape[1])
                    self.marks_table.setHorizontalHeaderLabels(headers)
                    df_array = df1.values
                    for row in range(df1.shape[0]):
                        for col in range(df1.shape[1]):
                            self.marks_table.setItem(row, col,QTableWidgetItem(str(df_array[row,col])))
                    QMessageBox.information(MainWindow,"Successfull","Edit where necessary and SAVE before analysis")
                except IOError:
                    pass
            elif self.exam_combo.currentText()=="2":
                df2 = QFileDialog.getOpenFileName(MainWindow, 'Upload marks',os.path.expanduser("~/Documents"), 'excel(*.xlsx);;csv(*.csv)')
                path = df2[0]
                df3 = pd.read_excel(path)
                QMessageBox.information(MainWindow,"Successfull","Choose the last set of marks to upload.")
                df4 = QFileDialog.getOpenFileName(MainWindow, 'Upload marks',os.path.expanduser("~/Documents"), 'excel(*.xlsx);;csv(*.csv)')
                path = df4[0]
                df5 = pd.read_excel(path)        
                dfs=pd.concat((df3,df5)).groupby(['STREAM','ADM','NAME','KCPE'],as_index=False).mean().round()
                headers = list(dfs)
                self.marks_table.setRowCount(dfs.shape[0])
                self.marks_table.setColumnCount(dfs.shape[1])
                self.marks_table.setHorizontalHeaderLabels(headers)
                df_array = dfs.values
                for row in range(dfs.shape[0]):
                    for col in range(dfs.shape[1]):
                        self.marks_table.setItem(row, col,QTableWidgetItem(str(df_array[row,col])))
                QMessageBox.information(MainWindow,"Successfull","Edit where necessary and SAVE before analysis")
            elif self.exam_combo.currentText()== "3":
                df7 = QFileDialog.getOpenFileName(MainWindow, 'Upload marks',os.path.expanduser("~/Documents"), 'excel(*.xlsx);;csv(*.csv)')
                path = df7[0]
                df8 = pd.read_excel(path)
                QMessageBox.information(MainWindow,"Successfull","Choose a second exam set to upload.")
                df9 = QFileDialog.getOpenFileName(MainWindow, 'Upload marks',os.path.expanduser("~/Documents"), 'excel(*.xlsx);;csv(*.csv)')
                path = df9[0]
                df0 = pd.read_excel(path)
                QMessageBox.information(MainWindow,"Successfull","Choose the last exam set to upload.")
                dfi = QFileDialog.getOpenFileName(MainWindow, 'Upload marks',os.path.expanduser("~/Documents"), 'excel(*.xlsx);;csv(*.csv)')
                path = dfi[0]
                dfii = pd.read_excel(path)
                dfss=pd.concat((df8,df0,dfii)).groupby(['STREAM','ADM','NAME','KCPE'],as_index=False).mean().round()
                #INSERT INTO TABLE HERE
                headers = list(dfss)
                self.marks_table.setRowCount(dfss.shape[0])
                self.marks_table.setColumnCount(dfss.shape[1])
                self.marks_table.setHorizontalHeaderLabels(headers)
                df_array = dfss.values
                for row in range(dfss.shape[0]):
                    for col in range(dfss.shape[1]):
                        self.marks_table.setItem(row, col,QTableWidgetItem(str(df_array[row,col])))
                QMessageBox.information(MainWindow,"Successfull","Edit where necessary and SAVE before analysis")
            else:
                return
        except:
            QMessageBox.critical(MainWindow,"Failed","No file uploaded.")
    def analyze(self):
        global get_year
        try:
            marks = self.choose_class_combo.currentText()+" " + self.choose_term_combo.currentText() + " "+ self.choose_year_combo.currentText() + " marks"
            if self.choose_class_combo.currentText() == "Select class" or self.choose_term_combo.currentText()=="Select term" or self.choose_year_combo.currentText()== "Year":
                QMessageBox.information(MainWindow,"Reminder","Pick appropriately from the above options")
            elif self.choose_class_combo.currentText() == "FORM IV" and self.choose_term_combo.currentText() == "KCSE" and self.choose_year_combo.currentText() != "Year":
                QMessageBox.information(MainWindow,"Failed","Work in progress.")
                conn = sqlite3.connect()
                cur = conn.cursor()
                df_kcse = pd.read_sql("SELECT * FROM '" + str(marks) +"'",conn)

                df = df_kcse.copy()
                column_list = list(df)  # Begins to remove the unwanted columns to be worked out
                column_list.remove("STREAM")
                column_list.remove("ADM")
                column_list.remove("NAME")
                column_list.remove("KCPE")
                df[column_list] = df[column_list].astype("Int64")
                df.fillna(-1, inplace=True)
                df["ENTRY"] = df1[column_list].count(axis=1).astype(int)
                df["TOTAL"] = df1[column_list].sum(axis=1).astype(int)
                
                kcse_marks = []
                for i in df_kcse:
                    if i == 'A':
                        kcse_marks.append(12)
                    elif i == 'A-':
                        kcse_marks.append(11)
                    elif i == 'B+':
                        kcse_marks.append(10)
                    elif i == 'B':
                        kcse_marks.append(9)
                    elif i == 'B-':
                        kcse_marks.append(8)
                    elif i == 'C+':
                        kcse_marks.append(7)
                    elif i == 'C':
                        kcse_marks.append(6)
                    elif i == 'C-':
                        kcse_marks.append(5)
                    elif i == 'D+':
                        kcse_marks.append(4)
                    elif i == 'D':
                        kcse_marks.append(3)
                    elif i == 'D':
                        kcse_marks.append(2)
                    elif i == 'E':
                        kcse_marks.append(1)
                    else:
                        kcse_marks.append(0)
                    print(kcse_marks)

                conn.commit()
                conn.close()
            else:#Updating the columns with nan values to -1
                #marks = self.choose_class_combo.currentText()+" " + self.choose_term_combo.currentText() + " "+ self.choose_year_combo.currentText() + " marks"
                conn = sqlite3.connect('mydb.db')
                cur = conn.cursor()
                cur.execute("UPDATE '" + str(marks) + "' SET ENG=-1 WHERE ENG='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET KIS=-1 WHERE KIS='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET MAT=-1 WHERE MAT='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET BIO=-1 WHERE BIO='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET PHY=-1 WHERE PHY='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET CHE=-1 WHERE CHE='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET HIS=-1 WHERE HIS='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET GEO=-1 WHERE GEO='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET CRE=-1 WHERE CRE='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET AGR=-1 WHERE AGR='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET HSC=-1 WHERE HSC='nan'")
                cur.execute("UPDATE '" + str(marks) + "' SET BST=-1 WHERE BST='nan'")
                #Extracting data FROM DATABASE
                df1 = pd.read_sql("SELECT * FROM '" + str(marks) +"'",conn)
                df = df1.copy()
                column_list = list(df)  # Begins to remove the unwanted columns to be worked out
                column_list.remove("STREAM")
                column_list.remove("ADM")
                column_list.remove("NAME")
                column_list.remove("KCPE")
                df[column_list] = df[column_list].astype("Int64")
                df.fillna(-1, inplace=True)
                df["ENTRY"] = df1[column_list].count(axis=1).astype(int)
                df["TOTAL"] = df1[column_list].sum(axis=1).astype(int)
        ################CALCULATION OF SUBJECT GARDES######################################################################################
                ##############GRADING FOR SCIENCES##############################################################
                points = ['','_','E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
                bins = [-300,-1,0,25,30,35,40,45,50,55,60,65,70,75,100]
                df['MAT'] = (df.MAT.astype(str).replace('-1','_')) + pd.cut(df.MAT,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['BIO'] = (df.BIO.astype(str).replace('-1','_')) + pd.cut(df.BIO,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['PHY'] = (df.PHY.astype(str).replace('-1','_')) + pd.cut(df.PHY,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['CHE'] = (df.CHE.astype(str).replace('-1','_')) + pd.cut(df.CHE,bins,labels=points,include_lowest=True,right=False).astype(str)
                ##############GRADING FOR HUMANITIES, LANGUAGES AND TECHNICALS##################################
                points = ['','_','E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
                bins = [-300,-1,0,30,35,40,45,50,55,60,65,70,75,80,100]
                df['ENG'] = (df.ENG.astype(str).replace('-1','_')) + pd.cut(df.ENG,bins,labels=points,include_lowest=True,right=False).astype(str)#.)replace(-1300,'').replace(3000,'_')
                df['KIS'] = (df.KIS.astype(str).replace('-1','_')) + pd.cut(df.KIS,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['BST'] = (df.BST.astype(str).replace('-1','_')) + pd.cut(df.BST,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['HIS'] = (df.HIS.astype(str).replace('-1','_')) + pd.cut(df.HIS,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['CRE'] = (df.CRE.astype(str).replace('-1','_')) + pd.cut(df.CRE,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['GEO'] = (df.GEO.astype(str).replace('-1','_')) + pd.cut(df.GEO,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['AGR'] = (df.AGR.astype(str).replace('-1','_')) + pd.cut(df.AGR,bins,labels=points,include_lowest=True,right=False).astype(str)
                df['HSC'] = (df['HSC'].astype(str).replace('-1','_')) + pd.cut(df['HSC'],bins,labels=points,include_lowest=True,right=False).astype(str)
        ###############################################################################################################################################
                column_list = list(df1)  # Begins to removethe unwanted columns to be worked out
                column_list.remove("STREAM")
                column_list.remove("ADM")
                column_list.remove("NAME")
                column_list.remove("KCPE")
        ##################CALCULATION OF SUBJECT POINTS###################################################################################################
                points = [0,1,2,3,4,5,6,7,8,9,10,11,12]
                bins = [-1,0,30,35,40,45,50,55,60,65,70,75,80,100]
                df1['HIS'] = pd.cut(df1.HIS,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['HSC'] = pd.cut(df1['HSC'],bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['GEO'] = pd.cut(df1.GEO,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['CRE'] = pd.cut(df1.CRE,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1.AGR = pd.cut(df1.AGR,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['BST'] = pd.cut(df1.BST,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['ENG'] = pd.cut(df1.ENG,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['KIS'] = pd.cut(df1.KIS,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                points = [0,1,2,3,4,5,6,7,8,9,10,11,12]
                bins = [-1,0,25,30,35,40,45,50,55,60,65,70,75,100]
                df1['MAT'] = pd.cut(df1.MAT,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['CHE'] = pd.cut(df1.CHE,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['PHY'] = pd.cut(df1.PHY,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
                df1['BIO'] = pd.cut(df1.BIO,bins,labels=points,include_lowest=True,right=False).fillna(0).astype(int)
        ################STUDENTS POINTS/USED TO CALCULATE GRADES#############################################################################################
                if self.choose_class_combo.currentText() == "FORM I" or self.choose_class_combo.currentText() == "FORM II":
                    df['PTS'] = (df1.ENG+df1.KIS+df1.MAT+df1.CHE+df1.BIO+df1.PHY+df1.HIS+df1.GEO+df1.CRE+df1.AGR+df1['HSC']+df1.BST)
                else:
                    df['PTS'] = (df1[['BIO', 'PHY']].max(axis=1) + df1[['HIS','GEO','CRE','AGR','HSC','BST']].apply(lambda row: row.sort_values(ascending=False).head(2).sum() ,axis=1) + df1['ENG'] + df1['KIS']+ df1['MAT']+ df1['CHE'])
        ################STUDENTS GRADES#############################################################################################################
                if self.choose_class_combo.currentText() == "FORM I" or self.choose_class_combo.currentText() == "FORM II":
                    aver_grades = ['X','E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
                    bins = [-1,1,354,414,474,534,594,654,714,774,834,894,954,1200]
                    df['GRADE'] = pd.cut(df.TOTAL,bins,labels=aver_grades,include_lowest=True,right=False)
                else:
                    aver_grades = ['X','E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
                    bins = [-1,1,11,18,25,32,39,46,53,60,67,74,81,100]
                    df['GRADE'] = pd.cut(df.PTS,bins,labels=aver_grades,include_lowest=True,right=False)
        ################ OVERALL GRADE SUMMARY###################################################################################################
                columns = ['A','A-','B+','B','B-','C+','C','C-','D+','D','D-','E','X','Z']
                g_summary = (pd.crosstab(df.STREAM, df.GRADE, margins=True, margins_name='TOTAL').iloc[:,:-1].reindex(columns, axis=1, fill_value=0).rename_axis(index='SUBJ', columns=None))
                g_summary['TOTAL'] = g_summary.sum(axis=1)
        ######################CALCULATION OF STREAM MEANS ################################################################################################
                g_sum = (g_summary['A']*12+g_summary['A-']*11+g_summary['B+']*10+g_summary['B']*9+g_summary['B-']*8+g_summary['C+']*7+g_summary['C']*6+g_summary['C-']*5+g_summary['D+']*4+g_summary['D']*3+g_summary['D-']*2+g_summary['E']*1)
                tot = ((g_summary['TOTAL'])-(g_summary['X']*1+g_summary['Z']*1))
                g_summary['MEAN'] = (g_sum/tot).round(4)
        ################ CALCULATION OF STREAM GRADES ##############################################################################################################
                s_grades = ['X','E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
                bins = [-1,0,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12]
                g_summary['GRD'] = pd.cut(g_summary.MEAN,bins,labels=s_grades,include_lowest=True,right=False)
        #####################################################################################################################################################
                if self.choose_class_combo.currentText() == "FORM I" or self.choose_class_combo.currentText() == "FORM II":
                    df['POS'] = df['TOTAL'].rank(ascending=False).astype(int)
                else:
                    df['POS'] = df['PTS'].rank(ascending=False).astype(int)
                df.sort_values('POS',inplace=True)
                if self.choose_class_combo.currentText() == "FORM I" or self.choose_class_combo.currentText() == "FORM II":
                    df["VAP"] = df["TOTAL"] - ( df["KCPE"] +350)
                else:
                    df["VAP"] = df["PTS"] - ( (df["KCPE"]/5) - 10).astype(int)
        ###########################################################################################################################################
                headers = list(df)
                self.analysis_table.setRowCount(df.shape[0])
                self.analysis_table.setColumnCount(df.shape[1])
                self.analysis_table.setHorizontalHeaderLabels(headers)
                df_array = df.values
                for row in range(df.shape[0]):
                    for col in range(df.shape[1]):
                        self.analysis_table.setItem(row, col,QTableWidgetItem(str(df_array[row,col])))
                dfM = df1[column_list].replace(0, np.nan).mean().round(4)
        ##################CONVERTING SUBJECT POINTS TO GRADES###################################################################################################
                points = ['E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A','_']
                bins = [0,1,2,3,4,5,6,7,8,9,10,11,12,3000]
                df1['HIS'] = pd.cut(df1.HIS,bins,labels=points)
                df1['HSC'] = pd.cut(df1['HSC'],bins,labels=points)
                df1['GEO'] = pd.cut(df1.GEO,bins,labels=points)
                df1['CRE'] = pd.cut(df1.CRE,bins,labels=points)
                df1.AGR = pd.cut(df1.AGR,bins,labels=points)
                df1['BST'] = pd.cut(df1.BST,bins,labels=points)
                df1['ENG'] = pd.cut(df1.ENG,bins,labels=points)
                df1['KIS'] = pd.cut(df1.KIS,bins,labels=points)
                df1['MAT'] = pd.cut(df1.MAT,bins,labels=points)
                df1['CHE'] = pd.cut(df1.CHE,bins,labels=points)
                df1['PHY'] = pd.cut(df1.PHY,bins,labels=points)
                df1['BIO'] = pd.cut(df1.BIO,bins,labels=points)
        ################GETTING SUMMATION OF GRADES PER SUBJECT//GRADE SUMMARY FOR SUBJECTS##########################################################
                columns = ["A",'A-','B+',"B",'B-','C+',"C",'C-','D+',"D",'D-',"E",'X']
                cols = list(df[column_list])
                df2 = df1[cols].melt()
                df3 = (pd.crosstab(df2['variable'], df2['value'], margins=True, margins_name='TOTAL').iloc[:-1].reindex(columns + ['TOTAL'], fill_value=0, axis=1).rename_axis(index='SUBJ', columns=None))
                gr_sum = (df3['A']*12+df3['A-']*11+df3['B+']*10+df3['B']*9+df3['B-']*8+df3['C+']*7+df3['C']*6+df3['C-']*5+df3['D+']*4+df3['D']*3+df3['D-']*2+df3['E']*1)
                tots = ((df3['TOTAL']) - (df3['X']*1))
                df3['MEAN'] = (gr_sum/tots).round(4)
                df3.sort_values(by=['MEAN'],inplace=True,ascending = False)
        ################ CALCULATION OF SUBJECT GRADES FOR SUBJECT RANKING ##############################################################################################################
                sbj_grades = ['X','E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
                bins = [-1,0,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12]
                df3['GRD'] = pd.cut(df3.MEAN,bins,labels=sbj_grades,include_lowest=True,right=False)
                conn.commit()
                conn.close()
        ######################SAVING EXCELL ANALYSIS###############################################################################################################
                conn = sqlite3.connect('mydb.db')
                cur = conn.cursor()
                df_re = pd.read_sql("SELECT * FROM '" + str(marks) +"'",conn)
                dfrem = df_re.copy()
                df_re = df_re.fillna(-1)
                #CONVERSION OF MARKS TO POINT FOR REPORT FORM PRODUCTION
                points = ['_',1,2,3,4,5,6,7,8,9,10,11,12]
                bins = [-1,0,30,35,40,45,50,55,60,65,70,75,80,100]
                df_re['ENGp'] = pd.cut(df_re.ENG,bins,labels=points,include_lowest=True,right=False)
                df_re['KISp'] = pd.cut(df_re.KIS,bins,labels=points,include_lowest=True,right=False)
                df_re['HISp'] = pd.cut(df_re.HIS,bins,labels=points,include_lowest=True,right=False)
                df_re['H/SCp'] = pd.cut(df_re['HSC'],bins,labels=points,include_lowest=True,right=False)
                df_re['GEOp'] = pd.cut(df_re.GEO,bins,labels=points,include_lowest=True,right=False)
                df_re['CREp'] = pd.cut(df_re.CRE,bins,labels=points,include_lowest=True,right=False)
                df_re['AGRp'] = pd.cut(df_re.AGR,bins,labels=points,include_lowest=True,right=False)
                df_re['BSTp'] = pd.cut(df_re.BST,bins,labels=points,include_lowest=True,right=False)

                points = ['_',1,2,3,4,5,6,7,8,9,10,11,12]
                bins = [-1,0,25,30,35,40,45,50,55,60,65,70,75,100]
                df_re['MATp'] = pd.cut(df_re.MAT,bins,labels=points,include_lowest=True,right=False)
                df_re['CHEp'] = pd.cut(df_re.CHE,bins,labels=points,include_lowest=True,right=False)
                df_re['PHYp'] = pd.cut(df_re.PHY,bins,labels=points,include_lowest=True,right=False)
                df_re['BIOp'] = pd.cut(df_re.BIO,bins,labels=points,include_lowest=True,right=False)
                df_re = df_re.replace(-1,'_')

                df_re['PTS'] = df.PTS
                df_re['GRADE'] = df.GRADE
                df_re['ENTRY'] = df.ENTRY
                df_re['TOTAL'] = df.TOTAL
                df_re['POS'] = df.POS
                df_re['VAP'] = df.VAP

                df_re['ENGg'] = df1.ENG.fillna('_')
                df_re['KISg'] = df1.KIS.fillna('_')
                df_re['MATg'] = df1.MAT.fillna('_')
                df_re['BIOg'] = df1.BIO.fillna('_')
                df_re['PHYg'] = df1.PHY.fillna('_')
                df_re['CHEg'] = df1.CHE.fillna('_')
                df_re['HISg'] = df1.HIS.fillna('_')
                df_re['GEOg'] = df1.GEO.fillna('_')
                df_re['CREg'] = df1.CRE.fillna('_')
                df_re['AGRg'] = df1.AGR.fillna('_')
                df_re['H/SCg'] = df1['HSC'].fillna('_')
                df_re['BSTg'] = df1.BST.fillna('_')
                df_re['TOT'] = df_re.PTS.count()
                ## RANK SUBJECTS FOR REPORT CARDS#########################
                data = pd.read_sql("SELECT * FROM '" + str(marks) +"'",conn)
                dfrank = data.replace(-1,np.nan)
                df_re['ENGr'] = dfrank.ENG.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['KISr'] = dfrank.KIS.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['MATr'] = dfrank.MAT.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['BIOr'] = dfrank.BIO.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['PHYr'] = dfrank.PHY.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['CHEr'] = dfrank.CHE.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['HISr'] = dfrank.HIS.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['GEOr'] = dfrank.GEO.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['CREr'] = dfrank.CRE.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['AGRr'] = dfrank.AGR.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['H/SCr'] = dfrank['HSC'].rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
                df_re['BSTr'] = dfrank.BST.rank(ascending=False).fillna(-1).astype(int).replace(-1,'_')
        ################REPORT FORM REMARKS##############################################################################################
                remarks = ['_','POOR','WEAK','AVERAGE','GOOD','V.GOOD']
                bins = [-1,1,25,45,60,75,100]
                dfrem = dfrem.fillna(0)
                df_re['ENGre'] = pd.cut(dfrem.ENG,bins,labels=remarks,include_lowest=True,right=False)
                df_re['KISre'] = pd.cut(dfrem.KIS,bins,labels=remarks,include_lowest=True,right=False)
                df_re['MATre'] = pd.cut(dfrem.MAT,bins,labels=remarks,include_lowest=True,right=False)
                df_re['BIOre'] = pd.cut(dfrem.BIO,bins,labels=remarks,include_lowest=True,right=False)
                df_re['PHYre'] = pd.cut(dfrem.PHY,bins,labels=remarks,include_lowest=True,right=False)
                df_re['CHEre'] = pd.cut(dfrem.CHE,bins,labels=remarks,include_lowest=True,right=False)
                df_re['HISre'] = pd.cut(dfrem.HIS,bins,labels=remarks,include_lowest=True,right=False)
                df_re['GEOre'] = pd.cut(dfrem.GEO,bins,labels=remarks,include_lowest=True,right=False)
                df_re['CREre'] = pd.cut(dfrem.CRE,bins,labels=remarks,include_lowest=True,right=False)
                df_re['AGRre'] = pd.cut(dfrem.AGR,bins,labels=remarks,include_lowest=True,right=False)
                df_re['H/SCre'] = pd.cut(dfrem['HSC'],bins,labels=remarks,include_lowest=True,right=False)
                df_re['BSTre'] = pd.cut(dfrem.BST,bins,labels=remarks,include_lowest=True,right=False)
                ##########MISCELENIOUS COLUMNS########
                df_re['CLASS'] = self.choose_class_combo.currentText()
                df_re['TERM'] = self.choose_term_combo.currentText()
                df_re['YEAR'] = self.choose_year_combo.currentText()
                #Ceating table names
                overall_summary = self.choose_class_combo.currentText()+" " + self.choose_term_combo.currentText() + " "+ self.choose_year_combo.currentText() + " str summary"
                analysis = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " analysis"
                subject_summary = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " sub summary"
                students_data = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report"
                #csv information backups
                df.to_csv(analysis + ".csv",index=False)
                df_re.to_csv(students_data + ".csv",index=False)
                #Creating the tables with thye above names
                cur.execute("DROP TABLE IF EXISTS '" + str(overall_summary) +"' ")
                g_summary.to_sql(overall_summary, conn, if_exists='replace', index=True )
                #Subject summary table
                cur.execute("DROP TABLE IF EXISTS '" + str(subject_summary) +"' ")
                df3.to_sql(subject_summary,conn, if_exists='replace', index=True) # - writes the pd.df to SQLIte DB, conn"
                #Analysis table
                cur.execute("DROP TABLE IF EXISTS '" + str(analysis) +"' ")
                df.to_sql(analysis,conn, if_exists='replace', index=False)
                #Table containing report forms data
                cur.execute("DROP TABLE IF EXISTS '" + str(students_data) +"' ")
                df_re.to_sql(students_data,conn, if_exists='replace', index=False)
                try:
                    tab_gen = pd.read_csv('report generator.csv')
                    tab_gen.to_sql('report_generator',conn, if_exists='replace', index=False)
                except:
                    QMessageBox.information(MainWindow, 'Alert', 'Base report generator missing.')
                conn.commit()
                conn.close()
        except:
            QMessageBox.information(MainWindow,"Failed","Select appropriate fields above, check that marks corresponding to the chosen fields is saved.")
    def get_results(self):	
        try:
        ###################GENERATING PDF FOR MAIN ANALYSIS################
            analysist = (self.choose_class_combo.currentText() + ' ' + self.choose_term_combo.currentText() + ' ' + self.choose_year_combo.currentText() + ' ' + "STUDENT RANKS.pdf")
            pdf=SimpleDocTemplate(analysist)
            frame1 = Frame(30,10,950,620)
            land = PageTemplate(id='l',pagesize=[970,650],frames=[frame1])
            heading = 'FR GULIK URADI GIRLS SEC. SCHOOL // '+self.choose_class_combo.currentText()+' '+self.choose_term_combo.currentText()+' '+self.choose_year_combo.currentText()+' EXAMINATION RESULTS'
            styled = getSampleStyleSheet()
            des = ParagraphStyle('description',fontName='Courier-Bold',fontSize=17,leading=30, alignment=TA_CENTER)
            head_text = Paragraph(heading,des)#style=styled['Heading4'])
            pdf.addPageTemplates([land])
            flow_obj=[]
            flow_obj.append(head_text)
            #creating the connection
            analysis = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " analysis"
            conn = sqlite3.connect('mydb.db')
            cur = conn.cursor()
            analysis = pd.read_sql("SELECT * FROM '" + str(analysis) + "'", conn) 
            tdata = [] 
            tdata.append(analysis.columns.tolist()) 
            for index, data in analysis.iterrows():
                rowdata=[]
                STREAM=data[0]
                ADM=data[1]
                NAME=data[2]
                KCPE=data[3]
                ENG=data[4]
                KIS=data[5]
                MAT=data[6]
                BIO=data[7]
                PHY=data[8]
                CHE=data[9]
                HIS=data[10]
                GEO=data[11]
                CRE=data[12]
                AGR=data[13]
                HSC=data[14]
                BST=data[15]
                ENTRY=data[16]
                TOTAL=data[17]
                PTS=data[18]
                GRADE=data[19]
                POS=data[20]
                VAP=data[21]
                rowdata.append(STREAM)
                rowdata.append(ADM)
                rowdata.append(NAME)
                rowdata.append(KCPE)
                rowdata.append(ENG)
                rowdata.append(KIS)
                rowdata.append(MAT)
                rowdata.append(BIO)
                rowdata.append(PHY)
                rowdata.append(CHE)
                rowdata.append(HIS)
                rowdata.append(GEO)
                rowdata.append(CRE)
                rowdata.append(AGR)
                rowdata.append(HSC)
                rowdata.append(BST)
                rowdata.append(ENTRY)
                rowdata.append(TOTAL)
                rowdata.append(PTS)
                rowdata.append(GRADE)
                rowdata.append(POS)
                rowdata.append(VAP)
                tdata.append(rowdata)
            for i in range(len(tdata)):
                if(i%28==0 and i>0):
                    flow_obj.append(NextPageTemplate('l'))
                    flow_obj.append(PageBreak())
                    t=Table([tdata[0]],colWidths=[45,30,150,35,35,35,35,35,35,35,35,35,35,35,35,35,45,45,35,45,35,45])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier",9),
                                   ("BACKGROUND",(0,0),(-1,-1),colors.cyan)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
                if (i==0):
                    flow_obj.append(NextPageTemplate('l'))
                    t=Table([tdata[0]],colWidths=[45,30,150,35,35,35,35,35,35,35,35,35,35,35,35,35,45,45,35,45,35,45])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier-Bold",9),
                                    ("BACKGROUND",(0,0),(-1,-1),colors.cyan)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
                else:
                    flow_obj.append(NextPageTemplate('l'))
                    t=Table([tdata[i]],colWidths=[45,30,150,35,35,35,35,35,35,35,35,35,35,35,35,35,45,45,35,45,35,45])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier",9)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
            pdf.build(flow_obj)
            conn.commit()
            conn.close()
            ############PDF GENERATION FOR STREAM RAKNINGS#################
            str_rankings = (self.choose_class_combo.currentText() + ' ' + self.choose_term_combo.currentText() + ' ' + self.choose_year_combo.currentText() + ' ' + " STREAM RANKINGS.pdf")
            pdf2=SimpleDocTemplate(str_rankings)
            frame1 = Frame(30,20,900,600)
            land = PageTemplate(id='l',pagesize=[950,650],frames=[frame1])
            heading = self.choose_class_combo.currentText()+' '+self.choose_term_combo.currentText()+' '+self.choose_year_combo.currentText()+' OVERALL PERFOMANCE AND GRADE BREAKDOWN'
            descrip = ParagraphStyle('description',fontName='Courier-Bold',fontSize=18,leading=30, alignment=TA_CENTER)
            head_text = Paragraph(heading,descrip)
            pdf.addPageTemplates([land])
            pdf2.addPageTemplates(PageTemplate(id='l',pagesize=[950,650],frames=[frame1]))
            flow_obj=[]
            flow_obj.append(head_text)
            #creating the connection
            overall_summary = self.choose_class_combo.currentText()+" " + self.choose_term_combo.currentText() + " "+ self.choose_year_combo.currentText() + " str summary"
            conn = sqlite3.connect('mydb.db')
            cur = conn.cursor()
            str_summary = pd.read_sql("SELECT * FROM '" + str(overall_summary) + "'", conn) 
            tdata = [] 
            tdata.append(str_summary.columns.tolist()) 
            for index, row in str_summary.iterrows():
                rowdata = []
                BLANK=row[0]
                A1 =row[1]
                A2=row[2]
                B3=row[3]
                B4=row[4]
                B5=row[5]
                C6=row[6]
                C7=row[7]
                C8=row[8]
                D9=row[9]
                D0=row[10]
                D1=row[11]
                E2=row[12]
                X=row[13]
                Z = row[14]
                TOTAL=row[15]
                MEAN=row[16]
                GRD=row[17]
                rowdata.append(BLANK)
                rowdata.append(A1)
                rowdata.append(A2)
                rowdata.append(B3)
                rowdata.append(B4)
                rowdata.append(B5)
                rowdata.append(C6)
                rowdata.append(C7)
                rowdata.append(C8)
                rowdata.append(D9)
                rowdata.append(D0)
                rowdata.append(D1)
                rowdata.append(E2)
                rowdata.append(X)
                rowdata.append(Z)
                rowdata.append(TOTAL)
                rowdata.append(MEAN)
                rowdata.append(GRD)
                tdata.append(rowdata)
            for i in range(len(tdata)):
                if(i%50000==0 and i>0):
                    flow_obj.append(NextPageTemplate('l'))
                    flow_obj.append(PageBreak())
                    t=Table([tdata[0]],colWidths=[50,30,30,30,30,30,30,30,30,30,30,30,30,30,30,60,60,50])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier",12),
                                   ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
                if (i==0):
                    flow_obj.append(NextPageTemplate('l'))
                    t=Table([tdata[0]],colWidths=[50,30,30,30,30,30,30,30,30,30,30,30,30,30,30,60,60,50])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier-Bold",12),
                                    ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
                else:
                    flow_obj.append(NextPageTemplate('l'))
                    t=Table([tdata[i]],colWidths=[50,30,30,30,30,30,30,30,30,30,30,30,30,30,30,60,60,50])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier",12)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
            pdf2.build(flow_obj)
            conn.commit()
            conn.close()
            ###SUBJECT RANKUNGS#############################################
            sub_rankings = (self.choose_class_combo.currentText() + ' ' + self.choose_term_combo.currentText() + ' ' + self.choose_year_combo.currentText() + ' ' + " SUBJECT RANKINGS.pdf")
            pdf3=SimpleDocTemplate(sub_rankings)
            frame1 = Frame(30,20,900,600)
            land = PageTemplate(id='l',pagesize=[950,650],frames=[frame1])
            heading = self.choose_class_combo.currentText()+' '+self.choose_term_combo.currentText()+' '+self.choose_year_combo.currentText()+' SUBJECT PERFOMANCE AND RANKING'
            styled = getSampleStyleSheet()
            des = ParagraphStyle('description',fontName='Courier-Bold',fontSize=18,leading=30, alignment=TA_CENTER)
            story = Paragraph(heading,des)#style=styled['Heading2'])
            pdf.addPageTemplates([land])
            pdf3.addPageTemplates(PageTemplate(id='l',pagesize=[950,650],frames=[frame1]))
            flow_obj=[]
            flow_obj.append(story)
            #creating the connection
            sub_summary = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " sub summary"
            conn = sqlite3.connect('mydb.db')
            cur = conn.cursor()
            sub_summary = pd.read_sql("SELECT * FROM '" + str(sub_summary) + "'", conn) 
            tdata = [] 
            tdata.append(sub_summary.columns.tolist()) 
            for index, data in sub_summary.iterrows():
                rowdata=[]
                BLANK=data[0]
                A1 =data[1]
                A2=data[2]
                B3=data[3]
                B4=data[4]
                B5=data[5]
                C6=data[6]
                C7=data[7]
                C8=data[8]
                D9=data[9]
                D0=data[10]
                D1=data[11]
                E2=data[12]
                X=data[13]
                TOTAL=data[14]
                MEAN=data[15]
                GRD=data[16]
                rowdata.append(BLANK)
                rowdata.append(A1)
                rowdata.append(A2)
                rowdata.append(B3)
                rowdata.append(B4)
                rowdata.append(B5)
                rowdata.append(C6)
                rowdata.append(C7)
                rowdata.append(C8)
                rowdata.append(D9)
                rowdata.append(D0)
                rowdata.append(D1)
                rowdata.append(E2)
                rowdata.append(X)
                rowdata.append(TOTAL)
                rowdata.append(MEAN)
                rowdata.append(GRD)
                tdata.append(rowdata)
            for i in range(len(tdata)):
                if(i%50000==0 and i>0):
                    flow_obj.append(NextPageTemplate('l'))
                    flow_obj.append(PageBreak())
                    t=Table([tdata[0]],colWidths=[50,30,30,30,30,30,30,30,30,30,30,30,30,30,60,60,50])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier",12),
                                   ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
                if (i==0):
                    flow_obj.append(NextPageTemplate('l'))
                    t=Table([tdata[0]],colWidths=[50,30,30,30,30,30,30,30,30,30,30,30,30,30,60,60,50])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier-Bold",12),
                                    ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
                    t.setStyle(tstyle)
                    flow_obj.append(t,)
                else:
                    flow_obj.append(NextPageTemplate('l'))
                    t=Table([tdata[i]],colWidths=[50,30,30,30,30,30,30,30,30,30,30,30,30,30,60,60,50])
                    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                   ("FONT",(0,0),(-1,-1),"Courier",12)])
                    t.setStyle(tstyle)
                    flow_obj.append(t)
            existing_file = (self.choose_class_combo.currentText() + ' ' + self.choose_term_combo.currentText() + ' ' + self.choose_year_combo.currentText() + ' ' + "RESULTS.pdf")
            pdf3.build(flow_obj)
            conn.commit()
            conn.close()

            #######STREAM RANKS GRAPHS##########################
            
            df = str_summary
            xpos = np.arange(len(df['SUBJ']))
            plt.bar(xpos,df.MEAN)
            plt.xticks(xpos,df['SUBJ'])
            plt.ylabel("MEAN")
            #plt.xlabel("SUBJECT")
            plt.title('STREAM PERFOMANCE')
            plt.legend()
            str_graph = self.choose_class_combo.currentText() + ' ' + self.choose_term_combo.currentText() + ' ' + self.choose_year_combo.currentText() + ' ' + "GRAPH 1.pdf"
            plt.savefig(str_graph,orientation='landscape')
            #plt.show()
            #######STREAM RANKS GRAPHS##########################
            df = sub_summary
            xpos = np.arange(len(df['SUBJ']))
            plt.bar(xpos,df.MEAN)
            plt.xticks(xpos,df['SUBJ'])
            plt.ylabel("MEAN")
            plt.title('SUBJECT PERFOMANCE')
            plt.legend()
            size = (600,500)
            sub_graph = self.choose_class_combo.currentText() + ' ' + self.choose_term_combo.currentText() + ' ' + self.choose_year_combo.currentText() + ' ' + "GRAPH 2.pdf"
            plt.savefig(sub_graph,orientation=size)
            #plt.show()
            #THE MERGING OF THE PDF FILESs#########
            pdfs = [analysist,str_rankings,sub_rankings]
            merger = PdfFileMerger()
            for pdf in pdfs:
                merger.append(open(pdf, 'rb'))
            with open(existing_file, 'wb') as fout:
                merger.write(fout)
            
            #PAGE NUMBERING AND FOOTER##########################
            reader = PdfReader(existing_file)
            pages = [pagexobj(p) for p in reader.pages]
            canvas = Canvas(existing_file)
            for page_num, page in enumerate(pages, start=1):
                canvas.setPageSize((page.BBox[2], page.BBox[3]))
                canvas.doForm(makerl(canvas, page))
                footer_text = "PRINCIPAL   _____________________________________________   D.O.S    ___________________________________________      Page %s of %s" % (page_num, len(pages))
                canvas.saveState()
                canvas.setFont('Times-Roman', 14)
                canvas.drawString(44, 40, footer_text)
                canvas.restoreState()
                canvas.showPage()
            canvas.save()
            ########THE SAVING THROUGH QGETSAVEFILENAME#########
            saving_file = (self.choose_class_combo.currentText() + ' ' + self.choose_term_combo.currentText() + ' ' + self.choose_year_combo.currentText() + ' ' + "OVERALL ANALYSIS.pdf")
            filename = QFileDialog.getSaveFileName(MainWindow, "Save results",os.path.expanduser("~/Documents"),"Save pdf(*.pdf)")  # ;;Save excel(*.xlsx))")
            if filename:
                try:
                    with open(existing_file, 'r') as user, open(filename[0],'w') as name:
                        for line in user:
                            name.writelines(line)
                except IOError:
                    pass
            QMessageBox.information(MainWindow,"Successfull","Results downloaded to the location you specified.")
        except:
            QMessageBox.information(MainWindow,"Warning",'Could not download results, analyze first and retry')
    def download_report(self):
        try:
            conn = sqlite3.connect("mydb.db")
            cur = conn.cursor()
            klass = self.choose_class_combo.currentText()
            term = self.choose_term_combo.currentText()
            year = self.choose_year_combo.currentText()
            
            report_gen = pd.read_sql("SELECT * FROM report_generator", conn)
            repo = tempfile.NamedTemporaryFile(delete=True)
            report_gen.to_csv(repo.name + '.csv',index=False)
            repo.flush()
            repo.seek(0)
            repo = csv.reader(open(repo.name + '.csv','r'))
            if klass == 'FORM IV':
                #FORM I
                dataf1t1 = ("FORM I TERM I "+str(int(year) - 3)+" report")
                try:
                    f1t1 = pd.read_sql("SELECT * FROM '" + str(dataf1t1) + "'", conn)
                except:
                    f1t1 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf1t2 = ("FORM I TERM II "+str(int(year) - 3)+" report")
                try:
                    f1t2 = pd.read_sql("SELECT * FROM '" + str(dataf1t2) + "'", conn)
                except:
                    f1t2 = pd.read_sql("SELECT * FROM report_generator", conn)
        
                dataf1t3 = ("FORM I TERM III "+str(int(year) - 3)+" report")
                try:
                    f1t3 = pd.read_sql("SELECT * FROM '" + str(dataf1t3) + "'" or "report_generator", conn)
                except:
                    f1t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM II
                dataf2t1 = ("FORM II TERM I "+str(int(year) - 2)+" report")
                try:
                    f2t1 = pd.read_sql("SELECT * FROM '" + str(dataf2t1) + "'", conn)
                except:
                    f2t1 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf2t2 = ("FORM II TERM II "+str(int(year) - 2)+" report")
                try:
                    f2t2 = pd.read_sql("SELECT * FROM '" + str(dataf2t2) + "'", conn)
                except:
                    f2t2 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf2t3 = ("FORM II TERM III "+str(int(year) - 2)+" report")
                try:
                    f2t3 = pd.read_sql("SELECT * FROM '" + str(dataf2t3) + "'", conn)
                except:
                    f2t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM III
                dataf3t1 = ("FORM III TERM I "+str(int(year) - 1)+" report")
                try:
                    f3t1 = pd.read_sql("SELECT * FROM '" + str(dataf3t1) + "'", conn)
                except:
                    f3t1 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf3t2 = ("FORM III TERM II "+str(int(year) - 1)+" report")
                try:
                    f3t2 = pd.read_sql("SELECT * FROM '" + str(dataf3t2) + "'", conn)
                except:
                    f3t2 = pd.read_sql("SELECT * FROM report_generator", conn)
                
                dataf3t3 = ("FORM III TERM III "+str(int(year) - 1)+" report")
                try:
                    f3t3 = pd.read_sql("SELECT * FROM '" + str(dataf3t3) + "'", conn)
                except:
                    f3t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM IV
                dataf4t1 = ("FORM IV TERM I "+str(year)+" report")
                try:
                    f4t1 = pd.read_sql("SELECT * FROM '" + str(dataf4t1) + "'", conn)
                except:
                    f4t1 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf4t2 = ("FORM IV TERM II "+str(year)+" report")
                try:
                    f4t2 = pd.read_sql("SELECT * FROM '" + str(dataf4t2) + "'", conn)
                except:
                    f4t2 = pd.read_sql("SELECT * FROM report_generator", conn)
                
                dataf4t3 = ("FORM IV TERM III "+str(year)+" report")
                try:
                    f4t3 = pd.read_sql("SELECT * FROM '" + str(dataf4t3) + "'", conn)
                except:
                    f4t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                students_data = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report"     
                temp = pd.read_sql("SELECT * FROM '" + str(students_data) + "'", conn)
                #additional columns
                #Term I
                temp['class11'] = f1t1.CLASS
                temp['year11'] = f1t1.YEAR
                temp['points11'] = f1t1.PTS
                temp['grade11'] = f1t1.GRADE
                temp['position11'] = f1t1.POS
                #Term II
                temp['class12'] = f1t2.CLASS
                temp['year12'] = f1t2.YEAR
                temp['points12'] = f1t2.PTS
                temp['grade12'] = f1t2.GRADE
                temp['position12'] = f1t2.POS
                #Term III
                temp['class13'] = f1t3.CLASS
                temp['year13'] = f1t3.YEAR
                temp['points13'] = f1t3.PTS
                temp['grade13'] = f1t3.GRADE
                temp['position13'] = f1t3.POS
                #f2 Term I
                temp['class21'] = f2t1.CLASS
                temp['year21'] = f2t1.YEAR
                temp['points21'] = f2t1.PTS
                temp['grade21'] = f2t1.GRADE
                temp['position21'] = f2t1.POS
                #Term II
                temp['class22'] = f2t2.CLASS
                temp['year22'] = f2t2.YEAR
                temp['points22'] = f2t2.PTS
                temp['grade22'] = f2t2.GRADE
                temp['position22'] = f2t2.POS
                #Term III
                temp['class23'] = f2t3.CLASS
                temp['year23'] = f2t3.YEAR
                temp['points23'] = f2t3.PTS
                temp['grade23'] = f2t3.GRADE
                temp['position23'] = f2t3.POS
                #TermI
                temp['class31'] = f3t1.CLASS
                temp['year31'] = f3t1.YEAR
                temp['points31'] = f3t1.PTS
                temp['grade31'] = f3t1.GRADE
                temp['position31'] = f3t1.POS
                #Term II
                temp['class32'] = f3t2.CLASS
                temp['year32'] = f3t2.YEAR
                temp['points32'] = f3t2.PTS
                temp['grade32'] = f3t2.GRADE
                temp['position32'] = f3t2.POS
                #Term III
                temp['class33'] = f3t3.CLASS
                temp['year33'] = f3t3.YEAR
                temp['points33'] = f3t3.PTS
                temp['grade33'] = f3t3.GRADE
                temp['position33'] = f3t3.POS
                 #TermI
                temp['class41'] = f4t1.CLASS
                temp['year41'] = f4t1.YEAR
                temp['points41'] = f4t1.PTS
                temp['grade41'] = f4t1.GRADE
                temp['position41'] = f4t1.POS
                #Term II
                temp['class42'] = f4t2.CLASS
                temp['year42'] = f4t2.YEAR
                temp['points42'] = f4t2.PTS
                temp['grade42'] = f4t2.GRADE
                temp['position42'] = f4t2.POS
                #Term III
                temp['class43'] = f4t3.CLASS
                temp['year43'] = f4t3.YEAR
                temp['points43'] = f4t3.PTS
                temp['grade43'] = f4t3.GRADE
                temp['position43'] = f4t3.POS
                #temp.to_csv('me.csv',index=False)
                students_data2 = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report2"            
                temp.to_sql(students_data2,conn,if_exists='replace',index=False)
                students_data = pd.read_sql("SELECT * FROM '" + str(students_data2) + "'", conn)
                
                temp = tempfile.NamedTemporaryFile(delete=True)
                students_data.to_csv(temp.name + '.csv',index=False)
                temp.flush()
                temp.seek(0)
                temp = csv.reader(open(temp.name + '.csv','r'))
                c = canvas.Canvas(self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                for row in ([x for x in temp][1:]):
                    STREAM = row[0]
                    ADM = row[1]
                    NAME = row[2]
                    KCPE = row[3]
                    ENG = row[4]
                    KIS = row[5]
                    MAT = row[6]
                    BIO = row[7]
                    PHY = row[8]
                    CHE = row[9]
                    HIS = row[10]
                    GEO = row[11]
                    CRE = row[12]
                    AGR = row[13]
                    HSC = row[14]
                    BST = row[15]
                    PTS = row[28]
                    GRADE = row[29]
                    ENTRY = row[30]
                    TOTAL = row[31]
                    POS = row[32]
                    VAP = row[33]
                    TOT = row[46]
                    ###########
                    ENGg = row[34]
                    KISg = row[35]
                    MATg = row[36]
                    BIOg = row[37]
                    PHYg = row[38]
                    CHEg = row[39]
                    HISg = row[40]
                    GEOg = row[41]
                    CREg = row[42]
                    AGRg = row[43]
                    HSCg = row[44]
                    BSTg = row[45]
                    ##########
                    ENGp = row[16]
                    KISp = row[17]
                    MATp = row[24]
                    BIOp = row[27]
                    PHYp = row[26]
                    CHEp = row[25]
                    HISp = row[18]
                    GEOp = row[20]
                    CREp = row[21]
                    AGRp = row[22]
                    HSCp = row[19]
                    BSTp = row[23]
                    ############
                    ENGr = row[47]
                    KISr = row[48]
                    MATr = row[49]
                    BIOr = row[50]
                    PHYr = row[51]
                    CHEr = row[52]
                    HISr = row[53]
                    GEOr = row[54]
                    CREr = row[55]
                    AGRr = row[56]
                    HSCr = row[57]
                    BSTr = row[58]
                    ###############
                    ENGre = row[59]
                    KISre = row[60]
                    MATre = row[61]
                    BIOre = row[62]
                    PHYre = row[63]
                    CHEre = row[64]
                    HISre = row[65]
                    GEOre = row[66]
                    CREre = row[67]
                    AGRre = row[68]
                    HSCre = row[69]
                    BSTre = row[70]
                    CLASS = row[71]
                    TERM = row[72]
                    YEAR = row[73]
                    class11 = row[74]
                    year11 = row[75]
                    points11 = row[76]
                    grade11 = row[77]
                    position11 = row[78]

                    class12 = row[79]
                    year12 = row[80]
                    points12 = row[81]
                    grade12 = row[82]
                    position12 = row[83]
                    ######f1t3
                    class13 = row[84]
                    year13 = row[85]
                    points13 = row[86]
                    grade13 = row[87]
                    position13 = row[88]
                    ######f2t1
                    class21 = row[89]
                    year21 = row[90]
                    points21 = row[91]
                    grade21 = row[92]
                    position21 = row[93]
                    ######f2t2
                    class22 = row[94]
                    year22 = row[95]
                    points22 = row[96]
                    grade22 = row[97]
                    position22 = row[98]
                    ######f2t3
                    class23 = row[99]
                    year23 = row[100]
                    points23 = row[101]
                    grade23 = row[102]
                    position23 = row[103]
                    ######f3t1
                    class31 = row[104]
                    year31 = row[105]
                    points31 = row[106]
                    grade31 = row[107]
                    position31 = row[108]
                    ######f3t2
                    class32 = row[109]
                    year32 = row[110]
                    points32 = row[111]
                    grade32 = row[112]
                    position32 = row[113]
                    ######f3t3
                    class33 = row[114]
                    year33 = row[115]
                    points33 = row[116]
                    grade33 = row[117]
                    position33 = row[118]
                    ######f4t1
                    class41 = row[119]
                    year41 = row[120]
                    points41 = row[121]
                    grade41 = row[122]
                    position41 = row[123]
                    ######f4t2
                    class42 = row[124]
                    year42 = row[125]
                    points42 = row[126]
                    grade42 = row[127]
                    position42 = row[128]
                    ######f4t3
                    class43 = row[129]
                    year43 = row[130]
                    points43 = row[131]
                    grade43 = row[132]
                    position43 = row[133]
                    # Start using ReportLab to generate the pdfs 
                    c.drawImage("GULIK LOGO.png", 60, 650)
                    c.drawImage("GULIK LOGO.png", 400, 650)
                    c.drawString(205, 740, "FR GULIK URADI GIRLS SCHOOL")
                    c.drawString(235, 720, "P.O BOX 40-40608")
                    c.drawString(225, 700, "Phone: +254 708 836132")
                    c.drawString(190, 610, CLASS +' ' + TERM + ' ' + YEAR + ' REPORT FORM')
                    c.line(40,640, 550,640)
                    ######MARGIN LINES#3##
                    c.line(40,800, 550,800)
                    c.line(40,800, 40,10)
                    c.line(550,800, 550,10)
                    c.line(40,10, 550,10)#lowest line
                    #SUBJECT SEPARATOR LINES#
                    c.line(145,475, 450,475)
                    c.line(145,455, 450,455)
                    c.line(145,435, 450,435)
                    c.line(145,415, 450,415)
                    c.line(145,395, 450,395)
                    c.line(145,375, 450,375)
                    c.line(145,355, 450,355)
                    c.line(145,335, 450,335)
                    c.line(145,315, 450,315)
                    c.line(145,295, 450,295)
                    c.line(145,275, 450,275)
                    c.line(60,250, 510,250)

                    c.line(60,600, 510,600)
                    c.drawString(120, 580, "STUDENT NAME: " + NAME + '.  ' + '  ADM NO: ' + ADM)
                    c.line(160,570, 380,570)#########Between name and stream
                    c.drawString(160, 550, "STREAM: " + STREAM + "." + '    KCPE MARKS:  ' + '  ' + KCPE)
                    c.line(60,530, 510,530)
                    c.line(160,530, 160,250)########Table dividers
                    c.line(230,530, 230,250)
                    c.line(300,530, 300,250)
                    c.line(370,530, 370,250)
                    c.line(440,530, 440,250)
                    c.line(60,500, 510,500) 
                    c.drawString(60, 510, "SUBJECT")
                    c.drawString(170, 510, "SCORE")
                    c.drawString(240, 510, "GRADE")
                    c.drawString(310, 510, "POINTS")
                    c.drawString(380, 510, "RANK")
                    c.drawString(450, 510, "REMARKS")
                    c.drawString(60, 480, "ENGLISH")
                    c.drawString(60, 460, "KISWAHILI")
                    c.drawString(60, 440, "MATHS")
                    c.drawString(60, 420, "BIOLOGY")
                    c.drawString(60, 400, "PHYSICS")
                    c.drawString(60, 380, "CHEMISTRY")
                    c.drawString(60, 360, "HISTORY")
                    c.drawString(60, 340, "GEOGRAPHY")
                    c.drawString(60, 320, "CRE")
                    c.drawString(60, 300, "AGRICULTURE")
                    c.drawString(60, 280, "H/SCIENCE")
                    c.drawString(60, 260, 'B/STUDIES')
                    c.drawString(190, 480,ENG)
                    c.drawString(190, 460,KIS)
                    c.drawString(190, 440,MAT)
                    c.drawString(190, 420,BIO)
                    c.drawString(190, 400,PHY)
                    c.drawString(190, 380,CHE)
                    c.drawString(190, 360,HIS)
                    c.drawString(190, 340,GEO)
                    c.drawString(190, 320,CRE)
                    c.drawString(190, 300,AGR)
                    c.drawString(190, 280,HSC)
                    c.drawString(190, 260,BST)
                    ######GRADES#############
                    c.drawString(260, 480,ENGg)
                    c.drawString(260, 460,KISg)
                    c.drawString(260, 440,MATg)
                    c.drawString(260, 420,BIOg)
                    c.drawString(260, 400,PHYg)
                    c.drawString(260, 380,CHEg)
                    c.drawString(260, 360,HISg)
                    c.drawString(260, 340,GEOg)
                    c.drawString(260, 320,CREg)
                    c.drawString(260, 300,AGRg)
                    c.drawString(260, 280,HSCg)
                    c.drawString(260, 260,BSTg)
                    ###POINTS################
                    c.drawString(330, 480,ENGp)
                    c.drawString(330, 460,KISp)
                    c.drawString(330, 440,MATp)
                    c.drawString(330, 420,BIOp)
                    c.drawString(330, 400,PHYp)
                    c.drawString(330, 380,CHEp)
                    c.drawString(330, 360,HISp)
                    c.drawString(330, 340,GEOp)
                    c.drawString(330, 320,CREp)
                    c.drawString(330, 300,AGRp)
                    c.drawString(330, 280,HSCp)
                    c.drawString(330, 260,BSTp)
                    ###RANK################
                    c.drawString(400, 480,ENGr)
                    c.drawString(400, 460,KISr)
                    c.drawString(400, 440,MATr)
                    c.drawString(400, 420,BIOr)
                    c.drawString(400, 400,PHYr)
                    c.drawString(400, 380,CHEr)
                    c.drawString(400, 360,HISr)
                    c.drawString(400, 340,GEOr)
                    c.drawString(400, 320,CREr)
                    c.drawString(400, 300,AGRr)
                    c.drawString(400, 280,HSCr)
                    c.drawString(400, 260,BSTr)
                    ###REMARKS###############
                    c.drawString(450, 480,ENGre)
                    c.drawString(450, 460,KISre)
                    c.drawString(450, 440,MATre)
                    c.drawString(450, 420,BIOre)
                    c.drawString(450, 400,PHYre)
                    c.drawString(450, 380,CHEre)
                    c.drawString(450, 360,HISre)
                    c.drawString(450, 340,GEOre)
                    c.drawString(450, 320,CREre)
                    c.drawString(450, 300,AGRre)
                    c.drawString(450, 280,HSCre)
                    c.drawString(450, 260,BSTre)

                    c.drawString(130, 230, "Subject Entries: " + ENTRY + '.'+' Total Marks: '+ TOTAL + '.' + '  Total Points '+ '  ' + PTS )
                    c.line(130,220, 410,220) 
                    c.drawString(120, 200,'Grade: '+ GRADE + '     ' "Class Position:  " + POS +'  out of   ' + TOT)
                    c.drawString(370, 200,'VAP:  ' + VAP)
                    c.line(130,192, 410,192)
                    c.drawString(120, 175,'        PERFOMANCE TREND(FORM I - FORM IV')
                    #HORIZONTAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 510,170)
                    c.drawString(70, 155,'CLASS/YEAR')
                    c.drawString(155, 155,'FORM I ' + year11)
                    c.drawString(245, 155,'FORM II ' + year21)
                    c.drawString(335, 155,'FORM III ' + year31)
                    c.drawString(425, 155,'FORM IV ' + year41)
                    c.line(60,150, 510,150)
                    c.drawString(70, 135,'TERM                 I        II     III        I       II       III       I       II       III       I       II       III')
                    #c.drawString(155, 135,term11)
                    c.line(60,130, 510,130)
                    c.drawString(70, 115,'POSITION')
                    c.drawString(155, 115,position11)
                    c.drawString(185, 115,position12)
                    c.drawString(215, 115,position13)
                    c.drawString(245, 115,position21)
                    c.drawString(275, 115,position22)
                    c.drawString(305, 115,position23)
                    c.drawString(335, 115,position31)
                    c.drawString(365, 115,position32)
                    c.drawString(395, 115,position33)
                    c.drawString(425, 115,position41)
                    c.drawString(455, 115,position42)
                    c.drawString(485, 115,position43)
                    
                    c.line(60,110, 510,110)
                    c.drawString(70, 95,'POINTS')
                    c.drawString(155, 95,points11)
                    c.drawString(185, 95,points12)
                    c.drawString(215, 95,points13)
                    c.drawString(245, 95,points21)
                    c.drawString(275, 95,points22)
                    c.drawString(305, 95,points23)
                    c.drawString(335, 95,points31)
                    c.drawString(365, 95,points32)
                    c.drawString(395, 95,points33)
                    c.drawString(425, 95,points41)
                    c.drawString(455, 95,points42)
                    c.drawString(485, 95,points43)
                    
                    c.line(60,90, 510,90)
                    c.drawString(70, 75,'GRADE')
                    c.drawString(155, 75,grade11)
                    c.drawString(185, 75,grade12)
                    c.drawString(215, 75,grade13)
                    c.drawString(245, 75,grade21)
                    c.drawString(275, 75,grade22)
                    c.drawString(305, 75,grade23)
                    c.drawString(335, 75,grade31)
                    c.drawString(365, 75,grade32)
                    c.drawString(395, 75,grade33)
                    c.drawString(425, 75,grade41)
                    c.drawString(455, 75,grade42)
                    c.drawString(485, 75,grade43)
                    c.line(60,70, 510,70)
                    #VERTICAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 60,70)
                    c.line(150,170, 150,70)
                    c.line(180,150, 180,70)
                    c.line(210,150, 210,70)
                    c.line(240,170, 240,70)
                    c.line(270,150, 270,70)
                    c.line(300,150, 300,70)
                    c.line(330,170, 330,70)
                    c.line(360,150, 360,70)
                    c.line(390,150, 390,70)
                    c.line(420,170, 420,70)
                    c.line(450,150, 450,70)
                    c.line(480,150, 480,70)
                    c.line(510,170, 510,70)
                    c.drawString(60,35, "This term's fee_________Paid__________Balance_________Next Term_________")
                    c.showPage()
                c.save()  
                #PROMPTING THE USER TO SAVE THE REPORT FORMS########################
                saving_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "REPORT FORMS.pdf")
                existing_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                name_and_extension = QFileDialog.getSaveFileName(MainWindow, "Save Report Cards",os.path.expanduser("~/Documents"),"Save pdf(*.pdf);;excel(*.xlsx)")#;;Save excel(*.xlsx))")
                if name_and_extension:
                    try:
                        with open(name_and_extension[0],'w') as user_prefer:
                            user_prefer.writelines(open(existing_file))
                    except IOError:
                        pass
                os.remove(existing_file) 
                QMessageBox.information(MainWindow,'Successful','Report forms successfully generated and saved in the location you selected.')
            elif klass == 'FORM III':
                #FORM I
                dataf1t1 = ("FORM I TERM I "+str(int(year) - 2)+" report")
                try:
                    f1t1 = pd.read_sql("SELECT * FROM '" + str(dataf1t1) + "'", conn)
                except:
                    f1t1 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf1t2 = ("FORM I TERM II "+str(int(year) - 2)+" report")
                try:
                    f1t2 = pd.read_sql("SELECT * FROM '" + str(dataf1t2) + "'", conn)
                except:
                    f1t2 = pd.read_sql("SELECT * FROM report_generator", conn)
            
                dataf1t3 = ("FORM I TERM III "+str(int(year) - 2)+" report")
                try:
                    f1t3 = pd.read_sql("SELECT * FROM '" + str(dataf1t3) + "'" or "report_generator", conn)
                except:
                    f1t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM II
                dataf2t1 = ("FORM II TERM I "+str(int(year) - 1)+" report")
                try:
                    f2t1 = pd.read_sql("SELECT * FROM '" + str(dataf2t1) + "'", conn)
                except:
                    f2t1 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf2t2 = ("FORM II TERM II "+str(int(year) - 1)+" report")
                try:
                    f2t2 = pd.read_sql("SELECT * FROM '" + str(dataf2t2) + "'", conn)
                except:
                    f2t2 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf2t3 = ("FORM II TERM III "+str(int(year) - 1)+" report")
                try:
                    f2t3 = pd.read_sql("SELECT * FROM '" + str(dataf2t3) + "'", conn)
                except:
                    f2t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM III
                dataf3t1 = ("FORM III TERM I "+str(year)+" report")
                try:
                    f3t1 = pd.read_sql("SELECT * FROM '" + str(dataf3t1) + "'", conn)
                except:
                    f3t1 = pd.read_sql("SELECT * FROM report_generator", conn)

                dataf3t2 = ("FORM III TERM II "+str(year)+" report")
                try:
                    f3t2 = pd.read_sql("SELECT * FROM '" + str(dataf3t2) + "'", conn)
                except:
                    f3t2 = pd.read_sql("SELECT * FROM report_generator", conn)
                
                dataf3t3 = ("FORM III TERM III "+str(year)+" report")
                try:
                    f3t3 = pd.read_sql("SELECT * FROM '" + str(dataf3t3) + "'", conn)
                except:
                    f3t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                students_data = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report"     
                temp = pd.read_sql("SELECT * FROM '" + str(students_data) + "'", conn)
                #additional columns
                #Term I
                temp['class11'] = f1t1.CLASS
                temp['year11'] = f1t1.YEAR
                temp['points11'] = f1t1.PTS
                temp['grade11'] = f1t1.GRADE
                temp['position11'] = f1t1.POS
                #Term II
                temp['class12'] = f1t2.CLASS
                temp['year12'] = f1t2.YEAR
                temp['points12'] = f1t2.PTS
                temp['grade12'] = f1t2.GRADE
                temp['position12'] = f1t2.POS
                #Term III
                temp['class13'] = f1t3.CLASS
                temp['year13'] = f1t3.YEAR
                temp['points13'] = f1t3.PTS
                temp['grade13'] = f1t3.GRADE
                temp['position13'] = f1t3.POS
                #f2 Term I
                temp['class21'] = f2t1.CLASS
                temp['year21'] = f2t1.YEAR
                temp['points21'] = f2t1.PTS
                temp['grade21'] = f2t1.GRADE
                temp['position21'] = f2t1.POS
                #Term II
                temp['class22'] = f2t2.CLASS
                temp['year22'] = f2t2.YEAR
                temp['points22'] = f2t2.PTS
                temp['grade22'] = f2t2.GRADE
                temp['position22'] = f2t2.POS
                #Term III
                temp['class23'] = f2t3.CLASS
                temp['year23'] = f2t3.YEAR
                temp['points23'] = f2t3.PTS
                temp['grade23'] = f2t3.GRADE
                temp['position23'] = f2t3.POS
                #TermI
                temp['class31'] = f3t1.CLASS
                temp['year31'] = f3t1.YEAR
                temp['points31'] = f3t1.PTS
                temp['grade31'] = f3t1.GRADE
                temp['position31'] = f3t1.POS
                #Term II
                temp['class32'] = f3t2.CLASS
                temp['year32'] = f3t2.YEAR
                temp['points32'] = f3t2.PTS
                temp['grade32'] = f3t2.GRADE
                temp['position32'] = f3t2.POS
                #Term III
                temp['class33'] = f3t3.CLASS
                temp['year33'] = f3t3.YEAR
                temp['points33'] = f3t3.PTS
                temp['grade33'] = f3t3.GRADE
                temp['position33'] = f3t3.POS
                #temp.to_csv('me.csv',index=False)
                students_data2 = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report2"            
                temp.to_sql(students_data2,conn,if_exists='replace',index=False)
                students_data = pd.read_sql("SELECT * FROM '" + str(students_data2) + "'", conn)
                
                temp = tempfile.NamedTemporaryFile(delete=True)
                students_data.to_csv(temp.name + '.csv',index=False)
                temp.flush()
                temp.seek(0)
                temp = csv.reader(open(temp.name + '.csv','r'))

                c = canvas.Canvas(self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                for row in ([x for x in temp][1:]):
                    STREAM = row[0]
                    ADM = row[1]
                    NAME = row[2]
                    KCPE = row[3]
                    ENG = row[4]
                    KIS = row[5]
                    MAT = row[6]
                    BIO = row[7]
                    PHY = row[8]
                    CHE = row[9]
                    HIS = row[10]
                    GEO = row[11]
                    CRE = row[12]
                    AGR = row[13]
                    HSC = row[14]
                    BST = row[15]
                    PTS = row[28]
                    GRADE = row[29]
                    ENTRY = row[30]
                    TOTAL = row[31]
                    POS = row[32]
                    VAP = row[33]
                    TOT = row[46]
                    ###########
                    ENGg = row[34]
                    KISg = row[35]
                    MATg = row[36]
                    BIOg = row[37]
                    PHYg = row[38]
                    CHEg = row[39]
                    HISg = row[40]
                    GEOg = row[41]
                    CREg = row[42]
                    AGRg = row[43]
                    HSCg = row[44]
                    BSTg = row[45]
                    ##########
                    ENGp = row[16]
                    KISp = row[17]
                    MATp = row[24]
                    BIOp = row[27]
                    PHYp = row[26]
                    CHEp = row[25]
                    HISp = row[18]
                    GEOp = row[20]
                    CREp = row[21]
                    AGRp = row[22]
                    HSCp = row[19]
                    BSTp = row[23]
                    ############
                    ENGr = row[47]
                    KISr = row[48]
                    MATr = row[49]
                    BIOr = row[50]
                    PHYr = row[51]
                    CHEr = row[52]
                    HISr = row[53]
                    GEOr = row[54]
                    CREr = row[55]
                    AGRr = row[56]
                    HSCr = row[57]
                    BSTr = row[58]
                    ###############
                    ENGre = row[59]
                    KISre = row[60]
                    MATre = row[61]
                    BIOre = row[62]
                    PHYre = row[63]
                    CHEre = row[64]
                    HISre = row[65]
                    GEOre = row[66]
                    CREre = row[67]
                    AGRre = row[68]
                    HSCre = row[69]
                    BSTre = row[70]
                    CLASS = row[71]
                    TERM = row[72]
                    YEAR = row[73]
                    ######f1t1
                    class11 = row[74]
                    year11 = row[75]
                    points11 = row[76]
                    grade11 = row[77]
                    position11 = row[78]
                    ######f1t2
                    class12 = row[79]
                    year12 = row[80]
                    points12 = row[81]
                    grade12 = row[82]
                    position12 = row[83]
                    ######f1t3
                    class13 = row[84]
                    year13 = row[85]
                    points13 = row[86]
                    grade13 = row[87]
                    position13 = row[88]
                    ######f2t1
                    class21 = row[89]
                    year21 = row[90]
                    points21 = row[91]
                    grade21 = row[92]
                    position21 = row[93]
                    ######f2t2
                    class22 = row[94]
                    year22 = row[95]
                    points22 = row[96]
                    grade22 = row[97]
                    position22 = row[98]
                    ######f2t3
                    class23 = row[99]
                    year23 = row[100]
                    points23 = row[101]
                    grade23 = row[102]
                    position23 = row[103]
                    ######f3t1
                    class31 = row[104]
                    year31 = row[105]
                    points31 = row[106]
                    grade31 = row[107]
                    position31 = row[108]
                    ######f3t2
                    class32 = row[109]
                    year32 = row[110]
                    points32 = row[111]
                    grade32 = row[112]
                    position32 = row[113]
                    ######f3t3
                    class33 = row[114]
                    year33 = row[115]
                    points33 = row[116]
                    grade33 = row[117]
                    position33 = row[118]
                    # Start using ReportLab to generate the pdfs 
                    c.drawImage("GULIK LOGO.png", 60, 650)
                    c.drawImage("GULIK LOGO.png", 400, 650)
                    c.drawString(205, 740, "FR GULIK URADI GIRLS SCHOOL")
                    c.drawString(235, 720, "P.O BOX 40-40608")
                    c.drawString(225, 700, "Phone: +254 708 836132")
                    c.drawString(190, 610, CLASS +' ' + TERM + ' ' + YEAR + ' REPORT FORM')
                    c.line(40,640, 550,640)
                    ######MARGIN LINES#3##
                    c.line(40,800, 550,800)
                    c.line(40,800, 40,10)
                    c.line(550,800, 550,10)
                    c.line(40,10, 550,10)#lowest line
                    #SUBJECT SEPARATOR LINES#
                    c.line(145,475, 450,475)
                    c.line(145,455, 450,455)
                    c.line(145,435, 450,435)
                    c.line(145,415, 450,415)
                    c.line(145,395, 450,395)
                    c.line(145,375, 450,375)
                    c.line(145,355, 450,355)
                    c.line(145,335, 450,335)
                    c.line(145,315, 450,315)
                    c.line(145,295, 450,295)
                    c.line(145,275, 450,275)
                    c.line(60,250, 510,250)

                    c.line(60,600, 510,600)
                    c.drawString(120, 580, "STUDENT NAME: " + NAME + '.  ' + '  ADM NO: ' + ADM)
                    c.line(160,570, 380,570)#########Between name and stream
                    c.drawString(160, 550, "STREAM: " + STREAM + "." + '    KCPE MARKS:  ' + '  ' + KCPE)
                    c.line(60,530, 510,530)
                    c.line(160,530, 160,250)########Table dividers
                    c.line(230,530, 230,250)
                    c.line(300,530, 300,250)
                    c.line(370,530, 370,250)
                    c.line(440,530, 440,250)
                    c.line(60,500, 510,500) 
                    c.drawString(60, 510, "SUBJECT")
                    c.drawString(170, 510, "SCORE")
                    c.drawString(240, 510, "GRADE")
                    c.drawString(310, 510, "POINTS")
                    c.drawString(380, 510, "RANK")
                    c.drawString(450, 510, "REMARKS")
                    c.drawString(60, 480, "ENGLISH")
                    c.drawString(60, 460, "KISWAHILI")
                    c.drawString(60, 440, "MATHS")
                    c.drawString(60, 420, "BIOLOGY")
                    c.drawString(60, 400, "PHYSICS")
                    c.drawString(60, 380, "CHEMISTRY")
                    c.drawString(60, 360, "HISTORY")
                    c.drawString(60, 340, "GEOGRAPHY")
                    c.drawString(60, 320, "CRE")
                    c.drawString(60, 300, "AGRICULTURE")
                    c.drawString(60, 280, "H/SCIENCE")
                    c.drawString(60, 260, 'B/STUDIES')
                    c.drawString(190, 480,ENG)
                    c.drawString(190, 460,KIS)
                    c.drawString(190, 440,MAT)
                    c.drawString(190, 420,BIO)
                    c.drawString(190, 400,PHY)
                    c.drawString(190, 380,CHE)
                    c.drawString(190, 360,HIS)
                    c.drawString(190, 340,GEO)
                    c.drawString(190, 320,CRE)
                    c.drawString(190, 300,AGR)
                    c.drawString(190, 280,HSC)
                    c.drawString(190, 260,BST)
                    ######GRADES#############
                    c.drawString(260, 480,ENGg)
                    c.drawString(260, 460,KISg)
                    c.drawString(260, 440,MATg)
                    c.drawString(260, 420,BIOg)
                    c.drawString(260, 400,PHYg)
                    c.drawString(260, 380,CHEg)
                    c.drawString(260, 360,HISg)
                    c.drawString(260, 340,GEOg)
                    c.drawString(260, 320,CREg)
                    c.drawString(260, 300,AGRg)
                    c.drawString(260, 280,HSCg)
                    c.drawString(260, 260,BSTg)
                    ###POINTS################
                    c.drawString(330, 480,ENGp)
                    c.drawString(330, 460,KISp)
                    c.drawString(330, 440,MATp)
                    c.drawString(330, 420,BIOp)
                    c.drawString(330, 400,PHYp)
                    c.drawString(330, 380,CHEp)
                    c.drawString(330, 360,HISp)
                    c.drawString(330, 340,GEOp)
                    c.drawString(330, 320,CREp)
                    c.drawString(330, 300,AGRp)
                    c.drawString(330, 280,HSCp)
                    c.drawString(330, 260,BSTp)
                    ###RANK################
                    c.drawString(400, 480,ENGr)
                    c.drawString(400, 460,KISr)
                    c.drawString(400, 440,MATr)
                    c.drawString(400, 420,BIOr)
                    c.drawString(400, 400,PHYr)
                    c.drawString(400, 380,CHEr)
                    c.drawString(400, 360,HISr)
                    c.drawString(400, 340,GEOr)
                    c.drawString(400, 320,CREr)
                    c.drawString(400, 300,AGRr)
                    c.drawString(400, 280,HSCr)
                    c.drawString(400, 260,BSTr)
                    ###REMARKS###############
                    c.drawString(450, 480,ENGre)
                    c.drawString(450, 460,KISre)
                    c.drawString(450, 440,MATre)
                    c.drawString(450, 420,BIOre)
                    c.drawString(450, 400,PHYre)
                    c.drawString(450, 380,CHEre)
                    c.drawString(450, 360,HISre)
                    c.drawString(450, 340,GEOre)
                    c.drawString(450, 320,CREre)
                    c.drawString(450, 300,AGRre)
                    c.drawString(450, 280,HSCre)
                    c.drawString(450, 260,BSTre)

                    c.drawString(130, 230, "Subject Entries: " + ENTRY + '.'+' Total Marks: '+ TOTAL + '.' + '  Total Points '+ '  ' + PTS )
                    c.line(130,220, 410,220) 
                    c.drawString(120, 200,'Grade: '+ GRADE + '     ' "Class Position:  " + POS +'  out of   ' + TOT)
                    c.drawString(370, 200,'VAP:  ' + VAP)
                    c.line(130,192, 410,192)
                    c.drawString(120, 175,'        PERFOMANCE TREND(FORM I - FORM IV')
                    #HORIZONTAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 510,170)
                    c.drawString(70, 155,'CLASS/YEAR')
                    c.drawString(155, 155,'FORM I ' + year11)
                    c.drawString(245, 155,'FORM II ' + year21)
                    c.drawString(335, 155,'FORM III ' + year31)
                    c.line(60,150, 510,150)
                    c.drawString(70, 135,'TERM                 I        II     III        I       II       III        I       II       III')
                    #c.drawString(155, 135,term11)
                    c.line(60,130, 510,130)
                    c.drawString(70, 115,'POSITION')
                    c.drawString(155, 115,position11)
                    c.drawString(185, 115,position12)
                    c.drawString(215, 115,position13)
                    c.drawString(245, 115,position21)
                    c.drawString(275, 115,position22)
                    c.drawString(305, 115,position23)
                    c.drawString(335, 115,position31)
                    c.drawString(365, 115,position32)
                    c.drawString(395, 115,position33)
                    c.line(60,110, 510,110)
                    c.drawString(70, 95,'POINTS')
                    c.drawString(155, 95,points11)
                    c.drawString(185, 95,points12)
                    c.drawString(215, 95,points13)
                    c.drawString(245, 95,points21)
                    c.drawString(275, 95,points22)
                    c.drawString(305, 95,points23)
                    c.drawString(335, 95,points31)
                    c.drawString(365, 95,points32)
                    c.drawString(395, 95,points33)
                    c.line(60,90, 510,90)
                    c.drawString(70, 75,'GRADE')
                    c.drawString(155, 75,grade11)
                    c.drawString(185, 75,grade12)
                    c.drawString(215, 75,grade13)
                    c.drawString(245, 75,grade21)
                    c.drawString(275, 75,grade22)
                    c.drawString(305, 75,grade23)
                    c.drawString(335, 75,grade31)
                    c.drawString(365, 75,grade32)
                    c.drawString(395, 75,grade33)
                    c.line(60,70, 510,70)
                    #VERTICAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 60,70)
                    c.line(150,170, 150,70)
                    c.line(180,150, 180,70)
                    c.line(210,150, 210,70)
                    c.line(240,170, 240,70)
                    c.line(270,150, 270,70)
                    c.line(300,150, 300,70)
                    c.line(330,170, 330,70)
                    c.line(360,150, 360,70)
                    c.line(390,150, 390,70)
                    c.line(420,170, 420,70)
                    c.line(450,150, 450,70)
                    c.line(480,150, 480,70)
                    c.line(510,170, 510,70)
                    c.drawString(60,35, "This term's fee_________Paid__________Balance_________Next Term_________")
                    c.showPage()
                c.save()  
                #PROMPTING THE USER TO SAVE THE REPORT FORMS########################
                saving_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "REPORT FORMS.pdf")
                existing_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                name_and_extension = QFileDialog.getSaveFileName(MainWindow, "Save Report Cards",os.path.expanduser("~/Documents"),"Save pdf(*.pdf);;excel(*.xlsx)")#;;Save excel(*.xlsx))")
                if name_and_extension:
                    try:
                        with open(name_and_extension[0],'w') as user_prefer:
                            user_prefer.writelines(open(existing_file))
                    except IOError:
                        pass
                QMessageBox.information(MainWindow,'Successful','Report forms successfully generated and saved in the location you selected.')
            elif klass == 'FORM II':
                #FORM I TI
                dataf1t1 = ("FORM I TERM I "+str(int(year) - 1)+" report")
                try:
                    f1t1 = pd.read_sql("SELECT * FROM '" + str(dataf1t1) + "'", conn)
                except:
                    f1t1 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM I T1I
                dataf1t2 = ("FORM I TERM II "+str(int(year) - 1)+" report")
                try:
                    f1t2 = pd.read_sql("SELECT * FROM '" + str(dataf1t2) + "'", conn)
                except:
                    f1t2 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM I T1II
                dataf1t3 = ("FORM I TERM III "+str(int(year) - 1)+" report")
                try:
                    f1t3 = pd.read_sql("SELECT * FROM '" + str(dataf1t3) + "'" or "report_generator", conn)
                except:
                    f1t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM II T1
                dataf2t1 = ("FORM II TERM I "+str(year)+" report")
                try:
                    f2t1 = pd.read_sql("SELECT * FROM '" + str(dataf2t1) + "'", conn)
                except:
                    f2t1 = pd.read_sql("SELECT * FROM report_generator", conn)
                #FORM II T1I
                dataf2t2 = ("FORM II TERM II "+str(year)+" report")
                try:
                    f2t2 = pd.read_sql("SELECT * FROM '" + str(dataf2t2) + "'", conn)
                except:
                    f2t2 = pd.read_sql("SELECT * FROM report_generator", conn)
                    #FORM II T1I
                dataf2t3 = ("FORM II TERM III "+str(year)+" report")
                try:
                    f2t3 = pd.read_sql("SELECT * FROM '" + str(dataf2t3) + "'", conn)
                except:
                    f2t3 = pd.read_sql("SELECT * FROM report_generator", conn)
               
                students_data = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report"     
                temp = pd.read_sql("SELECT * FROM '" + str(students_data) + "'", conn)
                #additional columns
                #Term I
                temp['class11'] = f1t1.CLASS
                temp['year11'] = f1t1.YEAR
                temp['points11'] = f1t1.PTS
                temp['grade11'] = f1t1.GRADE
                temp['position11'] = f1t1.POS
                #Term II
                temp['class12'] = f1t2.CLASS
                temp['year12'] = f1t2.YEAR
                temp['points12'] = f1t2.PTS
                temp['grade12'] = f1t2.GRADE
                temp['position12'] = f1t2.POS
                #Term III
                temp['class13'] = f1t3.CLASS
                temp['year13'] = f1t3.YEAR
                temp['points13'] = f1t3.PTS
                temp['grade13'] = f1t3.GRADE
                temp['position13'] = f1t3.POS
                #f2 Term I
                temp['class21'] = f2t1.CLASS
                temp['year21'] = f2t1.YEAR
                temp['points21'] = f2t1.PTS
                temp['grade21'] = f2t1.GRADE
                temp['position21'] = f2t1.POS
                #Term II
                temp['class22'] = f2t2.CLASS
                temp['year22'] = f2t2.YEAR
                temp['points22'] = f2t2.PTS
                temp['grade22'] = f2t2.GRADE
                temp['position22'] = f2t2.POS
                #Term III
                temp['class23'] = f2t3.CLASS
                temp['year23'] = f2t3.YEAR
                temp['points23'] = f2t3.PTS
                temp['grade23'] = f2t3.GRADE
                temp['position23'] = f2t3.POS
                #temp.to_csv('me.csv',index=False)
                students_data2 = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report2"            
                temp.to_sql(students_data2,conn,if_exists='replace',index=False)
                students_data = pd.read_sql("SELECT * FROM '" + str(students_data2) + "'", conn)
                
                temp = tempfile.NamedTemporaryFile(delete=True)
                students_data.to_csv(temp.name + '.csv',index=False)
                temp.flush()
                temp.seek(0)
                temp = csv.reader(open(temp.name + '.csv','r'))
                c = canvas.Canvas(self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                for row in ([x for x in temp][1:]):
                    STREAM = row[0]
                    ADM = row[1]
                    NAME = row[2]
                    KCPE = row[3]
                    ENG = row[4]
                    KIS = row[5]
                    MAT = row[6]
                    BIO = row[7]
                    PHY = row[8]
                    CHE = row[9]
                    HIS = row[10]
                    GEO = row[11]
                    CRE = row[12]
                    AGR = row[13]
                    HSC = row[14]
                    BST = row[15]
                    PTS = row[28]
                    GRADE = row[29]
                    ENTRY = row[30]
                    TOTAL = row[31]
                    POS = row[32]
                    VAP = row[33]
                    TOT = row[46]
                    ###########
                    ENGg = row[34]
                    KISg = row[35]
                    MATg = row[36]
                    BIOg = row[37]
                    PHYg = row[38]
                    CHEg = row[39]
                    HISg = row[40]
                    GEOg = row[41]
                    CREg = row[42]
                    AGRg = row[43]
                    HSCg = row[44]
                    BSTg = row[45]
                    ##########
                    ENGp = row[16]
                    KISp = row[17]
                    MATp = row[24]
                    BIOp = row[27]
                    PHYp = row[26]
                    CHEp = row[25]
                    HISp = row[18]
                    GEOp = row[20]
                    CREp = row[21]
                    AGRp = row[22]
                    HSCp = row[19]
                    BSTp = row[23]
                    ############
                    ENGr = row[47]
                    KISr = row[48]
                    MATr = row[49]
                    BIOr = row[50]
                    PHYr = row[51]
                    CHEr = row[52]
                    HISr = row[53]
                    GEOr = row[54]
                    CREr = row[55]
                    AGRr = row[56]
                    HSCr = row[57]
                    BSTr = row[58]
                    ###############
                    ENGre = row[59]
                    KISre = row[60]
                    MATre = row[61]
                    BIOre = row[62]
                    PHYre = row[63]
                    CHEre = row[64]
                    HISre = row[65]
                    GEOre = row[66]
                    CREre = row[67]
                    AGRre = row[68]
                    HSCre = row[69]
                    BSTre = row[70]
                    CLASS = row[71]
                    TERM = row[72]
                    YEAR = row[73]
                    ######f1t1
                    class11 = row[74]
                    year11 = row[75]
                    points11 = row[76]
                    grade11 = row[77]
                    position11 = row[78]
                    ######f1t2
                    class12 = row[79]
                    year12 = row[80]
                    points12 = row[81]
                    grade12 = row[82]
                    position12 = row[83]
                    ######f1t3
                    class13 = row[84]
                    year13 = row[85]
                    points13 = row[86]
                    grade13 = row[87]
                    position13 = row[88]
                    ######f2t1
                    class21 = row[89]
                    year21 = row[90]
                    points21 = row[91]
                    grade21 = row[92]
                    position21 = row[93]
                    ######f2t2
                    class22 = row[94]
                    year22 = row[95]
                    points22 = row[96]
                    grade22 = row[97]
                    position22 = row[98]
                    ######f2t3
                    class23 = row[99]
                    year23 = row[100]
                    points23 = row[101]
                    grade23 = row[102]
                    position23 = row[103]
                    # Start using ReportLab to generate the pdfs 
                    c.drawImage("GULIK LOGO.png", 60, 650)
                    c.drawImage("GULIK LOGO.png", 400, 650)
                    c.drawString(205, 740, "FR GULIK URADI GIRLS SCHOOL")
                    c.drawString(235, 720, "P.O BOX 40-40608")
                    c.drawString(225, 700, "Phone: +254 708 836132")
                    c.drawString(190, 610, CLASS +' ' + TERM + ' ' + YEAR + ' REPORT FORM')
                    c.line(40,640, 550,640)
                    ######MARGIN LINES#3##
                    c.line(40,800, 550,800)
                    c.line(40,800, 40,10)
                    c.line(550,800, 550,10)
                    c.line(40,10, 550,10)#lowest line
                    #SUBJECT SEPARATOR LINES#
                    c.line(145,475, 450,475)
                    c.line(145,455, 450,455)
                    c.line(145,435, 450,435)
                    c.line(145,415, 450,415)
                    c.line(145,395, 450,395)
                    c.line(145,375, 450,375)
                    c.line(145,355, 450,355)
                    c.line(145,335, 450,335)
                    c.line(145,315, 450,315)
                    c.line(145,295, 450,295)
                    c.line(145,275, 450,275)
                    c.line(60,250, 510,250)

                    c.line(60,600, 510,600)
                    c.drawString(120, 580, "STUDENT NAME: " + NAME + '.  ' + '  ADM NO: ' + ADM)
                    c.line(160,570, 380,570)#########Between name and stream
                    c.drawString(160, 550, "STREAM: " + STREAM + "." + '    KCPE MARKS:  ' + '  ' + KCPE)
                    c.line(60,530, 510,530)
                    c.line(160,530, 160,250)########Table dividers
                    c.line(230,530, 230,250)
                    c.line(300,530, 300,250)
                    c.line(370,530, 370,250)
                    c.line(440,530, 440,250)
                    c.line(60,500, 510,500) 
                    c.drawString(60, 510, "SUBJECT")
                    c.drawString(170, 510, "SCORE")
                    c.drawString(240, 510, "GRADE")
                    c.drawString(310, 510, "POINTS")
                    c.drawString(380, 510, "RANK")
                    c.drawString(450, 510, "REMARKS")
                    c.drawString(60, 480, "ENGLISH")
                    c.drawString(60, 460, "KISWAHILI")
                    c.drawString(60, 440, "MATHS")
                    c.drawString(60, 420, "BIOLOGY")
                    c.drawString(60, 400, "PHYSICS")
                    c.drawString(60, 380, "CHEMISTRY")
                    c.drawString(60, 360, "HISTORY")
                    c.drawString(60, 340, "GEOGRAPHY")
                    c.drawString(60, 320, "CRE")
                    c.drawString(60, 300, "AGRICULTURE")
                    c.drawString(60, 280, "H/SCIENCE")
                    c.drawString(60, 260, 'B/STUDIES')
                    c.drawString(190, 480,ENG)
                    c.drawString(190, 460,KIS)
                    c.drawString(190, 440,MAT)
                    c.drawString(190, 420,BIO)
                    c.drawString(190, 400,PHY)
                    c.drawString(190, 380,CHE)
                    c.drawString(190, 360,HIS)
                    c.drawString(190, 340,GEO)
                    c.drawString(190, 320,CRE)
                    c.drawString(190, 300,AGR)
                    c.drawString(190, 280,HSC)
                    c.drawString(190, 260,BST)
                    ######GRADES#############
                    c.drawString(260, 480,ENGg)
                    c.drawString(260, 460,KISg)
                    c.drawString(260, 440,MATg)
                    c.drawString(260, 420,BIOg)
                    c.drawString(260, 400,PHYg)
                    c.drawString(260, 380,CHEg)
                    c.drawString(260, 360,HISg)
                    c.drawString(260, 340,GEOg)
                    c.drawString(260, 320,CREg)
                    c.drawString(260, 300,AGRg)
                    c.drawString(260, 280,HSCg)
                    c.drawString(260, 260,BSTg)
                    ###POINTS################
                    c.drawString(330, 480,ENGp)
                    c.drawString(330, 460,KISp)
                    c.drawString(330, 440,MATp)
                    c.drawString(330, 420,BIOp)
                    c.drawString(330, 400,PHYp)
                    c.drawString(330, 380,CHEp)
                    c.drawString(330, 360,HISp)
                    c.drawString(330, 340,GEOp)
                    c.drawString(330, 320,CREp)
                    c.drawString(330, 300,AGRp)
                    c.drawString(330, 280,HSCp)
                    c.drawString(330, 260,BSTp)
                    ###RANK################
                    c.drawString(400, 480,ENGr)
                    c.drawString(400, 460,KISr)
                    c.drawString(400, 440,MATr)
                    c.drawString(400, 420,BIOr)
                    c.drawString(400, 400,PHYr)
                    c.drawString(400, 380,CHEr)
                    c.drawString(400, 360,HISr)
                    c.drawString(400, 340,GEOr)
                    c.drawString(400, 320,CREr)
                    c.drawString(400, 300,AGRr)
                    c.drawString(400, 280,HSCr)
                    c.drawString(400, 260,BSTr)
                    ###REMARKS###############
                    c.drawString(450, 480,ENGre)
                    c.drawString(450, 460,KISre)
                    c.drawString(450, 440,MATre)
                    c.drawString(450, 420,BIOre)
                    c.drawString(450, 400,PHYre)
                    c.drawString(450, 380,CHEre)
                    c.drawString(450, 360,HISre)
                    c.drawString(450, 340,GEOre)
                    c.drawString(450, 320,CREre)
                    c.drawString(450, 300,AGRre)
                    c.drawString(450, 280,HSCre)
                    c.drawString(450, 260,BSTre)

                    c.drawString(130, 230, "Subject Entries: " + ENTRY + '.'+' Total Marks: '+ TOTAL + '.' + '  Total Points '+ '  ' + PTS )
                    c.line(130,220, 410,220) 
                    c.drawString(120, 200,'Grade: '+ GRADE + '     ' "Class Position:  " + POS +'  out of   ' + TOT)
                    c.drawString(370, 200,'VAP:  ' + VAP)
                    c.line(130,192, 410,192)
                    c.drawString(120, 175,'        PERFOMANCE TREND(FORM I - FORM IV')
                    #HORIZONTAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 510,170)
                    c.drawString(70, 155,'CLASS/YEAR')
                    c.drawString(155, 155,'FORM I ' + year11)
                    c.drawString(245, 155,'FORM II ' + year21)
                    c.line(60,150, 510,150)
                    c.drawString(70, 135,'TERM                 I        II     III        I       II       III')
                    #c.drawString(155, 135,term11)
                    c.line(60,130, 510,130)
                    c.drawString(70, 115,'POSITION')
                    c.drawString(155, 115,position11)
                    c.drawString(185, 115,position12)
                    c.drawString(215, 115,position13)
                    c.drawString(245, 115,position21)
                    c.drawString(275, 115,position22)
                    c.drawString(305, 115,position23)
                    c.line(60,110, 510,110)
                    c.drawString(70, 95,'POINTS')
                    c.drawString(155, 95,points11)
                    c.drawString(185, 95,points12)
                    c.drawString(215, 95,points13)
                    c.drawString(245, 95,points21)
                    c.drawString(275, 95,points22)
                    c.drawString(305, 95,points23)
                    c.line(60,90, 510,90)
                    c.drawString(70, 75,'GRADE')
                    c.drawString(155, 75,grade11)
                    c.drawString(185, 75,grade12)
                    c.drawString(215, 75,grade13)
                    c.drawString(245, 75,grade21)
                    c.drawString(275, 75,grade22)
                    c.drawString(305, 75,grade23)
                    c.line(60,70, 510,70)
                    #VERTICAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 60,70)
                    c.line(150,170, 150,70)
                    c.line(180,150, 180,70)
                    c.line(210,150, 210,70)
                    c.line(240,170, 240,70)
                    c.line(270,150, 270,70)
                    c.line(300,150, 300,70)
                    c.line(330,170, 330,70)
                    c.line(360,150, 360,70)
                    c.line(390,150, 390,70)
                    c.line(420,170, 420,70)
                    c.line(450,150, 450,70)
                    c.line(480,150, 480,70)
                    c.line(510,170, 510,70)
                    c.drawString(60,35, "This term's fee_________Paid__________Balance_________Next Term_________")
                    c.showPage()
                c.save()  
                #PROMPTING THE USER TO SAVE THE REPORT FORMS########################
                saving_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "REPORT FORMS.pdf")
                existing_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                name_and_extension = QFileDialog.getSaveFileName(MainWindow, "Save Report Cards",os.path.expanduser("~/Documents"),"Save pdf(*.pdf);;excel(*.xlsx)")#;;Save excel(*.xlsx))")
                if name_and_extension:
                    try:
                        with open(name_and_extension[0],'w') as user_prefer:
                            user_prefer.writelines(open(existing_file))
                    except IOError:
                        pass
                QMessageBox.information(MainWindow,'Successful','Report forms successfully generated and saved in the location you selected.')
            
            elif klass == 'FORM I':
                #Form I term I
                dataf1t1 = ("FORM I TERM I "+str(year)+" report")
                try:
                    f1t1 = pd.read_sql("SELECT * FROM '" + str(dataf1t1) + "'", conn)
                except:
                    f1t1 = pd.read_sql("SELECT * FROM report_generator", conn)
                #Form I term II
                dataf1t2 = ("FORM I TERM II "+str(year)+" report")
                try:
                    f1t2 = pd.read_sql("SELECT * FROM '" + str(dataf1t2) + "'", conn)
                except:
                    f1t2 = pd.read_sql("SELECT * FROM report_generator", conn)
                #Form I term III
                dataf1t3 = ("FORM I TERM III "+str(year)+" report")
                try:
                    f1t3 = pd.read_sql("SELECT * FROM '" + str(dataf1t3) + "'" or "report_generator", conn)
                except:
                    f1t3 = pd.read_sql("SELECT * FROM report_generator", conn)
                #Grabbing the table from the database
                students_data = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report"     
                temp = pd.read_sql("SELECT * FROM '" + str(students_data) + "'", conn)
                #additional columns
                #Term I
                temp['class11'] = f1t1.CLASS
                temp['year11'] = f1t1.YEAR
                temp['points11'] = f1t1.PTS
                temp['grade11'] = f1t1.GRADE
                temp['position11'] = f1t1.POS
                #Term II
                temp['class12'] = f1t2.CLASS
                temp['year12'] = f1t2.YEAR
                temp['points12'] = f1t2.PTS
                temp['grade12'] = f1t2.GRADE
                temp['position12'] = f1t2.POS
                #Term III
                temp['class13'] = f1t3.CLASS
                temp['year13'] = f1t3.YEAR
                temp['points13'] = f1t3.PTS
                temp['grade13'] = f1t3.GRADE
                temp['position13'] = f1t3.POS
                #temp.to_csv('me.csv',index=False)
                students_data2 = self.choose_class_combo.currentText() + " " + self.choose_term_combo.currentText() +" " + self.choose_year_combo.currentText() + " report2"            
                temp.to_sql(students_data2,conn,if_exists='replace',index=False)
                students_data = pd.read_sql("SELECT * FROM '" + str(students_data2) + "'", conn)
                
                temp = tempfile.NamedTemporaryFile(delete=True)
                students_data.to_csv(temp.name + '.csv',index=False)
                temp.flush()
                temp.seek(0)
                temp = csv.reader(open(temp.name + '.csv','r'))
                c = canvas.Canvas(self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                for row in ([x for x in temp][1:]):
                    STREAM = row[0]
                    ADM = row[1]
                    NAME = row[2]
                    KCPE = row[3]
                    ENG = row[4]
                    KIS = row[5]
                    MAT = row[6]
                    BIO = row[7]
                    PHY = row[8]
                    CHE = row[9]
                    HIS = row[10]
                    GEO = row[11]
                    CRE = row[12]
                    AGR = row[13]
                    HSC = row[14]
                    BST = row[15]
                    PTS = row[28]
                    GRADE = row[29]
                    ENTRY = row[30]
                    TOTAL = row[31]
                    POS = row[32]
                    VAP = row[33]
                    TOT = row[46]
                    ###########
                    ENGg = row[34]
                    KISg = row[35]
                    MATg = row[36]
                    BIOg = row[37]
                    PHYg = row[38]
                    CHEg = row[39]
                    HISg = row[40]
                    GEOg = row[41]
                    CREg = row[42]
                    AGRg = row[43]
                    HSCg = row[44]
                    BSTg = row[45]
                    ##########
                    ENGp = row[16]
                    KISp = row[17]
                    MATp = row[24]
                    BIOp = row[27]
                    PHYp = row[26]
                    CHEp = row[25]
                    HISp = row[18]
                    GEOp = row[20]
                    CREp = row[21]
                    AGRp = row[22]
                    HSCp = row[19]
                    BSTp = row[23]
                    ############
                    ENGr = row[47]
                    KISr = row[48]
                    MATr = row[49]
                    BIOr = row[50]
                    PHYr = row[51]
                    CHEr = row[52]
                    HISr = row[53]
                    GEOr = row[54]
                    CREr = row[55]
                    AGRr = row[56]
                    HSCr = row[57]
                    BSTr = row[58]
                    ###############
                    ENGre = row[59]
                    KISre = row[60]
                    MATre = row[61]
                    BIOre = row[62]
                    PHYre = row[63]
                    CHEre = row[64]
                    HISre = row[65]
                    GEOre = row[66]
                    CREre = row[67]
                    AGRre = row[68]
                    HSCre = row[69]
                    BSTre = row[70]
                    CLASS = row[71]
                    TERM = row[72]
                    YEAR = row[73]
                    ######f1t1
                    class11 = row[74]
                    year11 = row[75]
                    points11 = row[76]
                    grade11 = row[77]
                    position11 = row[78]
                    ######f1t2
                    class12 = row[79]
                    year12 = row[80]
                    points12 = row[81]
                    grade12 = row[82]
                    position12 = row[83]
                    ######f1t3
                    class13 = row[84]
                    year13 = row[85]
                    points13 = row[86]
                    grade13 = row[87]
                    position13 = row[88]
                    # Start using ReportLab to generate the pdfs 
                    c.drawImage("GULIK LOGO.png", 60, 650)
                    c.drawImage("GULIK LOGO.png", 400, 650)
                    c.drawString(205, 740, "FR GULIK URADI GIRLS SCHOOL")
                    c.drawString(235, 720, "P.O BOX 40-40608")
                    c.drawString(225, 700, "Phone: +254 708 836132")
                    c.drawString(190, 610, CLASS +' ' + TERM + ' ' + YEAR + ' REPORT FORM')
                    c.line(40,640, 550,640)
                    ######MARGIN LINES#3##
                    c.line(40,800, 550,800)
                    c.line(40,800, 40,10)
                    c.line(550,800, 550,10)
                    c.line(40,10, 550,10)#lowest line
                    #SUBJECT SEPARATOR LINES#
                    c.line(145,475, 450,475)
                    c.line(145,455, 450,455)
                    c.line(145,435, 450,435)
                    c.line(145,415, 450,415)
                    c.line(145,395, 450,395)
                    c.line(145,375, 450,375)
                    c.line(145,355, 450,355)
                    c.line(145,335, 450,335)
                    c.line(145,315, 450,315)
                    c.line(145,295, 450,295)
                    c.line(145,275, 450,275)
                    c.line(60,250, 510,250)

                    c.line(60,600, 510,600)
                    c.drawString(120, 580, "STUDENT NAME: " + NAME + '.  ' + '  ADM NO: ' + ADM)
                    c.line(160,570, 380,570)#########Between name and stream
                    c.drawString(160, 550, "STREAM: " + STREAM + "." + '    KCPE MARKS:  ' + '  ' + KCPE)
                    c.line(60,530, 510,530)
                    c.line(160,530, 160,250)########Table dividers
                    c.line(230,530, 230,250)
                    c.line(300,530, 300,250)
                    c.line(370,530, 370,250)
                    c.line(440,530, 440,250)
                    c.line(60,500, 510,500) 
                    c.drawString(60, 510, "SUBJECT")
                    c.drawString(170, 510, "SCORE")
                    c.drawString(240, 510, "GRADE")
                    c.drawString(310, 510, "POINTS")
                    c.drawString(380, 510, "RANK")
                    c.drawString(450, 510, "REMARKS")
                    c.drawString(60, 480, "ENGLISH")
                    c.drawString(60, 460, "KISWAHILI")
                    c.drawString(60, 440, "MATHS")
                    c.drawString(60, 420, "BIOLOGY")
                    c.drawString(60, 400, "PHYSICS")
                    c.drawString(60, 380, "CHEMISTRY")
                    c.drawString(60, 360, "HISTORY")
                    c.drawString(60, 340, "GEOGRAPHY")
                    c.drawString(60, 320, "CRE")
                    c.drawString(60, 300, "AGRICULTURE")
                    c.drawString(60, 280, "H/SCIENCE")
                    c.drawString(60, 260, 'B/STUDIES')
                    c.drawString(190, 480,ENG)
                    c.drawString(190, 460,KIS)
                    c.drawString(190, 440,MAT)
                    c.drawString(190, 420,BIO)
                    c.drawString(190, 400,PHY)
                    c.drawString(190, 380,CHE)
                    c.drawString(190, 360,HIS)
                    c.drawString(190, 340,GEO)
                    c.drawString(190, 320,CRE)
                    c.drawString(190, 300,AGR)
                    c.drawString(190, 280,HSC)
                    c.drawString(190, 260,BST)
                    ######GRADES#############
                    c.drawString(260, 480,ENGg)
                    c.drawString(260, 460,KISg)
                    c.drawString(260, 440,MATg)
                    c.drawString(260, 420,BIOg)
                    c.drawString(260, 400,PHYg)
                    c.drawString(260, 380,CHEg)
                    c.drawString(260, 360,HISg)
                    c.drawString(260, 340,GEOg)
                    c.drawString(260, 320,CREg)
                    c.drawString(260, 300,AGRg)
                    c.drawString(260, 280,HSCg)
                    c.drawString(260, 260,BSTg)
                    ###POINTS################
                    c.drawString(330, 480,ENGp)
                    c.drawString(330, 460,KISp)
                    c.drawString(330, 440,MATp)
                    c.drawString(330, 420,BIOp)
                    c.drawString(330, 400,PHYp)
                    c.drawString(330, 380,CHEp)
                    c.drawString(330, 360,HISp)
                    c.drawString(330, 340,GEOp)
                    c.drawString(330, 320,CREp)
                    c.drawString(330, 300,AGRp)
                    c.drawString(330, 280,HSCp)
                    c.drawString(330, 260,BSTp)
                    ###RANK################
                    c.drawString(400, 480,ENGr)
                    c.drawString(400, 460,KISr)
                    c.drawString(400, 440,MATr)
                    c.drawString(400, 420,BIOr)
                    c.drawString(400, 400,PHYr)
                    c.drawString(400, 380,CHEr)
                    c.drawString(400, 360,HISr)
                    c.drawString(400, 340,GEOr)
                    c.drawString(400, 320,CREr)
                    c.drawString(400, 300,AGRr)
                    c.drawString(400, 280,HSCr)
                    c.drawString(400, 260,BSTr)
                    ###REMARKS###############
                    c.drawString(450, 480,ENGre)
                    c.drawString(450, 460,KISre)
                    c.drawString(450, 440,MATre)
                    c.drawString(450, 420,BIOre)
                    c.drawString(450, 400,PHYre)
                    c.drawString(450, 380,CHEre)
                    c.drawString(450, 360,HISre)
                    c.drawString(450, 340,GEOre)
                    c.drawString(450, 320,CREre)
                    c.drawString(450, 300,AGRre)
                    c.drawString(450, 280,HSCre)
                    c.drawString(450, 260,BSTre)

                    c.drawString(130, 230, "Subject Entries: " + ENTRY + '.'+' Total Marks: '+ TOTAL + '.' + '  Total Points '+ '  ' + PTS )
                    c.line(130,220, 410,220) 
                    c.drawString(120, 200,'Grade: '+ GRADE + '     ' "Class Position:  " + POS +'  out of   ' + TOT)
                    c.drawString(370, 200,'VAP:  ' + VAP)
                    c.line(130,192, 410,192)
                    c.drawString(120, 175,'        PERFOMANCE TREND(FORM I - FORM IV')
                    #HORIZONTAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 510,170)
                    c.drawString(70, 155,'CLASS/YEAR')
                    c.drawString(155, 155,'FORM I ' + year11)
                    c.line(60,150, 510,150)
                    c.drawString(70, 135,'TERM                 I        II     III')
                    #c.drawString(155, 135,term11)
                    c.line(60,130, 510,130)
                    c.drawString(70, 115,'POSITION')
                    c.drawString(155, 115,position11)
                    c.drawString(185, 115,position12)
                    c.drawString(215, 115,position13)
                    c.line(60,110, 510,110)
                    c.drawString(70, 95,'POINTS')
                    c.drawString(155, 95,points11)
                    c.drawString(185, 95,points12)
                    c.drawString(215, 95,points13)
                    c.line(60,90, 510,90)
                    c.drawString(70, 75,'GRADE')
                    c.drawString(155, 75,grade11)
                    c.drawString(185, 75,grade12)
                    c.drawString(215, 75,grade13)
                    c.line(60,70, 510,70)
                    #VERTICAL LINES FOR PERFOMANCE TREND TABLE
                    c.line(60,170, 60,70)
                    c.line(150,170, 150,70)
                    c.line(180,150, 180,70)
                    c.line(210,150, 210,70)
                    c.line(240,170, 240,70)
                    c.line(270,150, 270,70)
                    c.line(300,150, 300,70)
                    c.line(330,170, 330,70)
                    c.line(360,150, 360,70)
                    c.line(390,150, 390,70)
                    c.line(420,170, 420,70)
                    c.line(450,150, 450,70)
                    c.line(480,150, 480,70)
                    c.line(510,170, 510,70)
                    c.drawString(60,35, "This term's fee_________Paid__________Balance_________Next Term_________")
                    c.showPage()
                c.save()  
                #PROMPTING THE USER TO SAVE THE REPORT FORMS########################
                saving_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "REPORT FORMS.pdf")
                existing_file = (self.choose_class_combo.currentText() +' '+self.choose_term_combo.currentText() +' '+ self.choose_year_combo.currentText() +' '+ "RF.pdf")
                name_and_extension = QFileDialog.getSaveFileName(MainWindow, "Save Report Cards",os.path.expanduser("~/Documents"),"Save pdf(*.pdf);;excel(*.xlsx)")#;;Save excel(*.xlsx))")
                if name_and_extension:
                    try:
                        with open(name_and_extension[0],'w') as user_prefer:
                            user_prefer.writelines(open(existing_file))
                    except IOError:
                        pass
                QMessageBox.information(MainWindow,'Successful','Report forms successfully generated and saved in the location you selected.')
            else:
                pass
            conn.commit()
            conn.close()
        except:
            QMessageBox.information(MainWindow,'Failed', 'Process not successful. Please check your data, entries and retry')
    def generate_graphs(self):
        objects = ('EAGLE', 'HAWK', 'TOTAL')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2,1]
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Usage')
        plt.title('Programming language usage')
        plt.show()
    def fetch_teacher_data(self):
        try:
            conn= sqlite3.connect("mydb.db")
            querry = "SELECT * FROM teacher_data"
            result = conn.execute(querry)
            self.teachers_table.setRowCount(0)
            for row,row_data in enumerate(result):
                self.teachers_table.insertRow(row)
                for column,data in enumerate(row_data):
                    self.teachers_table.setItem(row,column,QtWidgets.QTableWidgetItem(str(data)))
            conn.commit()
            conn.close()
        except:
            pass
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
