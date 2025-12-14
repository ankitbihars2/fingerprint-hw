#hex 2 img
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


def hex_txt_to_image(txt_file,output, width=256, height=144, ):
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
import os

base_dir = r"D:\fingerprint-iot-device\labelldata\ankits2-20251213T090227Z-1-001"

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)

    if os.path.isdir(folder_path):
        for subfolder in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder)

            if os.path.isdir(subfolder_path):
                for file in os.listdir(subfolder_path):
                    file_path = os.path.join(subfolder_path, file)
                    print(file_path)

from pathlib import Path

def process_fingerprint_dataset(root_dir):
    root_dir = Path(root_dir)

    for side in ["left", "right"]:
        side_path = root_dir / side
        if not side_path.exists():
            continue

        for finger_dir in side_path.iterdir():
            if finger_dir.is_dir():
                for file in finger_dir.iterdir():
                    if file.suffix.lower() == ".txt":
                        output_png = file.with_suffix(".png")

                        print(f"Converting: {file}")
                        hex_txt_to_image(file, output_png)
#for folder process
def process_fingerprint_dataset(root_dir):
    root_dir = Path(root_dir)

    for side in ["left", "right"]:
        side_path = root_dir / side
        if not side_path.exists():
            continue

        for finger_dir in side_path.iterdir():
            if finger_dir.is_dir():
                for txt_file in finger_dir.glob("*.txt"):
                    output_png = txt_file.with_suffix(".png")
                    hex_txt_to_image(txt_file, output_png)
#function call
if __name__ == "__main__":
    dataset_path = r"D:\fingerprint-iot-device\labelldata\ankits2-20251213T090227Z-1-001\ankits2"
    process_fingerprint_dataset(dataset_path)
                        