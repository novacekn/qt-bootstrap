from PySide6.QtWidgets import QLineEdit


class QBSLineEdit(QLineEdit):
    BS_LINE_EDIT_STYLE_SHEET = '''
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

    def __init__(self, placeholder=None):
        super(QBSLineEdit, self).__init__()
        self.placeholder = placeholder
        if self.placeholder is not None:
            self.setPlaceholderText(self.placeholder)
        self.setStyleSheet(self.BS_LINE_EDIT_STYLE_SHEET)

