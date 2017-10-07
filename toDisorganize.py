import os
import shutil
import os.path
import numpy as np

currentPath = os.getcwd()
dirs = [d for d in os.listdir() if os.path.isdir(os.path.join( d))]
print (dirs)
slash = "\\"

listToArray = np.asarray(dirs)

for x in listToArray:
    oldpath = currentPath + slash + x
    print(oldpath)
    directoryArray = os.listdir(x)
    print (directoryArray)
    for i in directoryArray:
        shutil.move(oldpath + slash + i,currentPath + slash +i)


