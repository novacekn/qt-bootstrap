from PySide6.QtWidgets import QProgressBar


class QBSProgressBar(QProgressBar):
    BS_PROGRESS_BAR_STYLE_SHEET = '''
    QProgressBar {
      text-align: center;
      border-radius: 4px;
      background-color: #E9ECEF;
    }

    QProgressBar::chunk {
      background-color: #0D6EFD;
    }
    '''

    def __init__(self):
        super(QBSProgressBar, self).__init__()
        self.setStyleSheet(self.BS_PROGRESS_BAR_STYLE_SHEET)

