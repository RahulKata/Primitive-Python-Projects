import barcode
from barcode.writer import ImageWriter

# =============================================================================
# make sure to 
# * pip install better_profanity*
# before you proceeeeeeeed
# Reference: " https://pypi.org/project/python-barcode/ "
# =============================================================================


# print(barcode.PROVIDED_BARCODES)

EAN = barcode.get_barcode_class('ean13')  
ean = EAN('1234567890123')
qr = ean.save('ean13_mark1')  #this generates a .svg file

ean = EAN('1234567890123', writer=ImageWriter())
qr1 = ean.save('ean13_mark2')   #this generates a .png file

ISBN = barcode.get_barcode_class('isbn13')
isbn = ISBN('978561654156',writer = ImageWriter())
qr2 = isbn.save('isbn_mark1')
  
#all the files are saved in the same directory