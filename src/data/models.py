from dataclasses import dataclass, field
from pathlib import Path

# structured representaiton of the dataset
@dataclass
class DatasetInfo:
    path: Path
    image_count: int = 0
    annotation_count: int = 0
    invalid_image_count: int = 0
    invalid_annotation_count: int = 0
    classes: list[str] = field(default_factory=list)

