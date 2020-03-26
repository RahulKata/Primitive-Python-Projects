import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("image.jpg") 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp1.jpg')
im.show()
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)
