import qrcode

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    version=4,
    box_size=12,
    border=10,
)

qr.add_data("http.//www.github.com")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("advance.png")
