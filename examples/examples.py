from PySide6 import QtWidgets
from qt_bootstrap import *

import sys

BACKGROUND_COLOR = '#F8F9FA'


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(600, 425)

        layout = QtWidgets.QVBoxLayout()
        self.setStyleSheet('QWidget { background-color: %s; }' % BACKGROUND_COLOR)

        primary_btn = QBSPrimaryButton('PRIMARY')
        danger_btn = QBSDangerButton('DANGER')
        secondary_btn = QBSSecondaryButton('SECONDARY')
        light_btn = QBSLightButton('LIGHT')
        dark_btn = QBSDarkButton('DARK')
        success_btn = QBSSuccessButton('SUCCESS')
        warning_btn = QBSWarningButton('WARNING')
        info_btn = QBSInfoButton('INFO')

        line_edit = QBSLineEdit()
        text_edit = QBSTextEdit()

        combobox = QBSComboBox()
        combobox.addItem('Item 1')
        combobox.addItem('Item 2')

        progress_bar = QBSProgressBar()
        progress_bar.setValue(25)

        layout.addWidget(primary_btn)
        layout.addWidget(danger_btn)
        layout.addWidget(secondary_btn)
        layout.addWidget(light_btn)
        layout.addWidget(dark_btn)
        layout.addWidget(success_btn)
        layout.addWidget(warning_btn)
        layout.addWidget(info_btn)
        layout.addWidget(line_edit)
        layout.addWidget(text_edit)
        layout.addWidget(combobox)
        layout.addWidget(progress_bar)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet('* { font: 11pt "Segoe UI"; }')
    window.show()
    sys.exit(app.exec_())
        
