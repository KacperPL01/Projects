import pyqrcode

data = input("Enter the text or link to generate QR code: ")

qr = pyqrcode.create(data)

qr.svg('E:\\Python Scripts\\QR_Code\\qr_code.svg', scale = 10)
