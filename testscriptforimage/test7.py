import numpy as np
from PIL import Image
import re
import math
import os

def hex_file_to_png(hex_file, output_png="output.png"):
    # Read file
    with open(hex_file, "r") as f:
        text = f.read()

    # Extract hex bytes (supports: 0xFF, FF, space separated)
    hex_bytes = re.findall(r'(?:0x)?([0-9A-Fa-f]{2})', text)

    if not hex_bytes:
        raise ValueError("No HEX bytes found in file")

    # Convert hex → pixel values
    pixels = np.array([int(b, 16) for b in hex_bytes], dtype=np.uint8)

    # Auto-detect square image
    total = pixels.size
    side = int(math.sqrt(total))

    if side * side != total:
        raise ValueError(
            f"Total bytes = {total}. Not a perfect square.\n"
            f"Specify WIDTH and HEIGHT manually."
        )

    image = pixels.reshape((side, side))

    # Save PNG
    Image.fromarray(image, mode="L").save(output_png)

    print(f"✅ PNG saved at: {os.path.abspath(output_png)}")
    print(f"🖼 Image size: {side} x {side}")

# ===== RUN =====
fingerprint="hex_log_20251212_162843.txt"
hex_file_to_png(fingerprint, "fingerprint.png")
