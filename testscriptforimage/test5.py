import numpy as np
import cv2
import re
import os

def hex_txt_to_png(
    txt_file,
    width=256,
    height=144,
    output_png="fingerprint.png"
):
    # Read file safely
    with open(txt_file, "r", errors="ignore") as f:
        text = f.read()

    # Extract hex bytes: supports 0xAA, AA, aa, mixed separators
    hex_values = re.findall(r'\b(?:0x)?([0-9A-Fa-f]{2})\b', text)

    if not hex_values:
        raise ValueError("No HEX bytes found in the file.")

    data_bytes = bytearray(int(h, 16) for h in hex_values)
    print("Parsed bytes:", len(data_bytes))

    expected_size = width * height
    if len(data_bytes) < expected_size:
        raise ValueError(
            f"Expected {expected_size} bytes, got {len(data_bytes)}"
        )

    # Create grayscale image
    img = np.frombuffer(data_bytes[:expected_size], dtype=np.uint8)
    img = img.reshape((height, width))

    # Save PNG in local folder
    cv2.imwrite(output_png, img)
    print(f"✅ PNG image saved locally as: {output_png}")

    return img


# ---------- RUN ----------
# Put fingerprint.txt in the SAME folder as this script
hex_txt_to_png("fingerprint.txt")
