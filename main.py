from PIL import Image,ImageEnhance,ImageFilter
import os;

plik = './imgs'
retusz = './reimgs'

for filename in os.listdir(plik):
    img = Image.open(f"{plik}/{filename}")
    print("Filtr do zdjęcia: " + filename)
    print("1.Blur")
    print("2.Contour")
    print("3.Detail")
    print("4.Sharpen")
    print("5.Smooth")
    i = input("jaki filtr wariacie?")
    match i:
        case '1':
            edit = img.filter(ImageFilter.BLUR)
            cleanName = os.path.splitext(filename)[0]
            edit.save(f'{retusz}/{cleanName}_edited.png')
        case '2':
            edit = img.filter(ImageFilter.CONTOUR)
            cleanName = os.path.splitext(filename)[0]
            edit.save(f'{retusz}/{cleanName}_edited.png')
        case '3':
            edit = img.filter(ImageFilter.DETAIL)
            cleanName = os.path.splitext(filename)[0]
            edit.save(f'{retusz}/{cleanName}_edited.png')
        case '4':
            edit = img.filter(ImageFilter.SHARPEN)
            cleanName = os.path.splitext(filename)[0]
            edit.save(f'{retusz}/{cleanName}_edited.png')
        case '5':
            edit = img.filter(ImageFilter.SMOOTH)
            cleanName = os.path.splitext(filename)[0]
            edit.save(f'{retusz}/{cleanName}_edited.png')