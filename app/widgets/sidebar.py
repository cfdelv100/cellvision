from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QLabel,
    QWidget,
)

class Sidebar(QWidget):
    page_changed = Signal(str)
    
    def __init__(self) -> None:
        super().__init__()
        
        self.setObjectName("Sidebar")
        layout = QVBoxLayout(self)
        title = QLabel("Cell Vision")
        title.setObjectName("SidebarTitle")
        subtitle = QLabel("Dataset Explorer")
        subtitle.setObjectName("SidebarSubtitle")
        
        self.navigation = QListWidget()

        pages = [
            "Dashboard",
            "Images",
            "Annotations",
            "Splits",
            "YOLO",
            "Quality",
        ]

        for page in pages:
            QListWidgetItem(page, self.navigation,)
        self.navigation.currentItemChanged.connect(self._page_selected)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(self.navigation)

    def _page_selected(self, current, previous,) -> None:
        if current is not None:
            self.page_changed.emit(current.text())

