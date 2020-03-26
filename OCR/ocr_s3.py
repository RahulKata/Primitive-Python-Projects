import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("image.jpg") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
im.show()
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
text
  
for j in search(text, tld="co.in", num=10, stop=1, pause=2): 
    print(j) 
