from PIL import Image
import pytesseract

img_doc = Image.open('qt_1.jpg') # 'C:\\users\\uncleengineer\\desktop\\basic ocr\\eng_text.png'
ocr_text = pytesseract.image_to_string(img_doc,lang='tha+eng')
print(ocr_text)