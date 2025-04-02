import os
import send2trash


# script to delete everything except the files with numbers only

path = "./CC"

files = os.listdir(path)

def check():
    path = "./CC"
    files = os.listdir(path)
    for i in files:
        tt = os.listdir(f"{path}/{i}")
        for j in tt:
            ll = os.listdir(f"{path}/{i}/{j}")
            for l in ll:
                check = True
                for char in list(l.split(".")[0]):
                    try:
                        if type(int(char)) == int:
                            continue
                    except:
                        check = False
                        continue
                if check == True:
                    print(l)
                else:
                    send2trash.send2trash(f"{path}/{i}/{j}/{l}")


check()
