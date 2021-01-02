from PySide6.QtWidgets import QTextEdit


class QBSTextEdit(QTextEdit):
    BS_TEXT_EDIT_STYLE_SHEET = '''
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

    def __init__(self, placeholder=None):
        super(QBSTextEdit, self).__init__()
        self.placeholder = placeholder
        if self.placeholder is not None:
            self.setPlaceholderText(self.placeholder)
        self.setStyleSheet(self.BS_TEXT_EDIT_STYLE_SHEET)

