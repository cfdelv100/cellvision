from dataclasses import dataclass, field
from pathlib import Path

# structured representaiton of the dataset
@dataclass
class DatasetInfo:
    path: Path

    # Dataset Discoveries
    image_count: int = 0
    annotation_count: int = 0
    
    # Validation
    invalid_image_count: int = 0
    invalid_annotation_count: int = 0
    
    # Annotation Information
    total_object_count: int = 0
    classes: list[str] = field(default_factory=list)
    class_counts: dict[str, int] = field(default_factory=dict)

    # Dataset Split
    train_count: int = 0
    validation_count: int = 0
    test_count: int = 0 

    # Pipeline State
    split_created: bool = False
    yolo_conversion_complete: bool = False

    @property
    def valid(self) -> bool:
        return(self.invalid_image_count == 0 and self.invalid_annotation_count == 0)

# Split Information
@dataclass
class DatasetSplit:
    train: list[Path] = field(default_factory=list)
    validation: list[Path] = field(default_factory=list)
    test: list[Path] = field(default_factory=list)

    @property
    def total(self) -> int:
        return(len(self.train) + len(self.validation) + len(self.test))


