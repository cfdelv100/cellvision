from pathlib import Path
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QWidget,
)
from app.widgets.dashboard import Dashboard
from app.widgets.sidebar import Sidebar
from src.data.stats import analyze_dataset


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Cell Vision Blood Cell Dataset Explorer")

        self.resize(1280, 800)
        self.setup_ui()

    def setup_ui(self) -> None:
        central = QWidget()

        layout = QHBoxLayout(central)

        self.sidebar = Sidebar()

        self.dashboard = Dashboard()

        self.pages = QStackedWidget()

        self.pages.addWidget(self.dashboard)

        layout.addWidget(self.sidebar)

        layout.addWidget(self.pages, 1)

        self.setCentralWidget(central)

        self.dashboard.select_button.clicked.connect(self.select_dataset)

    def select_dataset(self) -> None:

        directory = (QFileDialog.getExistingDirectory(self,"Select Cell Vision Dataset"))
        if not directory:
            return

        dataset_path = Path(directory)

        dataset = analyze_dataset(dataset_path)

        self.dashboard.update_dataset(dataset)