from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)

class StatusPanel(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("StatusPanel")

        layout = QVBoxLayout(self)
        title = QLabel("Pipeline Status")
        title.setObjectName("SectionTitle")
        self.status = QLabel("No Dataset Found.")

        self.status.setWordWrap(True)
        layout.addWidget(title)
        layout.addWidget(self.status)

    def update_status(self, text: str,) -> None:
        self.status.setText(text)
