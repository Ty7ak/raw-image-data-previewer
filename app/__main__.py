#!/usr/bin/env python
import cv2 as cv
"""Raw image data previewer - terminal functionality."""

import argparse
import os
from .core import (load_image, get_displayable)
from .image.color_format import AVAILABLE_FORMATS
from .gui import MainWindow

parser = argparse.ArgumentParser(
    prog=__package__,
    description="preview raw data as an image of chosen format")
parser.add_argument("FILE_PATH", help="file containing raw image data")
parser.add_argument("-c",
                    "--color_format",
                    choices=AVAILABLE_FORMATS.keys(),
                    default=list(AVAILABLE_FORMATS.keys())[0],
                    help="target color format (default: %(default)s)")
parser.add_argument("-r",
                    "--resolution",
                    metavar=("width", "height"),
                    type=int,
                    nargs=2,
                    default=[600, 600],
                    help="target resolution (default: %(default)s)")

args = vars(parser.parse_args())

if not os.path.isfile(args["FILE_PATH"]):
    raise Exception("Given path does not lead to a file")

#img = load_image(args["FILE_PATH"], args["color_format"], args["resolution"])
app = MainWindow(args)
app.mainloop()
"""
cv.imshow(args["FILE_PATH"], get_displayable(img))
cv.waitKey(0)
cv.destroyAllWindows()
"""
