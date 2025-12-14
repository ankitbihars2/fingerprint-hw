import binascii
import re
from PIL import Image

def hex_to_png(hex_file, png_file, width, height):
    with open(hex_file, "r") as f:
        raw = f.read()

    cleaned = raw.replace("0x", "").replace(" ", "").replace(",", "").replace("\n", "")
    hex_data = re.sub(r'[^0-9A-Fa-f]', '', cleaned)

    try:
        img_bytes = binascii.unhexlify(hex_data)
    except Exception as e:
        print("Hex decode error:", e)
        return

    expected = width * height
    actual = len(img_bytes)

    print("Expected bytes:", expected)
    print("Actual bytes:", actual)

    if actual < expected:
        print("Error: Not enough data for image!")
        return

    img = Image.frombytes("L", (width, height), img_bytes[:expected])
    img.save(png_file)
    print("PNG saved as:", png_file)

hex_to_png(
    hex_file="hex_log_20251212_162843.txt",
    png_file="fingerprint_output.png",
    width=256,
    height=288
)