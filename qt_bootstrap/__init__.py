from PySide6.QtWidgets import QPushButton, QLineEdit, QTextEdit, QComboBox, QProgressBar


BTN_SS = '''
QPushButton {
  color: %s;
  background-color: %s;
  border: 1px solid;
  border-radius: 4px;
  padding: 8px 16px;
  height: 18px;
  font-weight: bold;
}

QPushButton:hover {
  background-color: %s;
}

QPushButton:pressed {
  background-color: %s;
}
'''

LINE_EDIT_SS = '''
    QLineEdit {
      color: #212529;
      background-color: #FFFFFF;
      border: 1px solid #CED4DA;
      border-radius: 4px;
      padding: 8px 16px;
      height: 18px;
    }

    QLineEdit:focus {
      border-color: #86B7FE;
    }

    QLineEdit:disabled {
      background-color: #E9ECEF;
    }

    QLineEdit::placeholder {
      color: #6C757D;
    }
'''

TEXT_EDIT_SS = '''
    QTextEdit {
      color: #212529;
      background-color: #FFFFFF;
      border: 1px solid #CED4DA;
      border-radius: 4px;
      padding: 8px 16px;
      height: 18px;
    }

    QTextEdit:focus {
      border-color: #86B7FE;
    }

    QTextEdit:disabled {
      background-color: #E9ECEF;
    }

    QTextEdit::placeholder {
      color: #6C757D;
    }
'''

COMBOBOX_SS = '''
    QComboBox {
      color: #212529;
      background-color: #FFFFFF;
      border: 1px solid #CED4DA;
      border-radius: 4px;
      padding: 8px 16px;
      height: 18px;
    }

    QComboBox:focus {
      border-color: #86B7FE;
    }

    QComboBox:disabled {
      background-color: #E9ECEF;
    }

    QComboBox::placeholder {
      color: #6C757D;
    }
'''

PROGRESS_BAR_SS = '''
    QProgressBar {
      text-align: center;
      border-radius: 4px;
      background-color: #E9ECEF;
    }

    QProgressBar::chunk {
      background-color: #0D6EFD;
    }
'''


class ButtonClasses:
    def __init__(self):
        self.BTN_PRIMARY = ['#FFFFFF', '#0D6EFD', '#0B5ED7', '#0A58CA']
        self.BTN_DANGER = ['#FFFFFF', '#DC3545', '#BB2D3B', '#B02A37']
        self.BTN_SECONDARY = ['#FFFFFF', '#6C757D', '#5C636A', '#565E64']
        self.BTN_LIGHT = ['#000000', '#F8F9FA', '#F9FAFB', '#F9FAFB']
        self.BTN_DARK = ['#FFFFFF', '#212529', '#1C1F23', '#1A1E21']
        self.BTN_SUCCESS = ['#FFFFFF', '#198754', '#157347', '#146C43']
        self.BTN_WARNING = ['#FFFFFF', '#FFC107', '#FFCA2C', '#FFCD39']
        self.BTN_INFO = ['#FFFFFF', '#0DCAF0', '#31D2F2', '#3DD5F3']


class QBSPrimaryButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSPrimaryButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_PRIMARY)
        self.setStyleSheet(stylesheet)


class QBSDangerButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSDangerButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_DANGER)
        self.setStyleSheet(stylesheet)


class QBSSecondaryButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSSecondaryButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_SECONDARY)
        self.setStyleSheet(stylesheet)


class QBSLightButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSLightButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_LIGHT)
        self.setStyleSheet(stylesheet)


class QBSDarkButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSDarkButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_DARK)
        self.setStyleSheet(stylesheet)


class QBSSuccessButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSSuccessButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_SUCCESS)
        self.setStyleSheet(stylesheet)


class QBSWarningButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSWarningButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_WARNING)
        self.setStyleSheet(stylesheet)


class QBSInfoButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QBSInfoButton, self).__init__(*args, **kwargs)
        btns = ButtonClasses()
        stylesheet = BTN_SS % tuple(btns.BTN_INFO)
        self.setStyleSheet(stylesheet)


class QBSLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(QBSLineEdit, self).__init__(*args, **kwargs)
        self.setStyleSheet(LINE_EDIT_SS)


class QBSTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super(QBSTextEdit, self).__init__(*args, **kwargs)
        self.setStyleSheet(TEXT_EDIT_SS)


class QBSComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super(QBSComboBox, self).__init__(*args, **kwargs)
        self.setStyleSheet(COMBOBOX_SS)


class QBSProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super(QBSProgressBar, self).__init__(*args, **kwargs)
        self.setStyleSheet(PROGRESS_BAR_SS)

