import datetime
import hashlib
import os
import math
import random
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.append("..")

from settings import META_CHARS, THIS_DIR


def convert_opencv2_to_pill(image):
    color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image=Image.fromarray(color_coverted)
    return pil_image


def convert_pill_to_opencv2(image):
    numpy_image=np.array(image, dtype="uint8")  
    opencv_image=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
    return opencv_image


def valid_location(image_name, delete=False):
    path = os.path.join(
        THIS_DIR, 
        "images", 
        image_name
    )
    if os.path.exists(path):
        if delete:
            choice = str(input("[INFO] Image {} exists, delete? y/n: ".format(path)))
            if choice.lower() == "y":
                os.unlink(path)
            else:
                raise FileExistsError("[INFO] {} exists, pick another name.".format(path)) from None
    return image_name


def valid_out_location(image_name, delete=False):
    path = os.path.join(
        THIS_DIR, 
        "output", 
        image_name
    )
    if os.path.exists(path):
        if delete:
            choice = str(input("[INFO] Image {} exists, delete? y/n: ".format(path)))
            if choice.lower() == "y":
                os.unlink(path)
            else:
                raise FileExistsError("[INFO] {} exists, pick another name.".format(path)) from None
    return image_name


def valid_url(url):
    try:
        resp = requests.get(url)
    except Exception as error:
        raise ValueError(str(error))
    if resp.status_code not in [x for x in range(200, 299+1)]:
        raise ValueError("[INFO] Url not reachable") from None
    return url


def shred(loca):
    for f in os.listdir(loca):
        if f.endswith(".txt"):
            print("[INFO] Shredding {}".format(
                os.path.join(loca, f)
                )
            )
            os.unlink(os.path.join(loca, f))


def shred_out(loca):
    if len(os.listdir(loca)) == 0:
        return False
    for f in os.listdir(loca):
        print("[INFO] Removing {}".format(
                os.path.join(loca, f)
            )
        )
        os.unlink(os.path.join(loca, f))


def hash_nom(nom, fmt):
    t1 = nom.replace("jpg", "").encode()
    t2 = hashlib.sha256(t1).hexdigest()
    if fmt == "txt":
        return "%s%s" % (t2, ".txt")
    elif fmt == "jpeg":
        return "%s%s" % (t2, ".jpeg")
    elif fmt == "png":
        return "%s%s" % (t2, ".png")
    raise NotImplementedError()


def morceau_de_toi(piece, interval, char_list=None):
    u = math.floor(piece * interval)
    if char_list is not None:
        return char_list[u]
    return META_CHARS["standard"][u]


def random_timestamp():
    return str(
        datetime.datetime.timestamp(
            datetime.datetime.now()
        )
    ).replace(".", "")


def swap(toi, random_colors=False, selected_colors=False, **kwargs):
    """
    kwargs = {
        'scale_factor' : <float>,
        'char_width'   : int,
        'char_length'  : int,
        'color' : <tuple r, g, b>
        'fmt' : <str> format
    }
    """
    scale_factor = kwargs["scale_factor"]
    char_width = kwargs["char_width"]
    char_height = kwargs["char_heigth"]
    fmt = kwargs["fmt"]
    
    if 'color' in kwargs:
        color = kwargs["color"]
    else:
        color = (0, 0, 0)
    
    interval = len(list(META_CHARS["standard"]))/256
    loca_drop = os.path.join(THIS_DIR, "output")
    text_file = os.path.join(loca_drop, hash_nom(random_timestamp(), "txt"))
    
    try:
        with open(text_file, "w", encoding="utf-8") as ts:
            
            wh = toi.size
            w1 = wh[0]
            h1 = wh[1]
            
            w2 = int(scale_factor * (w1 / 2))
            h2 = int(scale_factor * (h1 / 2))
            h2 = int(h2 * (char_width / char_height))
            toi = toi.resize((w2, h2), Image.NEAREST)
            
            wh3 = toi.size
            w3 = wh3[0]
            h3 = wh3[1]
            
            pixel = toi.load()
            w4 = char_width * w3
            h4 = char_height * h3
            votre_cadre = Image.new('RGB', (w4, h4), color=color)
            noir_et_blanc = ImageDraw.Draw(votre_cadre)
            
            for toiy in range(h4):
                for bellex in range(w4):
                    try:
                        pixel[bellex, toiy]
                    except IndexError as error:
                        continue
                    
                    try:
                        r, g, b = pixel[bellex, toiy]
                    except (ValueError, TypeError):
                        r, g, b, a = pixel[bellex, toiy]

                    u = int(r/3 + g/3 + b/3)
                    pixel[bellex, toiy] = (u, u, u)
                    text = morceau_de_toi(u, interval)
                    ts.write(text)
                    h5 = toiy * char_height
                    w5 = bellex * char_width
                    
                    if random_colors:
                        fill = (
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255)
                        )
                    else:
                        fill = (r, g, b)
                    
                    if selected_colors:
                        fill = kwargs["select_colors"]
                    elif not random_colors:
                        fill = (r, g, b)
                    
                    noir_et_blanc.text(
                        (w5, h5), 
                        text, 
                        fill=fill,
                    )
                
                ts.write("\n")
            vous = os.path.join(
                loca_drop,
                hash_nom(text_file, fmt)
            )
    except Exception as error:
        raise error
    return votre_cadre, vous, wh


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)
