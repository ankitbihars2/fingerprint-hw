"""import os

root_dir = "D:\fingerprint-iot-device\labelldata\ankits2-20251213T090227Z-1-001"   # top-level folder

for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)"""
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
                    
import img_generator
for i in file_path:
   hex_txt_to_image(i,i.png) 


