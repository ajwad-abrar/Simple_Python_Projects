import pyqrcode

qrcode = pyqrcode.create("Ajwad Abrar \najwadabrar@iut-dhaka.edu")

qrcode.png('qr_code.png', scale=8)