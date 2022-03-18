import qrcode    #pip install qrcode
qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)

data = input('URL or Text >> ')
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="cyan", back_color="black")
path = input('Enter QR image name: ')
img.save(f"{path}.png")
