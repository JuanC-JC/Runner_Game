from PIL import Image,ImageOps


for i in range(1,16):
    x = Image.open("./Project_Game/Images/Player/Walk ({}).png".format(i))

    espejo = ImageOps.mirror(x)

    espejo.save("./Project_Game/Images/Player/Walk_Left ({}).png".format(i))
