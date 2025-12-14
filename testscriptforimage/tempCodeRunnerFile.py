import numpy as np
import cv2
from tkinter import Tk, filedialog

def select_txt_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Select Fingerprint HEX TXT File",
        filetypes=[("Text files", "*.txt")]
    )

def hex_txt_to_image(txt_file):
    with open(txt_file, "r") as f:
        tokens = f.read().replace(",", " ").split()

    # Extract hex bytes like 0x1A
    data_bytes = bytearray(
        int(tok, 16) for tok in tokens if tok.startswith("0x")
    )

    print("Total hex bytes:", len(data_bytes))

    IMAGE_SIZE = 144 * 256  # 36864 bytes
    raw_image = data_bytes[:IMAGE_SIZE]

    if len(raw_image) != IMAGE_SIZE:
        raise ValueError(f"Expected {IMAGE_SIZE} bytes, got {len(raw_image)}")

    # Convert to grayscale image
    img = np.frombuffer(raw_image, dtype=np.uint8).reshape((144, 256))
    return img

# ---------- Main ----------
txt_file = select_txt_file()
img = hex_txt_to_image(txt_file)

cv2.imwrite("fingerprint.bmp", img)
print("✅ Fingerprint image saved as fingerprint.bmp")

cv2.imshow("Fingerprint Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
