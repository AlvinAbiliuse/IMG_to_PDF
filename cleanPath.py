#! /usr/bin/python3

import os
import send2trash


path = os.listdir("./")[0]

def cleanPath(path):
    test = path.split("-");
    print(f"Cleaning {path} \n")
    for i in os.listdir(path):
        if os.path.isdir(f"{path}/{i}") == True:
            trial(f"{path}/{i}")
        elif len(test) > 1 and test[-1] == " Asura Scans_files":
            for i in os.listdir(path):
                if i == "google.webp" or i == "logo.webp":
                    send2trash.send2trash(f"{path}/{i}")
                elif i.split(".")[-1] == "webp":
                    if len(i.split("-")[0]) > 5:
                        send2trash.send2trash(f"{path}/{i}")
                else:
                    send2trash.send2trash(f"{path}/{i}")
        else:
            for i in os.listdir(path):
                if i.split(".")[-1] in ["js", "css"]:
                    send2trash.send2trash(f"{path}/{i}")
                elif i == "logo-chap.png":
                    send2trash.send2trash(f"{path}/{i}")
                elif len(i.split("-")) > 1:
                    continue
                else:
                    send2trash.send2trash(f"{path}/{i}")

if __name__ == "__main__":
    for i in os.listdir("./CC"):
        if i.split(".")[-1] == "html":
            send2trash.send2trash(f"./CC/{i}")
        else:
            cleanPath(f"./CC/{i}")
