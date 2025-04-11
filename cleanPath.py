#! ./env/bin/python3

import os
import send2trash



def check(a):
    path = a
    files = os.listdir(path)
    for i in files:
        check = True
        for char in list(i.split(".")[0]):
            try:
                if type(int(char)) == int:
                    continue
            except:
                check = False
                continue
        if i.endswith(".cbz") or i.endswith(".zip"):
            check = True

        if check == True:
            continue
        else:
            send2trash.send2trash(f"{path}/{i}")

def cleanPath(path):
    test = path.split("-");
    print(f"Cleaning {path} \n")
    for i in os.listdir(path):
        try:
            if i.split(".")[-1] == "html":
                send2trash.send2trash(f"./{path}/{i}")
            elif os.path.isdir(f"{path}/{i}") == True:
                cleanPath(f"{path}/{i}")
            elif len(test) > 1 and test[-1] == " Asura Scans_files":
                for i in os.listdir(path):
                    if i == "google.webp" or i == "logo.webp":
                        send2trash.send2trash(f"{path}/{i}")
                    elif i.split(".")[-1] == "webp":
                        if i.find("_") != -1 & i.find("-") == -1:
                            if len(i.split("_")[0]) > 5:
                                    send2trash.send2trash(
                                        f"{path}/{i}")
                        elif len(i.split("-")[0]) > 5:
                            send2trash.send2trash(f"{path}/{i}")
                    else:
                        send2trash.send2trash(f"{path}/{i}")
            else:
                check(f"{path}");
                
            ''' 
                for i in os.listdir(path):
                    if i.split(".")[-1] in ["js", "css"]:
                        send2trash.send2trash(f"{path}/{i}")
                    elif i == "logo-chap.png":
                        send2trash.send2trash(f"{path}/{i}")
                    elif len(i.split("-")) > 1:
                        continue
                    else:
                        send2trash.send2trash(f"{path}/{i}")

            '''
        except OSError:
            pass

if __name__ == "__main__":
    cleanPath("./CC")
