# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 823)
        self.actionCopyright = QAction(MainWindow)
        self.actionCopyright.setObjectName(u"actionCopyright")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 20, 861, 741))
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.layoutWidget = QWidget(self.tabWidgetPage1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 90, 685, 221))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_video = QPushButton(self.layoutWidget)
        self.pushButton_video.setObjectName(u"pushButton_video")
        self.pushButton_video.setCheckable(False)
        self.pushButton_video.setChecked(False)

        self.horizontalLayout_2.addWidget(self.pushButton_video)

        self.label_videopath = QLabel(self.layoutWidget)
        self.label_videopath.setObjectName(u"label_videopath")
        self.label_videopath.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_2.addWidget(self.label_videopath)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_extract_method = QComboBox(self.layoutWidget)
        self.comboBox_extract_method.addItem("")
        self.comboBox_extract_method.addItem("")
        self.comboBox_extract_method.addItem("")
        self.comboBox_extract_method.setObjectName(u"comboBox_extract_method")

        self.horizontalLayout_4.addWidget(self.comboBox_extract_method)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEdit_length = QLineEdit(self.layoutWidget)
        self.lineEdit_length.setObjectName(u"lineEdit_length")
        self.lineEdit_length.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_length)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_width = QLineEdit(self.layoutWidget)
        self.lineEdit_width.setObjectName(u"lineEdit_width")
        self.lineEdit_width.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_width)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.spinBox_quality = QSpinBox(self.layoutWidget)
        self.spinBox_quality.setObjectName(u"spinBox_quality")
        self.spinBox_quality.setMaximum(100)
        self.spinBox_quality.setValue(100)

        self.horizontalLayout_5.addWidget(self.spinBox_quality)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.pushButton_extract = QPushButton(self.layoutWidget)
        self.pushButton_extract.setObjectName(u"pushButton_extract")

        self.horizontalLayout_5.addWidget(self.pushButton_extract)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.label_5 = QLabel(self.tabWidgetPage2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 660, 51, 21))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShape(QFrame.Panel)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.pushButton_rotate_shun = QPushButton(self.tabWidgetPage2)
        self.pushButton_rotate_shun.setObjectName(u"pushButton_rotate_shun")
        self.pushButton_rotate_shun.setGeometry(QRect(460, 50, 91, 24))
        self.pushButton_rotate_shun.setAutoRepeat(True)
        self.lcdNumber = QLCDNumber(self.tabWidgetPage2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(380, 50, 64, 23))
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setStyleSheet(u"")
        self.lcdNumber.setFrameShape(QFrame.Box)
        self.lcdNumber.setFrameShadow(QFrame.Plain)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)
        self.spinBox_rightdown_y = QSpinBox(self.tabWidgetPage2)
        self.spinBox_rightdown_y.setObjectName(u"spinBox_rightdown_y")
        self.spinBox_rightdown_y.setEnabled(False)
        self.spinBox_rightdown_y.setGeometry(QRect(760, 580, 71, 22))
        self.spinBox_rightdown_y.setMaximum(9999)
        self.spinBox_rightdown_x = QSpinBox(self.tabWidgetPage2)
        self.spinBox_rightdown_x.setObjectName(u"spinBox_rightdown_x")
        self.spinBox_rightdown_x.setEnabled(False)
        self.spinBox_rightdown_x.setGeometry(QRect(680, 580, 61, 22))
        self.spinBox_rightdown_x.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_rightdown_x.setAccelerated(True)
        self.spinBox_rightdown_x.setMaximum(9999)
        self.spinBox_leftup_x = QSpinBox(self.tabWidgetPage2)
        self.spinBox_leftup_x.setObjectName(u"spinBox_leftup_x")
        self.spinBox_leftup_x.setEnabled(False)
        self.spinBox_leftup_x.setGeometry(QRect(20, 140, 61, 22))
        self.spinBox_leftup_x.setMaximum(9999)
        self.layoutWidget1 = QWidget(self.tabWidgetPage2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 10, 700, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_choose = QPushButton(self.layoutWidget1)
        self.pushButton_choose.setObjectName(u"pushButton_choose")

        self.horizontalLayout.addWidget(self.pushButton_choose)

        self.label_path = QLabel(self.layoutWidget1)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setMinimumSize(QSize(600, 0))

        self.horizontalLayout.addWidget(self.label_path)

        self.label_adjustpara = QLabel(self.tabWidgetPage2)
        self.label_adjustpara.setObjectName(u"label_adjustpara")
        self.label_adjustpara.setGeometry(QRect(280, 660, 53, 16))
        self.pushButton_crop = QPushButton(self.tabWidgetPage2)
        self.pushButton_crop.setObjectName(u"pushButton_crop")
        self.pushButton_crop.setGeometry(QRect(610, 660, 101, 24))
        self.pushButton_refresh = QPushButton(self.tabWidgetPage2)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setGeometry(QRect(690, 460, 75, 24))
        self.label = QLabel(self.tabWidgetPage2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 53, 16))
        self.horizontalSlider = QSlider(self.tabWidgetPage2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QRect(340, 660, 160, 22))
        self.horizontalSlider.setMouseTracking(True)
        self.horizontalSlider.setValue(20)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)
        self.pushButton_preview = QPushButton(self.tabWidgetPage2)
        self.pushButton_preview.setObjectName(u"pushButton_preview")
        self.pushButton_preview.setGeometry(QRect(520, 90, 75, 24))
        self.checkBox = QCheckBox(self.tabWidgetPage2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(180, 90, 141, 20))
        self.label_4 = QLabel(self.tabWidgetPage2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(760, 560, 53, 16))
        self.layoutWidget2 = QWidget(self.tabWidgetPage2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(340, 90, 182, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.spinBox_No = QSpinBox(self.layoutWidget2)
        self.spinBox_No.setObjectName(u"spinBox_No")
        self.spinBox_No.setMinimumSize(QSize(40, 0))
        self.spinBox_No.setMinimum(1)
        self.spinBox_No.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.spinBox_No)

        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_rightdowny = QLabel(self.tabWidgetPage2)
        self.label_rightdowny.setObjectName(u"label_rightdowny")
        self.label_rightdowny.setGeometry(QRect(760, 610, 53, 16))
        self.label_rightdowny.setFrameShape(QFrame.Panel)
        self.label_rightdowny.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.tabWidgetPage2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 120, 53, 16))
        self.pushButton_rotate_ni = QPushButton(self.tabWidgetPage2)
        self.pushButton_rotate_ni.setObjectName(u"pushButton_rotate_ni")
        self.pushButton_rotate_ni.setGeometry(QRect(270, 50, 91, 24))
        self.pushButton_rotate_ni.setCheckable(False)
        self.pushButton_rotate_ni.setAutoRepeat(True)
        self.label_leftupx = QLabel(self.tabWidgetPage2)
        self.label_leftupx.setObjectName(u"label_leftupx")
        self.label_leftupx.setGeometry(QRect(20, 180, 53, 16))
        self.label_leftupx.setFrameShape(QFrame.Panel)
        self.label_leftupx.setFrameShadow(QFrame.Sunken)
        self.comboBox = QComboBox(self.tabWidgetPage2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 660, 111, 22))
        self.spinBox_leftup_y = QSpinBox(self.tabWidgetPage2)
        self.spinBox_leftup_y.setObjectName(u"spinBox_leftup_y")
        self.spinBox_leftup_y.setEnabled(False)
        self.spinBox_leftup_y.setGeometry(QRect(90, 140, 61, 22))
        self.spinBox_leftup_y.setMaximum(9999)
        self.MplWidget = MplWidget(self.tabWidgetPage2)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setGeometry(QRect(160, 120, 500, 500))
        self.label_3 = QLabel(self.tabWidgetPage2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 560, 53, 16))
        self.label_leftupy = QLabel(self.tabWidgetPage2)
        self.label_leftupy.setObjectName(u"label_leftupy")
        self.label_leftupy.setGeometry(QRect(90, 180, 53, 16))
        self.label_leftupy.setFrameShape(QFrame.Panel)
        self.label_leftupy.setFrameShadow(QFrame.Sunken)
        self.label_rightdownx = QLabel(self.tabWidgetPage2)
        self.label_rightdownx.setObjectName(u"label_rightdownx")
        self.label_rightdownx.setGeometry(QRect(680, 610, 53, 16))
        self.label_rightdownx.setFrameShape(QFrame.Panel)
        self.label_rightdownx.setFrameShadow(QFrame.Sunken)
        self.pushButton_reset = QPushButton(self.tabWidgetPage2)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setGeometry(QRect(730, 660, 75, 24))
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.label_gif_display = QLabel(self.tabWidgetPage3)
        self.label_gif_display.setObjectName(u"label_gif_display")
        self.label_gif_display.setGeometry(QRect(60, 100, 600, 600))
        self.label_gif_display.setFrameShape(QFrame.Box)
        self.label_gif_display.setFrameShadow(QFrame.Sunken)
        self.label_gif_display.setMidLineWidth(0)
        self.label_gif_display.setAlignment(Qt.AlignCenter)
        self.pushButton_gif_save = QPushButton(self.tabWidgetPage3)
        self.pushButton_gif_save.setObjectName(u"pushButton_gif_save")
        self.pushButton_gif_save.setGeometry(QRect(730, 600, 75, 24))
        self.layoutWidget3 = QWidget(self.tabWidgetPage3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(170, 60, 341, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.spinBox_gif_time = QSpinBox(self.layoutWidget3)
        self.spinBox_gif_time.setObjectName(u"spinBox_gif_time")
        self.spinBox_gif_time.setKeyboardTracking(False)
        self.spinBox_gif_time.setMinimum(0)
        self.spinBox_gif_time.setMaximum(5000)
        self.spinBox_gif_time.setSingleStep(50)
        self.spinBox_gif_time.setValue(1000)

        self.horizontalLayout_6.addWidget(self.spinBox_gif_time)

        self.layoutWidget4 = QWidget(self.tabWidgetPage3)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(60, 20, 721, 26))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_gif_home = QPushButton(self.layoutWidget4)
        self.pushButton_gif_home.setObjectName(u"pushButton_gif_home")
        self.pushButton_gif_home.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_gif_home)

        self.label_GIFhome = QLabel(self.layoutWidget4)
        self.label_GIFhome.setObjectName(u"label_GIFhome")

        self.horizontalLayout_7.addWidget(self.label_GIFhome)

        self.tabWidget.addTab(self.tabWidgetPage3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 936, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton_choose, self.spinBox_leftup_x)
        QWidget.setTabOrder(self.spinBox_leftup_x, self.spinBox_leftup_y)
        QWidget.setTabOrder(self.spinBox_leftup_y, self.spinBox_rightdown_x)
        QWidget.setTabOrder(self.spinBox_rightdown_x, self.spinBox_rightdown_y)
        QWidget.setTabOrder(self.spinBox_rightdown_y, self.pushButton_crop)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionCopyright)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VideoFC", None))
        self.actionCopyright.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.actionCopyright.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>www.asgeologeekfan.top</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_video.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.label_videopath.setText("")
        self.comboBox_extract_method.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u8d77\u6b62\u65f6\u523b", None))
        self.comboBox_extract_method.setItemText(1, QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u7279\u5b9a\u79d2", None))
        self.comboBox_extract_method.setItemText(2, QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u7279\u5b9a\u5e27", None))

        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8d77\u6b62\u79d2\u6570\u548c\u95f4\u9694\u79d2\u6570\uff08\u7a7a\u683c\u5206\u9694\uff09  \u4f8b\u5982\uff1a4 20 2\u8868\u793a\u4ece\u7b2c4\u79d2\u5f00\u59cb\uff0c\u7b2c20\u79d2\u622a\u6b62\uff0c\u6bcf\u96942\u79d2\u63d0\u53d6\u4e00\u5f20", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5c3a\u5bf8", None))
        self.lineEdit_length.setInputMask("")
        self.lineEdit_length.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u957f\u8fb9\u50cf\u7d20", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.lineEdit_width.setInputMask("")
        self.lineEdit_width.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u77ed\u8fb9\u50cf\u7d20", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8d28\u91cf", None))
        self.pushButton_extract.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u89c6\u9891", None))
        self.label_5.setText("")
        self.pushButton_rotate_shun.setText(QCoreApplication.translate("MainWindow", u"\u987a\u65f6\u9488\u65cb\u8f6c1\u00b0", None))
        self.pushButton_choose.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.label_path.setText("")
        self.label_adjustpara.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6", None))
        self.pushButton_crop.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5904\u7406\u5e76\u4fdd\u5b58", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u88c1\u526a\u6846", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u4e0aX", None))
        self.pushButton_preview.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9884\u89c8\u56fe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u8f93\u5165\u88c1\u526a\u6846\u5750\u6807", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u4e0bY", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5728\u9884\u89c8    \u7b2c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5f20", None))
        self.label_rightdowny.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u4e0aY", None))
        self.pushButton_rotate_ni.setText(QCoreApplication.translate("MainWindow", u"\u9006\u65f6\u9488\u65cb\u8f6c1\u00b0", None))
        self.label_leftupx.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u5f69\u56fe", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u5904\u7406", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e8c\u503c\u5316\u5904\u7406", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u53cd\u76f8\u5904\u7406", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u4e0bX", None))
        self.label_leftupy.setText("")
        self.label_rightdownx.setText("")
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u5904\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5904\u7406\u56fe\u50cf", None))
        self.label_gif_display.setText(QCoreApplication.translate("MainWindow", u"GIF\u9884\u89c8\u533a", None))
        self.pushButton_gif_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58GIF", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u663e\u793a\u65f6\u95f4\uff081\u8868\u793a1/1000\u79d2\uff0c1000\u8868\u793a1\u79d2\uff09", None))
        self.spinBox_gif_time.setSpecialValueText("")
        self.spinBox_gif_time.setSuffix("")
        self.pushButton_gif_home.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9GIF\u7d20\u6750\u6587\u4ef6\u5939", None))
        self.label_GIFhome.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), QCoreApplication.translate("MainWindow", u"\u751f\u6210GIF", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

