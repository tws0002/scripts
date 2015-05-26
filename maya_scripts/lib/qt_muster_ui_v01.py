# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '//Art-1405260002/d/assets/scripts/maya_scripts/ui/qt_muster_submit_v01.ui'
#
# Created: Tue May 26 17:17:46 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MusterConnector(object):
    def setupUi(self, MusterConnector):
        MusterConnector.setObjectName("MusterConnector")
        MusterConnector.resize(400, 760)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MusterConnector.sizePolicy().hasHeightForWidth())
        MusterConnector.setSizePolicy(sizePolicy)
        MusterConnector.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        MusterConnector.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(MusterConnector)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.server_panel_layout = QtGui.QVBoxLayout()
        self.server_panel_layout.setSpacing(0)
        self.server_panel_layout.setObjectName("server_panel_layout")
        self.server_panel_button = QtGui.QPushButton(MusterConnector)
        self.server_panel_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.server_panel_button.setStyleSheet("text-align: left")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/julio/.designer/icons/minus-square-o_000000_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:/Users/julio/.designer/icons/plus-square-o_000000_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.server_panel_button.setIcon(icon)
        self.server_panel_button.setCheckable(False)
        self.server_panel_button.setObjectName("server_panel_button")
        self.server_panel_layout.addWidget(self.server_panel_button)
        self.server_panel = QtGui.QWidget(MusterConnector)
        self.server_panel.setObjectName("server_panel")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.server_panel)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(15, 0, 35, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.muster_ip_layout = QtGui.QHBoxLayout()
        self.muster_ip_layout.setSpacing(15)
        self.muster_ip_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.muster_ip_layout.setContentsMargins(0, 0, 0, 0)
        self.muster_ip_layout.setObjectName("muster_ip_layout")
        self.muster_ip_label = QtGui.QLabel(self.server_panel)
        self.muster_ip_label.setMinimumSize(QtCore.QSize(80, 0))
        self.muster_ip_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.muster_ip_label.setObjectName("muster_ip_label")
        self.muster_ip_layout.addWidget(self.muster_ip_label)
        self.muster_ip = QtGui.QLineEdit(self.server_panel)
        self.muster_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.muster_ip.setObjectName("muster_ip")
        self.muster_ip_layout.addWidget(self.muster_ip)
        self.verticalLayout_2.addLayout(self.muster_ip_layout)
        self.muster_port_layout = QtGui.QHBoxLayout()
        self.muster_port_layout.setSpacing(15)
        self.muster_port_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.muster_port_layout.setObjectName("muster_port_layout")
        self.muster_port_label = QtGui.QLabel(self.server_panel)
        self.muster_port_label.setMinimumSize(QtCore.QSize(80, 0))
        self.muster_port_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.muster_port_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.muster_port_label.setObjectName("muster_port_label")
        self.muster_port_layout.addWidget(self.muster_port_label)
        self.muster_port = QtGui.QLineEdit(self.server_panel)
        self.muster_port.setAlignment(QtCore.Qt.AlignCenter)
        self.muster_port.setObjectName("muster_port")
        self.muster_port_layout.addWidget(self.muster_port)
        self.verticalLayout_2.addLayout(self.muster_port_layout)
        self.priority_layout = QtGui.QHBoxLayout()
        self.priority_layout.setSpacing(15)
        self.priority_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.priority_layout.setObjectName("priority_layout")
        self.priority_label = QtGui.QLabel(self.server_panel)
        self.priority_label.setMinimumSize(QtCore.QSize(80, 0))
        self.priority_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.priority_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.priority_label.setObjectName("priority_label")
        self.priority_layout.addWidget(self.priority_label)
        self.priority = QtGui.QLineEdit(self.server_panel)
        self.priority.setAlignment(QtCore.Qt.AlignCenter)
        self.priority.setObjectName("priority")
        self.priority_layout.addWidget(self.priority)
        self.verticalLayout_2.addLayout(self.priority_layout)
        self.muster_packet_size_layout = QtGui.QHBoxLayout()
        self.muster_packet_size_layout.setSpacing(15)
        self.muster_packet_size_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.muster_packet_size_layout.setObjectName("muster_packet_size_layout")
        self.muster_packet_size_label = QtGui.QLabel(self.server_panel)
        self.muster_packet_size_label.setMinimumSize(QtCore.QSize(80, 0))
        self.muster_packet_size_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.muster_packet_size_label.setObjectName("muster_packet_size_label")
        self.muster_packet_size_layout.addWidget(self.muster_packet_size_label)
        self.packet_size = QtGui.QLineEdit(self.server_panel)
        self.packet_size.setAlignment(QtCore.Qt.AlignCenter)
        self.packet_size.setObjectName("packet_size")
        self.muster_packet_size_layout.addWidget(self.packet_size)
        self.verticalLayout_2.addLayout(self.muster_packet_size_layout)
        self.server_panel_layout.addWidget(self.server_panel)
        self.verticalLayout.addLayout(self.server_panel_layout)
        self.frame_range_layout = QtGui.QVBoxLayout()
        self.frame_range_layout.setSpacing(0)
        self.frame_range_layout.setObjectName("frame_range_layout")
        self.frame_range_panel_button = QtGui.QPushButton(MusterConnector)
        self.frame_range_panel_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_range_panel_button.setStyleSheet("text-align: left")
        self.frame_range_panel_button.setIcon(icon)
        self.frame_range_panel_button.setCheckable(False)
        self.frame_range_panel_button.setObjectName("frame_range_panel_button")
        self.frame_range_layout.addWidget(self.frame_range_panel_button)
        self.frame_range_panel = QtGui.QWidget(MusterConnector)
        self.frame_range_panel.setEnabled(True)
        self.frame_range_panel.setObjectName("frame_range_panel")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_range_panel)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(15, 0, 35, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.start_frame_layout = QtGui.QHBoxLayout()
        self.start_frame_layout.setSpacing(15)
        self.start_frame_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.start_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.start_frame_layout.setObjectName("start_frame_layout")
        self.start_frame_label = QtGui.QLabel(self.frame_range_panel)
        self.start_frame_label.setMinimumSize(QtCore.QSize(80, 0))
        self.start_frame_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_frame_label.setObjectName("start_frame_label")
        self.start_frame_layout.addWidget(self.start_frame_label)
        self.start_frame = QtGui.QLineEdit(self.frame_range_panel)
        self.start_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.start_frame.setObjectName("start_frame")
        self.start_frame_layout.addWidget(self.start_frame)
        self.verticalLayout_3.addLayout(self.start_frame_layout)
        self.end_frame_layout = QtGui.QHBoxLayout()
        self.end_frame_layout.setSpacing(15)
        self.end_frame_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.end_frame_layout.setObjectName("end_frame_layout")
        self.end_frame_label = QtGui.QLabel(self.frame_range_panel)
        self.end_frame_label.setMinimumSize(QtCore.QSize(80, 0))
        self.end_frame_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.end_frame_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.end_frame_label.setObjectName("end_frame_label")
        self.end_frame_layout.addWidget(self.end_frame_label)
        self.end_frame = QtGui.QLineEdit(self.frame_range_panel)
        self.end_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.end_frame.setObjectName("end_frame")
        self.end_frame_layout.addWidget(self.end_frame)
        self.verticalLayout_3.addLayout(self.end_frame_layout)
        self.by_frame_layout = QtGui.QHBoxLayout()
        self.by_frame_layout.setSpacing(15)
        self.by_frame_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.by_frame_layout.setObjectName("by_frame_layout")
        self.by_frame_label = QtGui.QLabel(self.frame_range_panel)
        self.by_frame_label.setMinimumSize(QtCore.QSize(80, 0))
        self.by_frame_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.by_frame_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.by_frame_label.setObjectName("by_frame_label")
        self.by_frame_layout.addWidget(self.by_frame_label)
        self.by_frame = QtGui.QLineEdit(self.frame_range_panel)
        self.by_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.by_frame.setObjectName("by_frame")
        self.by_frame_layout.addWidget(self.by_frame)
        self.verticalLayout_3.addLayout(self.by_frame_layout)
        self.frame_padding_layout = QtGui.QHBoxLayout()
        self.frame_padding_layout.setSpacing(15)
        self.frame_padding_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.frame_padding_layout.setObjectName("frame_padding_layout")
        self.frame_padding_label = QtGui.QLabel(self.frame_range_panel)
        self.frame_padding_label.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_padding_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.frame_padding_label.setObjectName("frame_padding_label")
        self.frame_padding_layout.addWidget(self.frame_padding_label)
        self.frame_padding = QtGui.QLineEdit(self.frame_range_panel)
        self.frame_padding.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_padding.setObjectName("frame_padding")
        self.frame_padding_layout.addWidget(self.frame_padding)
        self.verticalLayout_3.addLayout(self.frame_padding_layout)
        self.frame_range_layout.addWidget(self.frame_range_panel)
        self.verticalLayout.addLayout(self.frame_range_layout)
        self.submit_panel_layout = QtGui.QVBoxLayout()
        self.submit_panel_layout.setSpacing(0)
        self.submit_panel_layout.setObjectName("submit_panel_layout")
        self.submit_panel_button = QtGui.QPushButton(MusterConnector)
        self.submit_panel_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submit_panel_button.setStyleSheet("text-align: left")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/julio/.designer/icons/gear_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_panel_button.setIcon(icon1)
        self.submit_panel_button.setCheckable(False)
        self.submit_panel_button.setObjectName("submit_panel_button")
        self.submit_panel_layout.addWidget(self.submit_panel_button)
        self.submit_panel = QtGui.QWidget(MusterConnector)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_panel.sizePolicy().hasHeightForWidth())
        self.submit_panel.setSizePolicy(sizePolicy)
        self.submit_panel.setMinimumSize(QtCore.QSize(400, 0))
        self.submit_panel.setObjectName("submit_panel")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.submit_panel)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(15, 0, 35, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.job_name_layout = QtGui.QHBoxLayout()
        self.job_name_layout.setSpacing(15)
        self.job_name_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.job_name_layout.setContentsMargins(0, -1, 0, -1)
        self.job_name_layout.setObjectName("job_name_layout")
        self.job_name_label = QtGui.QLabel(self.submit_panel)
        self.job_name_label.setMinimumSize(QtCore.QSize(80, 0))
        self.job_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.job_name_label.setObjectName("job_name_label")
        self.job_name_layout.addWidget(self.job_name_label)
        self.job_name = QtGui.QLineEdit(self.submit_panel)
        self.job_name.setObjectName("job_name")
        self.job_name_layout.addWidget(self.job_name)
        self.verticalLayout_4.addLayout(self.job_name_layout)
        self.image_folder_layout = QtGui.QHBoxLayout()
        self.image_folder_layout.setSpacing(15)
        self.image_folder_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.image_folder_layout.setObjectName("image_folder_layout")
        self.image_folder_label = QtGui.QLabel(self.submit_panel)
        self.image_folder_label.setMinimumSize(QtCore.QSize(80, 0))
        self.image_folder_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_folder_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_folder_label.setObjectName("image_folder_label")
        self.image_folder_layout.addWidget(self.image_folder_label)
        self.image_folder = QtGui.QLineEdit(self.submit_panel)
        self.image_folder.setObjectName("image_folder")
        self.image_folder_layout.addWidget(self.image_folder)
        self.open_path_button = QtGui.QPushButton(self.submit_panel)
        self.open_path_button.setMinimumSize(QtCore.QSize(22, 22))
        self.open_path_button.setMaximumSize(QtCore.QSize(22, 22))
        self.open_path_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/julio/.designer/icons/folder-o_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_path_button.setIcon(icon2)
        self.open_path_button.setObjectName("open_path_button")
        self.image_folder_layout.addWidget(self.open_path_button)
        self.verticalLayout_4.addLayout(self.image_folder_layout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.render_pool_label = QtGui.QLabel(self.submit_panel)
        self.render_pool_label.setMinimumSize(QtCore.QSize(80, 0))
        self.render_pool_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.render_pool_label.setObjectName("render_pool_label")
        self.horizontalLayout.addWidget(self.render_pool_label)
        self.render_pool = QtGui.QListWidget(self.submit_panel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.render_pool.sizePolicy().hasHeightForWidth())
        self.render_pool.setSizePolicy(sizePolicy)
        self.render_pool.setObjectName("render_pool")
        self.horizontalLayout.addWidget(self.render_pool)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.default_selection_button = QtGui.QPushButton(self.submit_panel)
        self.default_selection_button.setMinimumSize(QtCore.QSize(22, 22))
        self.default_selection_button.setMaximumSize(QtCore.QSize(22, 22))
        self.default_selection_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/refresh_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.default_selection_button.setIcon(icon3)
        self.default_selection_button.setObjectName("default_selection_button")
        self.verticalLayout_6.addWidget(self.default_selection_button)
        self.clear_selection_button = QtGui.QPushButton(self.submit_panel)
        self.clear_selection_button.setMinimumSize(QtCore.QSize(22, 22))
        self.clear_selection_button.setMaximumSize(QtCore.QSize(22, 22))
        self.clear_selection_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/remove_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_selection_button.setIcon(icon4)
        self.clear_selection_button.setObjectName("clear_selection_button")
        self.verticalLayout_6.addWidget(self.clear_selection_button)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.submit_button_layout = QtGui.QHBoxLayout()
        self.submit_button_layout.setSpacing(10)
        self.submit_button_layout.setContentsMargins(0, 10, -1, 10)
        self.submit_button_layout.setObjectName("submit_button_layout")
        self.submit_render_button = QtGui.QPushButton(self.submit_panel)
        self.submit_render_button.setMaximumSize(QtCore.QSize(200, 80))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/julio/.designer/icons/send-o_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_render_button.setIcon(icon5)
        self.submit_render_button.setObjectName("submit_render_button")
        self.submit_button_layout.addWidget(self.submit_render_button)
        self.verticalLayout_4.addLayout(self.submit_button_layout)
        self.submit_panel_layout.addWidget(self.submit_panel)
        self.verticalLayout.addLayout(self.submit_panel_layout)
        self.nuke_panel_layout = QtGui.QVBoxLayout()
        self.nuke_panel_layout.setSpacing(0)
        self.nuke_panel_layout.setObjectName("nuke_panel_layout")
        self.nuke_panel_button = QtGui.QPushButton(MusterConnector)
        self.nuke_panel_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nuke_panel_button.setStyleSheet("text-align: left")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/julio/nuke_scripts/icons/Write1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("C:/Users/julio/nuke_scripts/icons/Write.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nuke_panel_button.setIcon(icon6)
        self.nuke_panel_button.setCheckable(False)
        self.nuke_panel_button.setObjectName("nuke_panel_button")
        self.nuke_panel_layout.addWidget(self.nuke_panel_button)
        self.nuke_panel = QtGui.QWidget(MusterConnector)
        self.nuke_panel.setObjectName("nuke_panel")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.nuke_panel)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nuke_write_table_layout = QtGui.QVBoxLayout()
        self.nuke_write_table_layout.setSpacing(0)
        self.nuke_write_table_layout.setObjectName("nuke_write_table_layout")
        self.nuke_write_table = QtGui.QTableWidget(self.nuke_panel)
        self.nuke_write_table.setObjectName("nuke_write_table")
        self.nuke_write_table.setColumnCount(3)
        self.nuke_write_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.nuke_write_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.nuke_write_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.nuke_write_table.setHorizontalHeaderItem(2, item)
        self.nuke_write_table.horizontalHeader().setVisible(True)
        self.nuke_write_table.horizontalHeader().setDefaultSectionSize(45)
        self.nuke_write_table.horizontalHeader().setMinimumSectionSize(0)
        self.nuke_write_table.horizontalHeader().setStretchLastSection(False)
        self.nuke_write_table_layout.addWidget(self.nuke_write_table)
        self.verticalLayout_5.addLayout(self.nuke_write_table_layout)
        self.nuke_panel_layout.addWidget(self.nuke_panel)
        self.verticalLayout.addLayout(self.nuke_panel_layout)

        self.retranslateUi(MusterConnector)
        QtCore.QMetaObject.connectSlotsByName(MusterConnector)

    def retranslateUi(self, MusterConnector):
        MusterConnector.setWindowTitle(QtGui.QApplication.translate("MusterConnector", "MusterConnector", None, QtGui.QApplication.UnicodeUTF8))
        self.server_panel_button.setText(QtGui.QApplication.translate("MusterConnector", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.muster_ip_label.setText(QtGui.QApplication.translate("MusterConnector", "Muster Server", None, QtGui.QApplication.UnicodeUTF8))
        self.muster_ip.setText(QtGui.QApplication.translate("MusterConnector", "192.168.200.27", None, QtGui.QApplication.UnicodeUTF8))
        self.muster_port_label.setText(QtGui.QApplication.translate("MusterConnector", "Muster Port", None, QtGui.QApplication.UnicodeUTF8))
        self.muster_port.setText(QtGui.QApplication.translate("MusterConnector", "9681", None, QtGui.QApplication.UnicodeUTF8))
        self.priority_label.setText(QtGui.QApplication.translate("MusterConnector", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.priority.setText(QtGui.QApplication.translate("MusterConnector", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.muster_packet_size_label.setText(QtGui.QApplication.translate("MusterConnector", "Packet Size", None, QtGui.QApplication.UnicodeUTF8))
        self.packet_size.setText(QtGui.QApplication.translate("MusterConnector", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_range_panel_button.setText(QtGui.QApplication.translate("MusterConnector", "Frame Range", None, QtGui.QApplication.UnicodeUTF8))
        self.start_frame_label.setText(QtGui.QApplication.translate("MusterConnector", "Start Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.end_frame_label.setText(QtGui.QApplication.translate("MusterConnector", "End Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.by_frame_label.setText(QtGui.QApplication.translate("MusterConnector", "By Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_padding_label.setText(QtGui.QApplication.translate("MusterConnector", "Frame Padding", None, QtGui.QApplication.UnicodeUTF8))
        self.submit_panel_button.setText(QtGui.QApplication.translate("MusterConnector", "Render Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.job_name_label.setText(QtGui.QApplication.translate("MusterConnector", "Job Name", None, QtGui.QApplication.UnicodeUTF8))
        self.image_folder_label.setText(QtGui.QApplication.translate("MusterConnector", "Image Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.render_pool_label.setText(QtGui.QApplication.translate("MusterConnector", "Render Pools", None, QtGui.QApplication.UnicodeUTF8))
        self.render_pool.setToolTip(QtGui.QApplication.translate("MusterConnector", "<html><head/><body><p>(滑鼠右鍵) <span style=\" font-weight:600;\">選擇</span></p><p>(CTRL + 滑鼠右鍵)<span style=\" font-weight:600;\"> 減選</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.submit_render_button.setText(QtGui.QApplication.translate("MusterConnector", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.nuke_panel_button.setText(QtGui.QApplication.translate("MusterConnector", "Frame Range", None, QtGui.QApplication.UnicodeUTF8))
        self.nuke_write_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MusterConnector", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.nuke_write_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MusterConnector", "Node", None, QtGui.QApplication.UnicodeUTF8))

