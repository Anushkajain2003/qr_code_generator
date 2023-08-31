import qrcode
qr=qrcode.QRCode(
    version=10,
    box_size=5,
    border=5
)

data="https://github.com/Anushkajain2003"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('Github.png')