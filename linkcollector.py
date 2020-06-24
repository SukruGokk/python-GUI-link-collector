# @author : Şükrü Erdem Gök https://github.com/SukruGokk
# @date: 23/06/2020
# @os : Windows 10
# @version : Python 3.8

# GUI Link collector

# Lib
from PyQt5.QtGui import QFont, QIcon, QCursor
from PyQt5.QtCore import Qt, QRect, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QPushButton, QScrollArea, QWidget, QLabel, QVBoxLayout, QApplication, QTabWidget, QPlainTextEdit, QMessageBox, QInputDialog, QLineEdit, QMainWindow
from webbrowser import open
from bs4 import BeautifulSoup as BS
from requests import get


# Class for scrollable label
class ScrollLabel(QScrollArea):

    # Contstructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # Making widget resizable
        self.setWidgetResizable(True)

        # Making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # Vertical box layout
        lay = QVBoxLayout(content)

        # Creating label
        self.label = QLabel(content)

        # Setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Making label multi-line
        self.label.setWordWrap(True)

        # Adding label to the layout
        lay.addWidget(self.label)

    # Define settext method
    def setText(self, text):
        # Setting text to the label
        self.label.setText(text)

# Main form
class Ui_Form(object):

    # Setup
    def setupUi(self, Form):

        # Links array
        self.links = []
        Form.setObjectName("Form")

        # Window icon
        Form.setWindowIcon(QIcon("img/icon.ico"))

        # Unresizable
        Form.resize(397, 296)
        Form.setMaximumSize(397, 296)

        # Tab
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setGeometry(QRect(0, 0, 401, 301))
        self.tabWidget.setStyleSheet("background-color: rgb(133, 181, 191);")
        self.tabWidget.setObjectName("tabWidget")

        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")

        # Button to open github page
        self.githubButton = QPushButton(self.tab_3)
        self.githubButton.setGeometry(QRect(100, 0, 180, 120))
        self.githubButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.githubButton.setIconSize(QSize(200, 120))
        self.githubButton.setIcon(QIcon("img/GitHub.jpg"))
        self.githubButton.setObjectName("label")

        # Button to open telegram page
        self.telegramButton = QPushButton(self.tab_3)
        self.telegramButton.setGeometry(QRect(100, 140, 180, 120))
        self.telegramButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.telegramButton.setText("")
        self.telegramButton.setIcon(QIcon("img/Telegram.jpg"))
        self.telegramButton.setIconSize(QSize(210, 120))
        self.telegramButton.setObjectName("label_2")

        self.tabWidget.addTab(self.tab_3, "")

        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")

        # Text next to url entry
        self.urlText = QLabel(self.tab_2)
        self.urlText.setGeometry(QRect(10, 10, 111, 31))

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.urlText.setFont(font)
        self.urlText.setObjectName("urlText")

        # Text entry to get url
        self.url = QPlainTextEdit(self.tab_2)
        self.url.setGeometry(QRect(150, 10, 181, 41))

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)

        self.url.setFont(font)
        self.url.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.url.setObjectName("url")

        # Text next to filter key text entry
        self.filterText = QLabel(self.tab_2)
        self.filterText.setGeometry(QRect(10, 50, 121, 61))

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.filterText.setFont(font)
        self.filterText.setWordWrap(True)
        self.filterText.setObjectName("filterText")

        # Filter key entry
        self.contain = QPlainTextEdit(self.tab_2)
        self.contain.setGeometry(QRect(150, 50, 181, 61))

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(15)

        self.contain.setFont(font)
        self.contain.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.contain.setObjectName("contain")

        # Button to submit url
        self.urlButton = QPushButton(self.tab_2)
        self.urlButton.setGeometry(QRect(340, 10, 41, 41))

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.urlButton.setFont(font)
        self.urlButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.urlButton.setText("OK")
        self.urlButton.setObjectName("urlButton")

        # Button to submit filter key
        self.filterButton = QPushButton(self.tab_2)
        self.filterButton.setEnabled(False)
        self.filterButton.setGeometry(QRect(340, 60, 41, 41))

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.filterButton.setFont(font)
        self.filterButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.filterButton.setText("OK")
        self.filterButton.setObjectName("filterButton")

        # "RESULTS" label
        self.resultText = QLabel(self.tab_2)
        self.resultText.setGeometry(QRect(10, 120, 50, 50))
        font.setBold(True)
        font.setPointSize(15)
        self.resultText.setFont(font)

        self.resultText.setText("RESULTS")
        self.resultText.adjustSize()
        self.resultText.setObjectName("resultText")

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        # Creating scroll label
        self.label = ScrollLabel(self.tab_2)

        self.label.setGeometry(10, 150, 300, 100)

        # Button to open url
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(100, 125, 70, 20))

        font = QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")

        # Title of help text
        self.help_title_label = QLabel(self.tab_1)
        self.help_title_label.setText("HOW TO USE ?")
        self.help_title_label.move(10, 10)
        self.help_title_label.setFont(font)
        self.help_label = QLabel(self.tab_1)

        font.setBold(False)
        font.setPointSize(12)

        # Help text
        helpText = "OPEN LINK COLLECTOR TAB AND WRITE THE URL \nTHAT YOU WANT FIND LINKS. THEN CLICK OK BUTTON.\n\nTO FILTER LINKS, WRITE WHICH SHOULD LINK \nCONTAIN TO THE TEXT ENTRY.\n\nTO OPEN A URL WRITE WRITE INDEX OF URL TO \nPOP UP DIALOG AND CLICK OK."

        # Help text label
        self.help_label.setFont(font)
        self.help_label.move(10, 30)
        self.help_label.setText(helpText)
        self.help_label.setWordWrap(True)

        # Add tabs
        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)

        #Set current tab
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # Method to open github page
    def github(self):
        open("https://github.com/SukruGokk")

    # Method to open telegram page
    def telegram(self):
        open("https://t.me/SukruGokk")

    # Method for get urls
    def connect(self):
        # Get link from user with input
        url = self.url.document().toPlainText()

        # Try to connect
        try:

            # Connect
            r = get(url)

            # Parse page's codes
            soup = BS(r.content, "lxml")

            # Get links from site content
            for link in soup.findAll('a'):
                # If it doesnt contains http, dont but if it contains append
                if str(link.get('href')).find("http") == -1:
                    pass
                else:
                    self.links.append(link.get('href'))

            # Enable button to submit filter key
            self.filterButton.setEnabled(True)

            # String of links
            self.strLinks = ""

            # Add list's elements to string
            num = 1
            for i in self.links:
                self.strLinks += str(num)
                self.strLinks += " "
                self.strLinks += i
                self.strLinks += '\n'
                num += 1

            # Display urls
            self.label.setText(self.strLinks)

        # If url if invalid
        except:

            # Show error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("INVALID URL")
            msg.setWindowTitle("ERROR")
            msg.setFont(QFont("Berlin Sans FB", 20, 17))
            msg.exec_()

    # Filter the links according to filter key
    def filterLinks(self):
        self.filterKey = self.contain.document().toPlainText()
        self.filteredLinks = []

        for i in self.links:
            if i.find(self.filterKey) != -1:
                self.filteredLinks.append(i)
        num = 1
        self.strLinks = ""

        for i in self.filteredLinks:
            self.strLinks += str(num)
            self.strLinks += " "
            self.strLinks += i
            self.strLinks += '\n'
            num += 1

        # Enable open link button
        self.pushButton.setEnabled(True)
        self.label.setText(self.strLinks)

    # Open selected link
    def openLink(self):
            text, okPressed = QInputDialog.getText(self.tab_2, "NUMBER OF URL", "NUMBER: ", QLineEdit.Normal, "")

            # Open url
            try:
                if okPressed:
                    open(self.filteredLinks[int(text)-1])

            # If index is invalid
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("INVALID")
                msg.setFont(QFont("Berlin Sans FB", 20, 17))
                msg.setWindowTitle("INVALID")
                msg.exec_()

    # Retranslate method
    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate

        # Set title
        Form.setWindowTitle("LINK COLLECTOR")

        # Set tab text
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "HELP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "LINK COLLECTOR"))

        self.urlText.setText(_translate("Form", "WRITE URL"))
        self.filterText.setText(_translate("Form", "What should link contain"))
        self.pushButton.setText(_translate("Form", "OPEN LINK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "DEVELOPER"))
        self.url.document().setPlainText("https://")

        # Onlick events
        self.urlButton.clicked.connect(self.connect)
        self.filterButton.clicked.connect(self.filterLinks)
        self.pushButton.clicked.connect(self.openLink)
        self.githubButton.clicked.connect(self.github)
        self.telegramButton.clicked.connect(self.telegram)

# Run code
if __name__ == "__main__":
   from sys import exit, argv

   # Applicaiton
   app = QApplication(argv)

   # Main Window
   MainWindow = QMainWindow()

   ui = Ui_Form()

   ui.setupUi(MainWindow)

   # Show and run
   MainWindow.show()
   exit(app.exec_())