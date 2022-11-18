import os
import glob

files = []
for file in glob.glob("*.png"):
    files.append(file)

for file in files:
    n_file = file.replace(':', '_')
    # print(f"{file} -> {n_file}")
    os.rename(file, n_file)

print("completed")
