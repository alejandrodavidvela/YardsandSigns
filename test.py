import os

directory = r'/Users/alexvela/Downloads/SignImage'
for filename in sorted(os.listdir(directory)):
    if filename.endswith(".png"):
        fileNameShort = os.path.join(filename[:-4])
        fileNameFull = os.path.join(filename)
        imgLineItem = '<img src="'+fileNameFull+'">'
        imgTitle = '<h1>'+fileNameShort+'</h1>'
        navLine = '<nav><a href="'+fileNameFull+'">'+fileNameShort+'</a><br><br></nav>'
        print(navLine)
    else:
        continue