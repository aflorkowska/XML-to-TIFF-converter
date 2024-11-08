from argparse import ArgumentParser
from config import AnnotationDataType
from convert_annotations_to_mask import generate_masks_from_annotations

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--annotations_dir', type=str, default=None, help="Path to dir with annotations.") 
    parser.add_argument('--images_dir', type=str, default=None, help="Path to dir with images.") 
    parser.add_argument('--output_dir', type=str, default=None, help="Path to output dir for saving generated masks.") 
    parser.add_argument("--xml_data_type", type=str, choices=[type.name for type in AnnotationDataType], help="Choose xml annotation data type, wheather coordinates in xml files are given in pixels at lvl 0 (PIXELS_LVL_0), or in units (UM_LVL_0).")
    args = parser.parse_args()

    generate_masks_from_annotations(args.annotations_dir, 
                                    args.images_dir,
                                    args.output_mask_dir,
                                    args.xml_data_type)
        
