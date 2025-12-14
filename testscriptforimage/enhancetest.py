import numpy as np
import cv2
import re

def parse_bytes(text):
    values = []

    # HEX (0xAA or AA)
    for h in re.findall(r'\b(?:0x)?[0-9A-Fa-f]{2}\b', text):
        values.append(int(h.replace("0x",""), 16))

    # DECIMAL (0–255)
    for d in re.findall(r'\b\d{1,3}\b', text):
        v = int(d)
        if 0 <= v <= 255:
            values.append(v)

    return bytearray(values)


def hex_txt_to_image(txt_file, width=256, height=144, output="fingerprint8.png"):
    with open(txt_file, "r", errors="ignore") as f:
        text = f.read()

    data_bytes = parse_bytes(text)
    print("Parsed bytes:", len(data_bytes))

    expected = width * height
    if len(data_bytes) < expected:
        raise ValueError(
            f"Expected {expected} bytes, got {len(data_bytes)}"
        )

    img = np.frombuffer(data_bytes[:expected], dtype=np.uint8)
    img = img.reshape((height, width))
    

    cv2.imwrite(output, img)
    print(f"✅ Image saved as {output}")
    

    return img


# -------- RUN --------
fingerprint="hex_log_20251212_162902.txt"
hex_txt_to_image(fingerprint)
