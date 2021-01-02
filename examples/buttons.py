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

import sys


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(600, 425)

        layout = QtWidgets.QVBoxLayout()

        primary_btn = QBSPrimaryButton(btn_text='PRIMARY')
        danger_btn = QBSDangerButton(btn_text='DANGER')
        secondary_btn = QBSSecondaryButton(btn_text='SECONDARY')
        light_btn = QBSLightButton(btn_text='LIGHT')
        dark_btn = QBSDarkButton(btn_text='DARK')
        success_btn = QBSSuccessButton(btn_text='SUCCESS')
        warning_btn = QBSWarningButton(btn_text='WARNING')
        info_btn = QBSInfoButton(btn_text='INFO')

        layout.addWidget(primary_btn)
        layout.addWidget(danger_btn)
        layout.addWidget(secondary_btn)
        layout.addWidget(light_btn)
        layout.addWidget(dark_btn)
        layout.addWidget(success_btn)
        layout.addWidget(warning_btn)
        layout.addWidget(info_btn)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        
