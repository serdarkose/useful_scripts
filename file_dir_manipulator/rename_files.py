import os
import glob

txtfiles = []
for file in glob.glob("*.png"):
    txtfiles.append(file)

for file in txtfiles:
    n_file = file.replace(':','_')
    #print(f"{file} -> {n_file}")
    os.rename(file, n_file)

print("completed")
