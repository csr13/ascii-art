"""
Some things needed
"""
import os

THIS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))

IMG_DIR = os.path.join(THIS_DIR, "images")

OUT_DIR = os.path.join(THIS_DIR, "output")

DATA_DIR = os.path.join(THIS_DIR, "data")

PARSER_ARGS_HELP = {
    "color" : (
        "[INFO] The color for the picture, represented by RGB specification, eg: --color "
        "255 255 255 -- defaults to 0 0 0 (black)"
    ),
    "char_width" : "[INFO] The width of the characters, eg: --char-width 18 -- defaults to 9",
    "char_height" : "[INFO] The height of the character, eg: --char-height 9 -- defaults to 9",
    "scale_factor" : "[INFO] Scale factor of the image, eg: 0.20 -- defaults to 0.18",
    "language" : "[INFO] Language for the characters, eg: arabic -- defaults to standard",
    "font_size" : "[INFO] Font size for unicode, cyrillic and arabic languages only.",
    "stroke_width" : "[INFO] The value for the width of the text stroke",
    "coords" : "[INFO] Target coordinates to crop from the image",
    "image_path" : "[INFO] Location of the image, eg : /home/xxx/wap.jpeg"
}

META_CHARS = {
    "arabic" : "وهنملكقفغعطضصشسزرذدخحجثتبا",
    "cyrillic" : u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяіѣѳ",
    "standard" : "$@B%8&WM#*oahkbdpqwmZO0QLC763YXzc/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."[::-1],
}
