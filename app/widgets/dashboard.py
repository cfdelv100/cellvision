from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from app.widgets.stat_card import StatCard
from app.widgets.status_panel import StatusPanel


class Dashboard(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:

        layout = QVBoxLayout(self)

        title = QLabel("Dataset Overview")
        title.setObjectName("PageTitle")
        subtitle = QLabel(
            "Analyze and validate your "
            "blood-cell computer vision dataset."
        )
        subtitle.setObjectName("PageSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        
        self.select_button = QPushButton("Select Dataset")

        layout.addWidget(self.select_button)
        layout.addSpacing(20)

        stats = QHBoxLayout()

        self.images_card = StatCard("Images")

        self.annotations_card = StatCard("Annotations")

        self.classes_card = StatCard("Classes")

        self.invalid_card = StatCard("Invalid Images")

        stats.addWidget(self.images_card)
        stats.addWidget(self.annotations_card)
        stats.addWidget(self.classes_card)
        stats.addWidget(self.invalid_card)

        layout.addLayout(stats)
        layout.addSpacing(20)

        self.status_panel = StatusPanel()

        layout.addWidget(self.status_panel)

        layout.addStretch()

    def update_dataset(self, dataset,) -> None:

        self.images_card.set_value(str(dataset.image_count))

        self.annotations_card.set_value(str(dataset.annotation_count))

        self.classes_card.set_value(str(len(dataset.classes)))

        self.invalid_card.set_value(str(dataset.invalid_image_count))

        status = (
            f"Dataset: {dataset.path}\n\n"
            f"Images discovered: "
            f"{dataset.image_count}\n"
            f"Annotations discovered: "
            f"{dataset.annotation_count}\n"
            f"Dataset valid: "
            f"{'Yes' if dataset.valid else 'No'}"
        )

        self.status_panel.update_status(status)