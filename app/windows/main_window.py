from PySide6.QtWidgets import(
    QFileDialog,
    QHBoxLayout,
    QMainWindow, 
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from pathlib import Path
from src.data.stats import analyze_dataset

class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("CellVision Dataset Explorer")
        self.resize(1100, 700)
        self.setup_ui()

    def setup_ui(self) -> None:
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        title = QLabel("CellVision")
        subtitle = QLabel("Blood Cell Dataset Explorer")
        self.select_button = QPushButton("Select Dataset")
        self.select_button.clicked.connect(self.select_data)
        
        self.status = QLabel("No Dataset Selected")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        # layout.addWidget(select_button)
        # layout.addWidget(status)
        layout.addWidget(self.select_button)
        layout.addWidget(self.status)

        self.setCentralWidget(central_widget)

    def select_data(self) -> None:
        directory = QFileDialog.getExistingDirectory(self, "Select Cell Vision Dataset")
        if not directory:
            return
        
        dataset_path = Path(directory)
        self.status.setText(f"Selected: {dataset_path}")
        result = analyze_dataset(dataset_path)
        self.status.setText("\n".join(
            [
                f"Dataset: {result.path}",
                f"Images: {result.image_count}",
                f"Annotations: {result.annotation_count}",
                (
                    "Invalid Images: "
                    f"{result.invalid_image_count}"  
                ),
            ]
        ))