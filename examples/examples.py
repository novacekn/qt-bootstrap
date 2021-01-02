from PySide6 import QtWidgets
from qt_bootstrap.buttons import (
        QBSPrimaryButton, 
        QBSDangerButton, 
        QBSSecondaryButton, 
        QBSLightButton, 
        QBSDarkButton, 
        QBSSuccessButton, 
        QBSWarningButton, 
        QBSInfoButton
)
from qt_bootstrap.lineedit import QBSLineEdit
from qt_bootstrap.textedit import QBSTextEdit
from qt_bootstrap.combobox import QBSComboBox
from qt_bootstrap.progressbar import QBSProgressBar

import sys

BACKGROUND_COLOR = '#F8F9FA'


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(600, 425)

        layout = QtWidgets.QVBoxLayout()
        self.setStyleSheet('QWidget { background-color: %s; }' % BACKGROUND_COLOR)

        primary_btn = QBSPrimaryButton(btn_text='PRIMARY')
        danger_btn = QBSDangerButton(btn_text='DANGER')
        secondary_btn = QBSSecondaryButton(btn_text='SECONDARY')
        light_btn = QBSLightButton(btn_text='LIGHT')
        dark_btn = QBSDarkButton(btn_text='DARK')
        success_btn = QBSSuccessButton(btn_text='SUCCESS')
        warning_btn = QBSWarningButton(btn_text='WARNING')
        info_btn = QBSInfoButton(btn_text='INFO')

        line_edit = QBSLineEdit(placeholder='This is a placeholder.')

        text_edit = QBSTextEdit(placeholder='This is a placeholder.')

        combobox = QBSComboBox()
        combobox.addItem('Cats')
        combobox.addItem('Dogs')

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
        
