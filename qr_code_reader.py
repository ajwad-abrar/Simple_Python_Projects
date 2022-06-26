import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

decodeQR = decode(Image.open('qr_code.png'))

print(decodeQR[0].data.decode('ascii'))
