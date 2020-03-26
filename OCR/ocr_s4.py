import requests
import sys
import webbrowser
import bs4
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("U.png") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp3.jpg')
print("The processed image is: ")
im.show()
text = pytesseract.image_to_string(Image.open('temp3.jpg'))
print(text)
print()
print("Now lets do something more with the scanned text! ")
print("Why not google it !!")
l=[print(".......") for i in range(0,10)]
res=requests.get('https://google.com/search?q='+''.join(text))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, "html.parser")
linkElements=soup.select('.r a')
linkToOpen=min(5,len(linkElements))
for i in range(linkToOpen):
     webbrowser.open('https://google.com'+linkElements[i].get('href'))
     
