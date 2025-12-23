import qrcode

qr = qrcode.QRCode(
    version=4,
    box_size=10,
    border=4,
)

qr.add_data("https://www.w3schools.com/python/python_class_methods.asp")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("mycode.png")
