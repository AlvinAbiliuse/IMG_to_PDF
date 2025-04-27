#! ./env/bin/python3

import os
import shutil
import sys


curr = os.listdir(sys.argv[1])
curr.sort()

for i in curr:
    if i.endswith(".pdf"):
        first = i.split(" Chapter")[0]
        if os.path.isdir(f"./{sys.argv[1]}/{first}") == False:
            os.makedirs(f"./{sys.argv[1]}/{first}");
        shutil.move(f"./{sys.argv[1]}/{i}", 
                f"./{sys.argv[1]}/{first}/{i}")
