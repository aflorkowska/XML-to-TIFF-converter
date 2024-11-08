# XML-to-TIFF-converter

This repo contains converter for histopatological data, saved in pyramidal files. It enables generating mask from xml annotations about the image, both for ground_truth and background masks. 
It is also a part of [HistopathologyAugmentationResearch repository](https://github.com/Jarartur/HistopathologyAugmentationResearch), that is usufull eg. for obtaining xaml annotations.

### Instalation

1. Install all libraries using commend: `pip install -r requirements.txt`
2. Then, using command `pip list` check if the packages were installed succesfully.

### Usage

1. Copy this repo with use of `git clone https://github.com/aflorkowska/XML-to-TIFF-converter.git`
2. Go to the repo's folder `cd <path-to-repo>`
3. Open terminal and run `python main.py --annotations_dir <path> --images_dir <path> --output_dir <path> --xml_data_type <pixels or units>`