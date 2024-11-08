from enum import Enum

WSI_EXTs = [".tiff", ".tif", ".mrxs"]
ANNOTATION_EXTs = [".xml"]

class AnnotationDataType(Enum):
    PIXELS_LVL_0 = "pixels"
    UNITS_LVL_0 = "units"

