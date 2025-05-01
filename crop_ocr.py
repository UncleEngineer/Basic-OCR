from PIL import Image
import pytesseract
from PIL import Image
import os

PATH = r'C:\Users\Asus\Desktop\RPA 2025\Basic OCR'

listfiles = os.listdir(PATH)
# print(listfiles)

filter_files = []

for f in listfiles:
    img = os.path.join(PATH,f)
    #print(img)
    if f[:2] == 'qt' and f[-3:] == 'jpg':
        filter_files.append(img)

print(filter_files)


total = 0

for f in filter_files:
    im = Image.open(f)

    # TITLE OF QT
    left = 340
    top = 1305
    right = 1233
    bottom = 1392
    im1 = im.crop((left, top, right, bottom))

    # TOTAL OF QT
    left = 2045
    top = 2389
    right = 2295
    bottom = 2464
    im2 = im.crop((left, top, right, bottom))

    ocr1 = pytesseract.image_to_string(im1,lang='tha+eng').strip()

    ocr2 = pytesseract.image_to_string(im2,lang='tha+eng').strip()

    print(ocr1, ocr2)

    total += float(ocr2.replace(',',''))
    print('------------')

print('TOTAL:',total)