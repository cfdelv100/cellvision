from pathlib import Path

from PIL import Image

def validate_image(image_path: Path) -> tuple[bool, str | None]:
    # validate the image can be opened and read. 
    try: 
        with Image.open(image_path) as image:
            image.verify()

        return True, None

    except Exception as e:
        return False, str(e)
