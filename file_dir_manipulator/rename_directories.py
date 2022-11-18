import os
import zipfile

basedir = './'
for fn in os.listdir(basedir):
    if not os.path.isdir(os.path.join(basedir, fn)):
        continue # Not a directory
    else:
        n_fn = fn.replace(':','_')
        os.rename(fn, n_fn)

print("completed")
