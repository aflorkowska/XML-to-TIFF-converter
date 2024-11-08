from pathlib import Path
from argparse import ArgumentParser
from config import AnnotationDataType
from convert_annotations_to_mask import generate_masks_from_annotations

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--annotations_dir', type=str, default=None, help="Path to dir with annotations.") 
    parser.add_argument('--images_dir', type=str, default=None, help="Path to dir with images.") 
    parser.add_argument('--output_dir', type=str, default=None, help="Path to output dir for saving generated masks.") 
    parser.add_argument("--xml_data_type", type=str, choices=[type.value for type in AnnotationDataType], help="Choose xml annotation data type, wheather coordinates in xml files are given in pixels at lvl 0 (pixels), or in units (units).")
    args = parser.parse_args()

    generate_masks_from_annotations(Path(args.annotations_dir), 
                                    Path(args.images_dir),
                                    Path(args.output_dir),
                                    AnnotationDataType(args.xml_data_type))
        
