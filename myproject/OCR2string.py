# -*- coding: utf-8 -*-


import sys
import time
from PIL import Image
import pytesseract

image=Image.open(r'/home/alex/Test.png')
code = pytesseract.image_to_string(image)
print(code)