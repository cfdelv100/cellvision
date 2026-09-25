from PySide6.QtWidgets import (
    QFrame, 
    QLabel,
    QVBoxLayout,
)

class StatCard(QFrame):

    def __init__(
        self,
        title: str,
        value: str = "-",
        subtitle: str = "",
    ) -> None:
        super().__init__()
        self.setObjectName("StatCard")

        layout = QVBoxLayout(self)

        self.title_label = QLabel(title)
        self.value_label = QLabel(value)
        self.subtitle_label = QLabel(subtitle)

        self.title_label.setObjectName("StatCardTitle")
        self.subtitle_label.setObjectName("StatCardSubtitle")

        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        layout.addWidget(self.subtitle_label)

    def set_value(self, value: str,) -> None:
        self.value_label.setText(value)

    def set_subtitle(self, subtitle: str,) -> None:
        self.subtitle_label.setText(subtitle)