# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '//Art-1405260002/d/assets/scripts/maya_scripts/ui/qt_main_ui.ui'
#
# Created: Fri Dec 18 09:41:03 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(471, 800)
        main_window.setMinimumSize(QtCore.QSize(0, 0))
        main_window.setMaximumSize(QtCore.QSize(620, 800))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        main_window.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(main_window)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inprogress_button = QtGui.QPushButton(main_window)
        self.inprogress_button.setMaximumSize(QtCore.QSize(24, 24))
        self.inprogress_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/play_off_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/play_on_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.inprogress_button.setIcon(icon)
        self.inprogress_button.setCheckable(True)
        self.inprogress_button.setChecked(True)
        self.inprogress_button.setFlat(True)
        self.inprogress_button.setObjectName("inprogress_button")
        self.horizontalLayout.addWidget(self.inprogress_button)
        self.ready_button = QtGui.QPushButton(main_window)
        self.ready_button.setMaximumSize(QtCore.QSize(24, 24))
        self.ready_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/pause_off_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/pause_on_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ready_button.setIcon(icon1)
        self.ready_button.setCheckable(True)
        self.ready_button.setChecked(False)
        self.ready_button.setFlat(True)
        self.ready_button.setObjectName("ready_button")
        self.horizontalLayout.addWidget(self.ready_button)
        self.complete_button = QtGui.QPushButton(main_window)
        self.complete_button.setMaximumSize(QtCore.QSize(24, 24))
        self.complete_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/check_off_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/check_on_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.complete_button.setIcon(icon2)
        self.complete_button.setCheckable(True)
        self.complete_button.setChecked(False)
        self.complete_button.setFlat(True)
        self.complete_button.setObjectName("complete_button")
        self.horizontalLayout.addWidget(self.complete_button)
        self.line_2 = QtGui.QFrame(main_window)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.update_cache = QtGui.QPushButton(main_window)
        self.update_cache.setMinimumSize(QtCore.QSize(0, 0))
        self.update_cache.setMaximumSize(QtCore.QSize(70, 16777215))
        self.update_cache.setObjectName("update_cache")
        self.horizontalLayout.addWidget(self.update_cache)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setSpacing(3)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.tabLayout = QtGui.QHBoxLayout()
        self.tabLayout.setSpacing(3)
        self.tabLayout.setObjectName("tabLayout")
        self.tabProjectWidget = QtGui.QTabWidget(main_window)
        self.tabProjectWidget.setObjectName("tabProjectWidget")
        self.tabProject = QtGui.QWidget()
        self.tabProject.setMinimumSize(QtCore.QSize(0, 0))
        self.tabProject.setObjectName("tabProject")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabProject)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.project_label = QtGui.QLabel(self.tabProject)
        self.project_label.setAlignment(QtCore.Qt.AlignCenter)
        self.project_label.setObjectName("project_label")
        self.verticalLayout_4.addWidget(self.project_label)
        self.project_list = QtGui.QListWidget(self.tabProject)
        self.project_list.setMinimumSize(QtCore.QSize(0, 150))
        self.project_list.setObjectName("project_list")
        self.verticalLayout_4.addWidget(self.project_list)
        self.project_info = QtGui.QTableWidget(self.tabProject)
        self.project_info.setMinimumSize(QtCore.QSize(190, 91))
        self.project_info.setMaximumSize(QtCore.QSize(16777215, 91))
        self.project_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.project_info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.project_info.setAutoScroll(False)
        self.project_info.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.project_info.setObjectName("project_info")
        self.project_info.setColumnCount(1)
        self.project_info.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.project_info.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.project_info.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.project_info.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.project_info.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.project_info.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.project_info.setHorizontalHeaderItem(0, item)
        self.project_info.horizontalHeader().setVisible(False)
        self.project_info.horizontalHeader().setCascadingSectionResizes(True)
        self.project_info.horizontalHeader().setDefaultSectionSize(150)
        self.project_info.horizontalHeader().setMinimumSectionSize(150)
        self.project_info.horizontalHeader().setStretchLastSection(True)
        self.project_info.verticalHeader().setDefaultSectionSize(18)
        self.verticalLayout_4.addWidget(self.project_info)
        self.tabProjectWidget.addTab(self.tabProject, "")
        self.tabLayout.addWidget(self.tabProjectWidget)
        self.tabProductionType = QtGui.QTabWidget(main_window)
        self.tabProductionType.setMinimumSize(QtCore.QSize(250, 0))
        self.tabProductionType.setMaximumSize(QtCore.QSize(350, 16777215))
        self.tabProductionType.setObjectName("tabProductionType")
        self.assets_tab = QtGui.QWidget()
        self.assets_tab.setObjectName("assets_tab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.assets_tab)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.asset_label = QtGui.QLabel(self.assets_tab)
        self.asset_label.setAlignment(QtCore.Qt.AlignCenter)
        self.asset_label.setObjectName("asset_label")
        self.verticalLayout_5.addWidget(self.asset_label)
        self.asset_layout = QtGui.QHBoxLayout()
        self.asset_layout.setSpacing(3)
        self.asset_layout.setObjectName("asset_layout")
        self.asset_list = QtGui.QListWidget(self.assets_tab)
        self.asset_list.setObjectName("asset_list")
        self.asset_layout.addWidget(self.asset_list)
        self.asset_process_list = QtGui.QListWidget(self.assets_tab)
        self.asset_process_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.asset_process_list.setObjectName("asset_process_list")
        self.asset_layout.addWidget(self.asset_process_list)
        self.verticalLayout_5.addLayout(self.asset_layout)
        self.asset_info = QtGui.QTableWidget(self.assets_tab)
        self.asset_info.setMinimumSize(QtCore.QSize(190, 91))
        self.asset_info.setMaximumSize(QtCore.QSize(16777215, 91))
        self.asset_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.asset_info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.asset_info.setAutoScroll(False)
        self.asset_info.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.asset_info.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.asset_info.setObjectName("asset_info")
        self.asset_info.setColumnCount(1)
        self.asset_info.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.asset_info.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.asset_info.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.asset_info.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.asset_info.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.asset_info.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.asset_info.setHorizontalHeaderItem(0, item)
        self.asset_info.horizontalHeader().setVisible(False)
        self.asset_info.horizontalHeader().setCascadingSectionResizes(True)
        self.asset_info.horizontalHeader().setDefaultSectionSize(150)
        self.asset_info.horizontalHeader().setMinimumSectionSize(150)
        self.asset_info.horizontalHeader().setStretchLastSection(True)
        self.asset_info.verticalHeader().setDefaultSectionSize(18)
        self.verticalLayout_5.addWidget(self.asset_info)
        self.tabProductionType.addTab(self.assets_tab, "")
        self.shots_tab = QtGui.QWidget()
        self.shots_tab.setObjectName("shots_tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.shots_tab)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.shot_label = QtGui.QLabel(self.shots_tab)
        self.shot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shot_label.setObjectName("shot_label")
        self.verticalLayout_3.addWidget(self.shot_label)
        self.shot_layout = QtGui.QHBoxLayout()
        self.shot_layout.setSpacing(3)
        self.shot_layout.setObjectName("shot_layout")
        self.shot_list = QtGui.QListWidget(self.shots_tab)
        self.shot_list.setObjectName("shot_list")
        self.shot_layout.addWidget(self.shot_list)
        self.shot_process_list = QtGui.QListWidget(self.shots_tab)
        self.shot_process_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.shot_process_list.setObjectName("shot_process_list")
        self.shot_layout.addWidget(self.shot_process_list)
        self.verticalLayout_3.addLayout(self.shot_layout)
        self.shot_info = QtGui.QTableWidget(self.shots_tab)
        self.shot_info.setMinimumSize(QtCore.QSize(190, 91))
        self.shot_info.setMaximumSize(QtCore.QSize(16777215, 91))
        self.shot_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shot_info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shot_info.setAutoScroll(False)
        self.shot_info.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.shot_info.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.shot_info.setObjectName("shot_info")
        self.shot_info.setColumnCount(1)
        self.shot_info.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.shot_info.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.shot_info.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.shot_info.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.shot_info.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.shot_info.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.shot_info.setHorizontalHeaderItem(0, item)
        self.shot_info.horizontalHeader().setVisible(False)
        self.shot_info.horizontalHeader().setCascadingSectionResizes(True)
        self.shot_info.horizontalHeader().setDefaultSectionSize(150)
        self.shot_info.horizontalHeader().setMinimumSectionSize(150)
        self.shot_info.horizontalHeader().setStretchLastSection(True)
        self.shot_info.verticalHeader().setDefaultSectionSize(18)
        self.verticalLayout_3.addWidget(self.shot_info)
        self.tabProductionType.addTab(self.shots_tab, "")
        self.tabLayout.addWidget(self.tabProductionType)
        self.mainLayout.addLayout(self.tabLayout)
        self.file_path_layout = QtGui.QVBoxLayout()
        self.file_path_layout.setSpacing(3)
        self.file_path_layout.setObjectName("file_path_layout")
        self.login_layout = QtGui.QHBoxLayout()
        self.login_layout.setSpacing(3)
        self.login_layout.setObjectName("login_layout")
        self.login_label = QtGui.QLabel(main_window)
        self.login_label.setMinimumSize(QtCore.QSize(60, 0))
        self.login_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.login_layout.addWidget(self.login_label)
        self.login_name = QtGui.QLineEdit(main_window)
        self.login_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_name.setAlignment(QtCore.Qt.AlignCenter)
        self.login_name.setObjectName("login_name")
        self.login_layout.addWidget(self.login_name)
        self.logout_button = QtGui.QPushButton(main_window)
        self.logout_button.setMaximumSize(QtCore.QSize(21, 21))
        self.logout_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/sign-out_222222_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_button.setIcon(icon3)
        self.logout_button.setObjectName("logout_button")
        self.login_layout.addWidget(self.logout_button)
        self.file_path_layout.addLayout(self.login_layout)
        self.save_path_layout = QtGui.QHBoxLayout()
        self.save_path_layout.setSpacing(3)
        self.save_path_layout.setObjectName("save_path_layout")
        self.save_path_label = QtGui.QLabel(main_window)
        self.save_path_label.setMinimumSize(QtCore.QSize(60, 0))
        self.save_path_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.save_path_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.save_path_label.setObjectName("save_path_label")
        self.save_path_layout.addWidget(self.save_path_label)
        self.save_path = QtGui.QLineEdit(main_window)
        self.save_path.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.save_path.setAlignment(QtCore.Qt.AlignCenter)
        self.save_path.setObjectName("save_path")
        self.save_path_layout.addWidget(self.save_path)
        self.open_path_button = QtGui.QPushButton(main_window)
        self.open_path_button.setMaximumSize(QtCore.QSize(21, 21))
        self.open_path_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/folder-open-o_222222_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_path_button.setIcon(icon4)
        self.open_path_button.setObjectName("open_path_button")
        self.save_path_layout.addWidget(self.open_path_button)
        self.file_path_layout.addLayout(self.save_path_layout)
        self.save_file_layout = QtGui.QHBoxLayout()
        self.save_file_layout.setSpacing(3)
        self.save_file_layout.setObjectName("save_file_layout")
        self.save_file_label = QtGui.QLabel(main_window)
        self.save_file_label.setMinimumSize(QtCore.QSize(60, 0))
        self.save_file_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.save_file_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.save_file_label.setObjectName("save_file_label")
        self.save_file_layout.addWidget(self.save_file_label)
        self.save_file = QtGui.QLineEdit(main_window)
        self.save_file.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.save_file.setAlignment(QtCore.Qt.AlignCenter)
        self.save_file.setObjectName("save_file")
        self.save_file_layout.addWidget(self.save_file)
        self.save_button = QtGui.QPushButton(main_window)
        self.save_button.setMaximumSize(QtCore.QSize(21, 21))
        self.save_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/save_222222_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon5)
        self.save_button.setObjectName("save_button")
        self.save_file_layout.addWidget(self.save_button)
        self.file_path_layout.addLayout(self.save_file_layout)
        self.mainLayout.addLayout(self.file_path_layout)
        self.file_list_layout = QtGui.QVBoxLayout()
        self.file_list_layout.setSpacing(6)
        self.file_list_layout.setObjectName("file_list_layout")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.file_list_label = QtGui.QLabel(main_window)
        self.file_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_list_label.setObjectName("file_list_label")
        self.verticalLayout_6.addWidget(self.file_list_label)
        self.file_list = QtGui.QListWidget(main_window)
        self.file_list.setMinimumSize(QtCore.QSize(0, 0))
        self.file_list.setMaximumSize(QtCore.QSize(16777215, 150))
        self.file_list.setObjectName("file_list")
        self.verticalLayout_6.addWidget(self.file_list)
        self.open_button = QtGui.QPushButton(main_window)
        self.open_button.setObjectName("open_button")
        self.verticalLayout_6.addWidget(self.open_button)
        self.file_list_layout.addLayout(self.verticalLayout_6)
        self.line = QtGui.QFrame(main_window)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.file_list_layout.addWidget(self.line)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.note_label = QtGui.QLabel(main_window)
        self.note_label.setAlignment(QtCore.Qt.AlignCenter)
        self.note_label.setMargin(-1)
        self.note_label.setObjectName("note_label")
        self.verticalLayout_7.addWidget(self.note_label)
        self.note_list = QtGui.QListWidget(main_window)
        self.note_list.setMinimumSize(QtCore.QSize(0, 0))
        self.note_list.setMaximumSize(QtCore.QSize(16777215, 150))
        self.note_list.setWordWrap(True)
        self.note_list.setObjectName("note_list")
        self.verticalLayout_7.addWidget(self.note_list)
        self.note = QtGui.QLineEdit(main_window)
        self.note.setObjectName("note")
        self.verticalLayout_7.addWidget(self.note)
        self.file_list_layout.addLayout(self.verticalLayout_7)
        self.mainLayout.addLayout(self.file_list_layout)
        self.verticalLayout_2.addLayout(self.mainLayout)

        self.retranslateUi(main_window)
        self.tabProjectWidget.setCurrentIndex(0)
        self.tabProductionType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "MCD TACTIC FileManager v1.1", None, QtGui.QApplication.UnicodeUTF8))
        self.inprogress_button.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">顯示</span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">進行中</span><span style=\" font-size:10pt;\">的專案</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ready_button.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">顯示</span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">準備中</span><span style=\" font-size:10pt;\">的專案</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.complete_button.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">顯示</span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">完成</span><span style=\" font-size:10pt;\">的專案</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.update_cache.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">看不到專案或新加的物件嗎? 請按這裡。</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.update_cache.setText(QtGui.QApplication.translate("main_window", "更新快取", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label.setText(QtGui.QApplication.translate("main_window", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.project_info.verticalHeaderItem(0).setText(QtGui.QApplication.translate("main_window", "專案:", None, QtGui.QApplication.UnicodeUTF8))
        self.project_info.verticalHeaderItem(1).setText(QtGui.QApplication.translate("main_window", "案型:", None, QtGui.QApplication.UnicodeUTF8))
        self.project_info.verticalHeaderItem(2).setText(QtGui.QApplication.translate("main_window", "窗口:", None, QtGui.QApplication.UnicodeUTF8))
        self.project_info.verticalHeaderItem(3).setText(QtGui.QApplication.translate("main_window", "開始:", None, QtGui.QApplication.UnicodeUTF8))
        self.project_info.verticalHeaderItem(4).setText(QtGui.QApplication.translate("main_window", "結束:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProjectWidget.setTabText(self.tabProjectWidget.indexOf(self.tabProject), QtGui.QApplication.translate("main_window", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_label.setText(QtGui.QApplication.translate("main_window", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_info.verticalHeaderItem(0).setText(QtGui.QApplication.translate("main_window", "物件:", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_info.verticalHeaderItem(1).setText(QtGui.QApplication.translate("main_window", "類型:", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_info.verticalHeaderItem(2).setText(QtGui.QApplication.translate("main_window", "分配:", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_info.verticalHeaderItem(3).setText(QtGui.QApplication.translate("main_window", "開始:", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_info.verticalHeaderItem(4).setText(QtGui.QApplication.translate("main_window", "結束:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProductionType.setTabText(self.tabProductionType.indexOf(self.assets_tab), QtGui.QApplication.translate("main_window", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_label.setText(QtGui.QApplication.translate("main_window", "Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_info.setToolTip(QtGui.QApplication.translate("main_window", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_info.verticalHeaderItem(0).setText(QtGui.QApplication.translate("main_window", "物件:", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_info.verticalHeaderItem(1).setText(QtGui.QApplication.translate("main_window", "類型:", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_info.verticalHeaderItem(2).setText(QtGui.QApplication.translate("main_window", "分配:", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_info.verticalHeaderItem(3).setText(QtGui.QApplication.translate("main_window", "開始:", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_info.verticalHeaderItem(4).setText(QtGui.QApplication.translate("main_window", "結束:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProductionType.setTabText(self.tabProductionType.indexOf(self.shots_tab), QtGui.QApplication.translate("main_window", "Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.login_label.setText(QtGui.QApplication.translate("main_window", "作者:", None, QtGui.QApplication.UnicodeUTF8))
        self.logout_button.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">登出</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.save_path_label.setText(QtGui.QApplication.translate("main_window", "存檔路徑:", None, QtGui.QApplication.UnicodeUTF8))
        self.open_path_button.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">打開資料夾</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.save_file_label.setText(QtGui.QApplication.translate("main_window", "存檔名:", None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">存檔</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.file_list_label.setText(QtGui.QApplication.translate("main_window", "檔案", None, QtGui.QApplication.UnicodeUTF8))
        self.open_button.setText(QtGui.QApplication.translate("main_window", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.note_label.setText(QtGui.QApplication.translate("main_window", "檔案備註", None, QtGui.QApplication.UnicodeUTF8))
        self.note_list.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">這裡會列出</span><span style=\" font-size:10pt; font-weight:600;\">選擇</span><span style=\" font-size:10pt;\">的檔案的備註，滑鼠點兩下可以刪除。</span></p><p><span style=\" font-size:10pt;\">用下面的字框來輸入備註，寫完記得按儲存。</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.note.setToolTip(QtGui.QApplication.translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt;\">這邊輸入備註。</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

