from pdf2image import convert_from_path

images = convert_from_path('qt_1.pdf',dpi=300)

for i,img in enumerate(images):
    img.save(f'qt_{i+1}.jpg','JPEG')