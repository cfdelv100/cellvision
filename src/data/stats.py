from pathlib import Path
from .discovery import (find_annotations, find_images,)
from .models import DatasetInfo
from .validation import validate_image

def analyze_dataset(dataset_path: Path) -> DatasetInfo:
    images = find_images(dataset_path)
    annotations = find_annotations(dataset_path)

    invalid_images = 0

    for image in images:
        valid, _ = validate_image(image)
        if not valid:
            invalid_images += 1
    return DatasetInfo(
        path=dataset_path,
        image_count=len(images),
        annotation_count=len(annotations),
        invalid_image_count=invalid_images,
    )

