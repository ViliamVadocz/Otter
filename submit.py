import os
from zipfile import ZipFile

if __name__ == "__main__":
    with ZipFile("Otter.zip", "w") as zip_obj:
        # Zip specific files.
        zip_obj.write("README.md")
        zip_obj.write("requirements.txt")
        # Zip the src directory.
        for folder, subfolders, file_names in os.walk("src"):
            for file_name in file_names:
                file_path = os.path.join(folder, file_name)
                print(file_path)
                zip_obj.write(file_path)
