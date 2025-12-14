import numpy as np
import cv2
from tkinter import Tk, filedialog

def load_txt_file(title="Select TXT Dump"):
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title=title,
        filetypes=[("Text files", "*.txt")]
    )
    return file_path

def parse_raw_image(txt_file):
    with open(txt_file, "r") as f:
        tokens = f.read().replace(",", " ").split()

    data_bytes = bytearray(int(tok, 16) for tok in tokens if tok.startswith("0x"))
    print("length of data bytes - ", len(data_bytes))
    raw_image = bytearray()
    i = 0
    raw_image += data_bytes[0:36864]

    print(raw_image)
    print("length of fimage - ", len(raw_image))

    if len(raw_image) == 36864:
        img = np.frombuffer(raw_image, dtype=np.uint8).reshape((144, 256))
        print(f"[{txt_file}] image detected (144x256)")
    else:
        raise ValueError(f"Unexpected image size: {len(raw_image)} bytes")

    return img
"""
def match_fingerprints(img1, img2):
    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        print("Error: Could not detect enough features")
        return

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    print("Number of ORB matches:", len(matches))
    if len(matches) > 30:  # threshold (tune)
        print("Fingerprint MATCHED ✅")
    else:
        print("Fingerprint NOT MATCHED ❌")

    match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None, flags=2)
    cv2.imshow("Matches", match_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# -------- Main Program --------
print("Select first fingerprint TXT file")
file1 = load_txt_file("Select First Fingerprint TXT")
img1 = parse_raw_image(file1)
cv2.imwrite("finger1.bmp", img1)

print("Select second fingerprint TXT file")
file2 = load_txt_file("Select Second Fingerprint TXT")
img2 = parse_raw_image(file2)
cv2.imwrite("finger2.bmp", img2)

match_fingerprints(img1, img2)"""
