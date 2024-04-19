import cv2
from PIL import Image
import numpy as np
import qrcode

def encode(url, x, y, w, h):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    url = (
        f"{url}"
        f"?x={x}"
        f"&y={y}"
        f"&w={w}"
        f"&h={h}"
    )
    qr.add_data(url)
    qr.make(fit=True)

    ref = qr.make_image(
        fill_color="black",
        back_color="white"
    )
    s = min(w, h)
    ref = ref.resize((s, s))
    ref = 255 * np.asarray(ref)

    mask = 255 * np.ones((h, w), dtype=np.int32)
    mask[:s, :s] = ref

    return mask


img = Image.open("001.png")
img = np.asarray(img)

target = Image.open("002.png")
tW, tH = target.size
W = 120
H = int(W * tH / tW)
target = target.resize((W, H))

# Stick image in location!
x, y, w, h = 320, 270, W, H
img[y:y+h, x:x+w] = np.asarray(target)
Image.fromarray(img).save("montage.png")

# Represent data!
ref = encode("002.png", x, y, w, h)
img[y:y+h, x:x+w] = ref[:, :, np.newaxis]
Image.fromarray(img).save("format.png")

