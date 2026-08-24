from pathlib import Path
import xml.etree.ElementTree as ET 
import pandas as pd 

def parse_annotation(annotation_path: Path) -> list[dict]:
    """Returning one Pascal VOC XML annotation and one dictionary per annotated object."""
    tree = ET.parse(annotation_path)
    root = tree.getroot()
    
    filename = root.findtext("filename")
    size = root.find("size")

    width = int(size.findtext("width"))
    height = int(size.findtext("height"))

    records = []

    for obj in root.findall("object"):
        class_name = obj.findtext("name")

        bbox = obj.find("bndbox")
        xmin = int(float(bbox.findtext("xmin")))
        ymin = int(float(bbox.findtext("ymin")))
        xmax = int(float(bbox.findtext("xmax")))
        ymax = int(float(bbox.findtext("ymax")))

        records.append(
            {
                "filename": filename,
                "width": width,
                "height" : height,
                "class": class_name,
                "xmin": xmin,
                "ymin": ymin,
                "xmax": xmax,
                "ymax": ymax,
            }
        )

    return records
