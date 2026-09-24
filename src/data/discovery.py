from pathlib import Path

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
}

ANNOTATION_EXTENSIONS = {
    ".xml",
    ".json",
    ".txt",

}

def find_images(dataset_path: Path) -> list[Path]:
    """Recursive searching for image files."""
    return sorted(
        path
        for path in dataset_path.rglob("*")
        if(path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS)
    )

def find_annotations(dataset_path: Path) -> list[Path]:
    """Rescursive search for annoation files."""
    return sorted(
        path 
        for path in dataset_path.rglob("*")
        if(path.is_file() and path.suffix.lower() in ANNOTATION_EXTENSIONS)
    )