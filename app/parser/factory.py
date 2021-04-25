"""Factory returning proper parser"""

from ..image.color_format import (PixelPlane, PixelFormat, ColorFormat)
from .rgb import ParserRGBA
from .yuv import (ParserYUV420, ParserYUV422)


class ParserFactory:
    """Parser factory"""
    @staticmethod
    def create_object(color_format):
        """Get parser for provided color format.

        Keyword arguments:
            color_format: instance of ColorFormat

        Returns: instance of parser
        """
        mapping = {}
        if color_format.pixel_plane == PixelPlane.PACKED:
            mapping = {
                PixelFormat.RGBA: ParserRGBA,
                PixelFormat.BGRA: ParserRGBA,
                PixelFormat.YUYV: ParserYUV422,
                PixelFormat.UYVY: ParserYUV420,
            }
        elif color_format.pixel_plane == PixelPlane.SEMIPLANAR:
            mapping = {
                PixelFormat.YUV: ParserYUV420,
                PixelFormat.YVU: ParserYUV420,
            }

        proper_class = mapping.get(color_format.pixel_format)
        return proper_class()
