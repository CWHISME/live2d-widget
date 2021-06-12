import os

dirPath=r"F:/Hexo/HexoBlog/Hexo/source/live2D/"

paths=os.listdir(dirPath)
for path in paths:
    childPath= os.path.join(dirPath,path)
    if os.path.isdir(childPath):
        for file in os.listdir(childPath):
            if file.endswith("model.json"):
                print(file)
                os.rename(os.path.join(childPath,file),os.path.join(childPath,"index.json"))