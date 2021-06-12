import os

file=r"F:/Hexo/HexoBlog/Hexo/source/live2d-widget/waifu-tips.js"
live2DPath=r"F:/Hexo/HexoBlog/Hexo/source/live2D/"
defaultName="22"


live2dFiles= os.listdir(live2DPath)
for live2d in live2dFiles:
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        # print(f.read())
        file_data=(f.read().replace("/"+defaultName+"/","/"+live2d+"/"))
        print("    更换为："+live2d)
        defaultName=live2d
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
    key=input("按回车更换")
        # for line in f:
        #     if old_str in line:
        #     line = line.replace(old_str,new_str)
        #     file_data += line
    # with open(file,"w",encoding="utf-8") as f:
    # f.write(file_data)