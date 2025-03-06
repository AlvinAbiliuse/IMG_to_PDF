#! /usr/bin/python3

import os
import send2trash


path = os.listdir("./")[0]

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
                for i in os.listdir(path):
                    if i.find(".webp"):
                        continue
                    elif i.split(".")[-1] in ["js", "css"]:
                        send2trash.send2trash(f"{path}/{i}")
                    elif i == "logo-chap.png":
                        send2trash.send2trash(f"{path}/{i}")
                    elif len(i.split("-")) > 1:
                        continue
                    else:
                        send2trash.send2trash(f"{path}/{i}")
        except OSError:
            pass
if __name__ == "__main__":
    cleanPath("./CC")
