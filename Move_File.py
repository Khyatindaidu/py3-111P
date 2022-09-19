import shutil 
import os 

from_dir = "/Users/khyatii/Downloads"
to_dir = "/Users/khyatii/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files :
    name,extentsion=os.path.splitext(file_name)
    