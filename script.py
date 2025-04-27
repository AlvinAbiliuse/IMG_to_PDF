import os
import shutil
import sys


curr = os.listdir(sys.argv[1])
curr.sort()
print("\n".join(curr))

for i in curr:
    first = i.split(" Chapter")[0]
    print(f"Moving {i} to {first}")
    shutil.move(f"{sys.argv[1]}/{i}", 
                f"{sys.argv[1]}/{first}/{i}")
