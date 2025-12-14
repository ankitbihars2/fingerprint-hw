import numpy as np
import cv2

def hex_txt_to_image(txt_file, width=256, height=144, out_file="fingerprint.bmp"):
    with open(txt_file, "r") as f:
        tokens = f.read().replace(",", " ").split()

    # Convert hex tokens (0x..) to bytes
    data = bytearray(int(t, 16) for t in tokens if t.startswith("0x"))

    expected_size = width * height
    if len(data) < expected_size:
        raise ValueError(f"Not enough data: {len(data)} bytes (need {expected_size})")

    # Create image
    img = np.frombuffer(data[:expected_size], dtype=np.uint8)
    img = img.reshape((height, width))

    # Save image
    cv2.imwrite(out_file, img)
    print(f"✅ Image saved as {out_file}")

    return img


# --------- USAGE ----------
hex_txt_to_imageimport numpy as np
import cv2

def hex_txt_to_image(txt_file, width=256, height=144, out_file="fingerprint.bmp"):
    with open(txt_file, "r") as f:
        tokens = f.read().replace(",", " ").split()

    # Convert hex tokens (0x..) to bytes
    data = bytearray(int(t, 16) for t in tokens if t.startswith("0x"))

    expected_size = width * height
    if len(data) < expected_size:
        raise ValueError(f"Not enough data: {len(data)} bytes (need {expected_size})")

    # Create image
    img = np.frombuffer(data[:expected_size], dtype=np.uint8)
    img = img.reshape((height, width))

    # Save image
    cv2.imwrite(out_file, img)
    print(f"✅ Image saved as {out_file}")

    return img


# --------- USAGE ----------
hex_txt_to_image("fingerprint.txt")

