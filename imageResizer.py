import os
from PIL import Image

if __name__ == "__main__":
    for i in os.listdir("originalImages"):
        print(i)
        for j in os.listdir("originalImages/" + i):
            # print ("\t-" + j)
            fileExtension = j.split('.')[1]
            if fileExtension != "gif":
                imageFile = "originalImages/" + i + "/" + j
                print(imageFile)
                # try:
                originalImg = Image.open(imageFile)
                print(originalImg)
                print(originalImg.size)
                width = originalImg.size[0]
                height = originalImg.size[1]
                wider = True if (width > height) else False
                print(height)
                if wider:
                    newWidth = 700
                    newHeight = newWidth * (height / width)
                else:
                    newHeight = 700
                    newWidth = newHeight * (width / height)
                smallerImg = originalImg.resize((int(newWidth), int(newHeight)), Image.ANTIALIAS)
                if not os.path.exists("images/"):
                    os.makedirs("images/")
                if not os.path.exists("images/" + i):
                    os.makedirs("images/" + i)
                smallerImg.save("images/" + i + "/" + j)
            # except:
                # print("Can't load image")