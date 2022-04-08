#Delete error files; avoid using rm

import glob
import os
for ent in glob.glob("*err"):
    os.remove(ent)

for ent in glob.glob("*out"):
    os.remove(ent)
