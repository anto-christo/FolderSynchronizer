import os
import shutil
import os.path
import numpy as np

currentPath = os.getcwd()
dirs = [d for d in os.listdir() if os.path.isdir(os.path.join( d))]
print (dirs)
slash = "\\"

listToArray = np.asarray(dirs)
