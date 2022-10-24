from asyncio import constants
import code
from distutils.version import Version
from ensurepip import version
import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrimg.png")

link = input("Coloque um link para gerar o QRcode: ")

generate_qrcode(link)

print("Seu QRCode já está pronto em seu dispositivo!")