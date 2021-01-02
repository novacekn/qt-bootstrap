from PySide6.QtWidgets import QComboBox


class QBSComboBox(QComboBox):
    BS_COMBOBOX_STYLE_SHEET = '''
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

    def __init__(self):
        super(QBSComboBox, self).__init__()
        self.setStyleSheet(self.BS_COMBOBOX_STYLE_SHEET)

