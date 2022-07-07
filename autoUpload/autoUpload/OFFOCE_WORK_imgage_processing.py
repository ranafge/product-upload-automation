from PIL import Image
import glob, os
import numpy as np
import subprocess

for f in glob.glob('/home/py/faiaz/Dp/Spices/*'):
     foo = Image.open(f)
     original_filename = os.path.basename(foo.filename.split(".")[0])
     resizeFile = foo.resize((420,420), Image.ANTIALIAS)

     resizeFile.save(original_filename+ ".png" , optimize=True, quality=True)


print('Finished')












