# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personProjectWizard.ui'
#
# Created: Tue Feb 12 19:48:43 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_personProjectWizard(object):
    def setupUi(self, personProjectWizard):
        personProjectWizard.setObjectName(_fromUtf8("personProjectWizard"))
        personProjectWizard.resize(879, 658)
        self.personProjectWizardPage1 = QtGui.QWizardPage()
        self.personProjectWizardPage1.setObjectName(_fromUtf8("personProjectWizardPage1"))
        self.gridLayoutWidget = QtGui.QWidget(self.personProjectWizardPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 591))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.personProjectDescriptionValue = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.personProjectDescriptionValue.setObjectName(_fromUtf8("personProjectDescriptionValue"))
        self.gridLayout_3.addWidget(self.personProjectDescriptionValue, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        self.personProjectNameValue = QtGui.QLineEdit(self.gridLayoutWidget)
        self.personProjectNameValue.setObjectName(_fromUtf8("personProjectNameValue"))
        self.gridLayout_3.addWidget(self.personProjectNameValue, 0, 1, 1, 1)
        self.personProjectNameLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.personProjectNameLabel.setEnabled(True)
        self.personProjectNameLabel.setObjectName(_fromUtf8("personProjectNameLabel"))
        self.gridLayout_3.addWidget(self.personProjectNameLabel, 0, 0, 1, 1)
        self.personProjectKeywordsValue = QtGui.QLineEdit(self.gridLayoutWidget)
        self.personProjectKeywordsValue.setObjectName(_fromUtf8("personProjectKeywordsValue"))
        self.gridLayout_3.addWidget(self.personProjectKeywordsValue, 1, 1, 1, 1)
        self.personProjectDescriptionLabel = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personProjectDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.personProjectDescriptionLabel.setSizePolicy(sizePolicy)
        self.personProjectDescriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.personProjectDescriptionLabel.setObjectName(_fromUtf8("personProjectDescriptionLabel"))
        self.gridLayout_3.addWidget(self.personProjectDescriptionLabel, 2, 0, 1, 1)
        self.personProkectKeywordsLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.personProkectKeywordsLabel.setObjectName(_fromUtf8("personProkectKeywordsLabel"))
        self.gridLayout_3.addWidget(self.personProkectKeywordsLabel, 1, 0, 1, 1)
        personProjectWizard.addPage(self.personProjectWizardPage1)
        self.personProjectWizardPage2 = QtGui.QWizardPage()
        self.personProjectWizardPage2.setObjectName(_fromUtf8("personProjectWizardPage2"))
        self.gridLayout = QtGui.QGridLayout(self.personProjectWizardPage2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.personProjectSearchResultsLabel = QtGui.QLabel(self.personProjectWizardPage2)
        self.personProjectSearchResultsLabel.setObjectName(_fromUtf8("personProjectSearchResultsLabel"))
        self.gridLayout.addWidget(self.personProjectSearchResultsLabel, 4, 0, 1, 1)
        self.personProjectAvailablePluginsScrollArea = QtGui.QScrollArea(self.personProjectWizardPage2)
        self.personProjectAvailablePluginsScrollArea.setWidgetResizable(True)
        self.personProjectAvailablePluginsScrollArea.setObjectName(_fromUtf8("personProjectAvailablePluginsScrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 729, 155))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.personProjectAvailablePluginsListView = QtGui.QListView(self.scrollAreaWidgetContents)
        self.personProjectAvailablePluginsListView.setObjectName(_fromUtf8("personProjectAvailablePluginsListView"))
        self.verticalLayout.addWidget(self.personProjectAvailablePluginsListView)
        self.personProjectAvailablePluginsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.personProjectAvailablePluginsScrollArea, 1, 2, 1, 2)
        self.personProjectSearchForDetailsLabel = QtGui.QLabel(self.personProjectWizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personProjectSearchForDetailsLabel.sizePolicy().hasHeightForWidth())
        self.personProjectSearchForDetailsLabel.setSizePolicy(sizePolicy)
        self.personProjectSearchForDetailsLabel.setObjectName(_fromUtf8("personProjectSearchForDetailsLabel"))
        self.gridLayout.addWidget(self.personProjectSearchForDetailsLabel, 0, 3, 1, 1)
        self.personProjectSearchForLabel = QtGui.QLabel(self.personProjectWizardPage2)
        self.personProjectSearchForLabel.setObjectName(_fromUtf8("personProjectSearchForLabel"))
        self.gridLayout.addWidget(self.personProjectSearchForLabel, 0, 0, 1, 2)
        self.personProjectTargetSeperatorLine = QtGui.QFrame(self.personProjectWizardPage2)
        self.personProjectTargetSeperatorLine.setLineWidth(4)
        self.personProjectTargetSeperatorLine.setFrameShape(QtGui.QFrame.HLine)
        self.personProjectTargetSeperatorLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.personProjectTargetSeperatorLine.setObjectName(_fromUtf8("personProjectTargetSeperatorLine"))
        self.gridLayout.addWidget(self.personProjectTargetSeperatorLine, 5, 1, 1, 3)
        self.personProjectSearchInLabel = QtGui.QLabel(self.personProjectWizardPage2)
        self.personProjectSearchInLabel.setObjectName(_fromUtf8("personProjectSearchInLabel"))
        self.gridLayout.addWidget(self.personProjectSearchInLabel, 1, 0, 1, 2)
        self.personProjectSearchForValue = QtGui.QLineEdit(self.personProjectWizardPage2)
        self.personProjectSearchForValue.setObjectName(_fromUtf8("personProjectSearchForValue"))
        self.gridLayout.addWidget(self.personProjectSearchForValue, 0, 2, 1, 1)
        self.personProjectSelectedTargetsLabel = QtGui.QLabel(self.personProjectWizardPage2)
        self.personProjectSelectedTargetsLabel.setObjectName(_fromUtf8("personProjectSelectedTargetsLabel"))
        self.gridLayout.addWidget(self.personProjectSelectedTargetsLabel, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.personProjectSearchButton = QtGui.QPushButton(self.personProjectWizardPage2)
        self.personProjectSearchButton.setObjectName(_fromUtf8("personProjectSearchButton"))
        self.horizontalLayout_2.addWidget(self.personProjectSearchButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 3, 1, 1)
        self.personProjectSearchResultsTable = QtGui.QTableView(self.personProjectWizardPage2)
        self.personProjectSearchResultsTable.setDragEnabled(True)
        self.personProjectSearchResultsTable.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.personProjectSearchResultsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.personProjectSearchResultsTable.setSortingEnabled(True)
        self.personProjectSearchResultsTable.setObjectName(_fromUtf8("personProjectSearchResultsTable"))
        self.personProjectSearchResultsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.personProjectSearchResultsTable.horizontalHeader().setStretchLastSection(True)
        self.personProjectSearchResultsTable.verticalHeader().setVisible(False)
        self.personProjectSearchResultsTable.verticalHeader().setCascadingSectionResizes(True)
        self.personProjectSearchResultsTable.verticalHeader().setMinimumSectionSize(19)
        self.personProjectSearchResultsTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.personProjectSearchResultsTable, 4, 2, 1, 2)
        self.personProjectSelectedTargetsTable = QtGui.QTableView(self.personProjectWizardPage2)
        self.personProjectSelectedTargetsTable.setDragEnabled(False)
        self.personProjectSelectedTargetsTable.setDragDropOverwriteMode(True)
        self.personProjectSelectedTargetsTable.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.personProjectSelectedTargetsTable.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.personProjectSelectedTargetsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.personProjectSelectedTargetsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.personProjectSelectedTargetsTable.setSortingEnabled(True)
        self.personProjectSelectedTargetsTable.setObjectName(_fromUtf8("personProjectSelectedTargetsTable"))
        self.personProjectSelectedTargetsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.personProjectSelectedTargetsTable.horizontalHeader().setStretchLastSection(True)
        self.personProjectSelectedTargetsTable.verticalHeader().setVisible(False)
        self.personProjectSelectedTargetsTable.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.personProjectSelectedTargetsTable, 7, 2, 1, 2)
        personProjectWizard.addPage(self.personProjectWizardPage2)
        self.personProjectWizardPage3 = QtGui.QWizardPage()
        self.personProjectWizardPage3.setObjectName(_fromUtf8("personProjectWizardPage3"))
        self.verticalLayoutWidget = QtGui.QWidget(self.personProjectWizardPage3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 851, 521))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.personProjectPluginConfigLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.personProjectPluginConfigLayout.setMargin(0)
        self.personProjectPluginConfigLayout.setObjectName(_fromUtf8("personProjectPluginConfigLayout"))
        personProjectWizard.addPage(self.personProjectWizardPage3)
        self.personProjectWizardPage4 = QtGui.QWizardPage()
        self.personProjectWizardPage4.setObjectName(_fromUtf8("personProjectWizardPage4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.personProjectWizardPage4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        personProjectWizard.addPage(self.personProjectWizardPage4)

        self.retranslateUi(personProjectWizard)
        QtCore.QMetaObject.connectSlotsByName(personProjectWizard)

    def retranslateUi(self, personProjectWizard):
        personProjectWizard.setWindowTitle(QtGui.QApplication.translate("personProjectWizard", "New Person Project", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage1.setTitle(QtGui.QApplication.translate("personProjectWizard", "Step 1 - Set Project Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage1.setSubTitle(QtGui.QApplication.translate("personProjectWizard", "Add project related information", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectNameLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Project Name ", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectDescriptionLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.personProkectKeywordsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Keywords", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage2.setTitle(QtGui.QApplication.translate("personProjectWizard", "Step 2 - Set the target", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage2.setSubTitle(QtGui.QApplication.translate("personProjectWizard", "Search for the person you want to track using the available plugins and add it to the selected targets", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchResultsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search Results ", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchForDetailsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search by username, mail, full name, id", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchForLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search for", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchInLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search In", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSelectedTargetsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Selected Targets", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchButton.setText(QtGui.QApplication.translate("personProjectWizard", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage3.setTitle(QtGui.QApplication.translate("personProjectWizard", "Step 3 - Set Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage3.setSubTitle(QtGui.QApplication.translate("personProjectWizard", "Provide the necessary search parameters for the plugins you are using", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage4.setTitle(QtGui.QApplication.translate("personProjectWizard", "Step 4  - Finalize Project", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectWizardPage4.setSubTitle(QtGui.QApplication.translate("personProjectWizard", "Click Finish to save the Project Configuration ", None, QtGui.QApplication.UnicodeUTF8))

