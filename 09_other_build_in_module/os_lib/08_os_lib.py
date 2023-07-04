# This file disscus of os module in python build in module


import os
import shutil
import send2trash

print(f">>> os.getcwd() -> getting preworking directory :\n{os.getcwd()}\n")
print(f">>> os.listdir() -> getting list directory at given path param :\n{os.listdir()}\n")
print(f">>> os.listdir('c://') -> getting list directory at given path param :\n{os.listdir('c://')}\n")

# shutil just work like shell command promt


# similar to $ mv [src] [dest]
try:
    shutil.move('movedtext.txt','./movehere')
except:
    pass

# deleting file with os lib
# os.unlink(path)
# os.rmdir(path)

# with shutil lib
# shutil.rmtree(path) # removing a tree from given path folder similar -> $ rm rf -r [path] 

# removing with os/shutil lib will permanently removed
# there are some lib will work like trash in my computer
# instal it with pip3 pip/pip3 in cmd
# $ pip3 install send2trash  

try:
    send2trash.send2trash('movedtext.txt')
except:
    pass


for folder, sub_folder,files in os.walk(os.getcwd()+'\\Example_Top_Level'):
    print(f"Currently in folder : {folder}\n")
    print("There is Sub folder :")
    for fol in sub_folder: # walking to sub folder
        print(f"\tSub folder : {fol}")
        
    print("There is file :")
    for fil in files:
        print(f"\tFile : {files}")