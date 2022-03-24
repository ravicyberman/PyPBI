import base64
with open("D:\Ravi\eagle eye.png", "rb") as img_file:
    Base64string = base64.b64encode(img_file.read())
print(Base64string)