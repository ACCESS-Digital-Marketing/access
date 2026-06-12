import os

folder_path = r"E:\Projats\P-1\Photo\G"

files = os.listdir(folder_path)
files.sort()

counter = 1

for file in files:
    old_path = os.path.join(folder_path, file)

    if os.path.isfile(old_path):
        ext = os.path.splitext(file)[1]
        new_name = f"g-{counter}{ext}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        counter += 1

print("Done renaming files!")