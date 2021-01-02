from PySide6.QtWidgets import QPushButton


class ButtonColors:
    def __init__(self):
        PRIMARY_COLOR = '#FFFFFF'
        PRIMARY_BACKGROUND = '#0D6EFD'
        PRIMARY_HOVER = '#0B5ED7'
        PRIMARY_PRESSED = '#0A58CA'
        self.PRIMARY = [PRIMARY_COLOR, PRIMARY_BACKGROUND, PRIMARY_HOVER, PRIMARY_PRESSED]

        DANGER_COLOR = '#FFFFFF'
        DANGER_BACKGROUND = '#DC3545'
        DANGER_HOVER = '#BB2D3B'
        DANGER_PRESSED = '#B02A37'
        self.DANGER = [DANGER_COLOR, DANGER_BACKGROUND, DANGER_HOVER, DANGER_PRESSED]

        SECONDARY_COLOR = '#FFFFFF'
        SECONDARY_BACKGROUND = '#6C757D'
        SECONDARY_HOVER = '#5C636A'
        SECONDARY_PRESSED = '#565E64'
        self.SECONDARY = [SECONDARY_COLOR, SECONDARY_BACKGROUND, SECONDARY_HOVER, SECONDARY_PRESSED]

        LIGHT_COLOR = '#000000'
        LIGHT_BACKGROUND = '#F8F9FA'
        LIGHT_HOVER = '#F9FAFB'
        LIGHT_PRESSED = '#F9FAFB'
        self.LIGHT = [LIGHT_COLOR, LIGHT_BACKGROUND, LIGHT_HOVER, LIGHT_PRESSED]

        DARK_COLOR = '#FFFFFF'
        DARK_BACKGROUND = '#212529'
        DARK_HOVER = '#1C1F23'
        DARK_PRESSED = '#1A1E21'
        self.DARK = [DARK_COLOR, DARK_BACKGROUND, DARK_HOVER, DARK_PRESSED]

        SUCCESS_COLOR = '#FFFFFF'
        SUCCESS_BACKGROUND = '#198754'
        SUCCESS_HOVER = '#157347'
        SUCCESS_PRESSED = '#146C43'
        self.SUCCESS = [SUCCESS_COLOR, SUCCESS_BACKGROUND, SUCCESS_HOVER, SUCCESS_PRESSED]

        WARNING_COLOR = '#FFFFFF'
        WARNING_BACKGROUND = '#FFC107'
        WARNING_HOVER = '#FFCA2C'
        WARNING_PRESSED = '#FFCD39'
        self.WARNING = [WARNING_COLOR, WARNING_BACKGROUND, WARNING_HOVER, WARNING_PRESSED]

        INFO_COLOR = '#FFFFFF'
        INFO_BACKGROUND = '#0DCAF0'
        INFO_HOVER = '#31D2F2'
        INFO_PRESSED = '#3DD5F3'
        self.INFO = [INFO_COLOR, INFO_BACKGROUND, INFO_HOVER, INFO_PRESSED]


class QBSPushButton(QPushButton):
    BTN_STYLE_SHEET = '''
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

    def __init__(self, btn_text, btn_class):
        super(QBSPushButton, self).__init__()
        self.btn_text = btn_text
        self.setText(btn_text)
        self._style_sheet = self.BTN_STYLE_SHEET
        self.btn_class = btn_class
        self._btn_colors = ButtonColors()
        self._format_stylesheet()

    def _format_stylesheet(self):
        if self.btn_class == 'primary':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.PRIMARY)
        elif self.btn_class == 'danger':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.DANGER)
        elif self.btn_class == 'secondary':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.SECONDARY)
        elif self.btn_class == 'light':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.LIGHT)
        elif self.btn_class == 'dark':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.DARK)
        elif self.btn_class == 'success':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.SUCCESS)
        elif self.btn_class == 'warning':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.WARNING)
        elif self.btn_class == 'info':
            self._style_sheet = self._style_sheet % tuple(self._btn_colors.INFO)
        
        self.setStyleSheet(self._style_sheet)


class QBSPrimaryButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='primary'):
        super(QBSPrimaryButton, self).__init__(btn_text=btn_text, btn_class=btn_class)


class QBSDangerButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='danger'):
        super(QBSDangerButton, self).__init__(btn_text=btn_text, btn_class=btn_class)


class QBSSecondaryButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='secondary'):
        super(QBSSecondaryButton, self).__init__(btn_text=btn_text, btn_class=btn_class)


class QBSLightButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='light'):
        super(QBSLightButton, self).__init__(btn_text=btn_text, btn_class=btn_class)


class QBSDarkButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='dark'):
        super(QBSDarkButton, self).__init__(btn_text=btn_text, btn_class=btn_class)


class  QBSSuccessButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='success'):
        super(QBSSuccessButton, self).__init__(btn_text=btn_text, btn_class=btn_class)


class QBSWarningButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='warning'):
        super(QBSWarningButton, self).__init__(btn_text=btn_text, btn_class=btn_class)


class QBSInfoButton(QBSPushButton):
    def __init__(self, btn_text, btn_class='info'):
        super(QBSInfoButton, self).__init__(btn_text=btn_text, btn_class=btn_class)

