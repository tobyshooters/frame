import sys
from PIL import Image
from pyzbar.pyzbar import decode

target = sys.argv[1]
target = Image.open(target)

for output in decode(target):
    print(output.data.decode())

