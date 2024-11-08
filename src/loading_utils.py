import os
import pyvips
from pathlib import Path
from typing import Dict

def load_image(path: Path ) -> pyvips.Image:
    """
    Load WSI image using PyVips library.  

    Parameters
    ----------
    path : Path
        Path to the specific file.

    Returns
    -------
    pyvips.Image
    """
    img = pyvips.Image.new_from_file(str(path), access="sequential")
    if img.bands > 3:
        img = img.flatten(background=255)
    return img

# TODO
# def get_pixel_size_scalling_factor(img_path : Path) -> Tuple[float, float]:
#     """
#     Get pixel size at level 0. 

#     Parameters
#     ----------
#     img_path : Path
#         Path to the image.

#     Returns
#     -------
#     Tuple[float, float]
#         Tuple of pixel size.

#     Raises
#     ------
#     ValueError : Image '{img_path}' can not be opended.
#     """
#     slide, is_open = open_slide(img_path)
#     if not is_open:
#         raise ValueError(f"Image '{img_path}' can not be opended.")
#     slide_properties = slide.properties
#     factors = (float(slide_properties['openslide.mpp-x']), float(slide_properties['openslide.mpp-y']))
#     slide.close()
#     return factors

def find_files_with_extension(root_dir : Path, 
                              extensions : list[str]) -> list[Path]:
    """
    Search root dir to find files with declared extensions.

    Parameters
    ----------
    root_dir : Path
        Path to the main dir you want to be searched.
    extensions : list of string
        List of desirable files' extensions.

    Returns
    -------
    list[Path]
        List of all found files with corresponding extension.

    Raises
    ------
    ExceptionType
        FileNotFoundError: If rootDir was not found.
    """
    if not os.path.exists(root_dir):
        raise FileNotFoundError(f"Dir '{root_dir}' does not exist.")

    file_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            for extension in extensions:
                if filename.endswith(extension):
                    file_paths.append(Path(os.path.join(dirpath, filename)))
    
    return file_paths

def map_images_to_annotations(img_paths : list[Path], 
                              annotation_paths : list[Path]) -> list[Dict[str, Path]]:
    """
    Map images and their corresponding annotations.

    Parameters
    ----------
    img_paths : list[Path]
        List of all found images' paths.
    annotation_paths : list[Path]
        List of all found annotations' paths.

    Returns
    -------
    list[dict]
        List of dictionaries containing all found pairs: paths to corresponding images and annotations.

    Raises
    ------
    ExceptionType
        ValueError: If at least one of the lists is empty.
    """
    if not img_paths or not annotation_paths:
        raise FileNotFoundError(f"Input list is empty")
    
    mappedData = []
    for img_path in img_paths:
        for annotation_path in annotation_paths:
            if str(img_path.stem) in str(annotation_path):
                annotation_paths.remove(annotation_path)
                mappedData.append({'image' : img_path, 
                                   'annotation' : annotation_path })
                break
    return mappedData
