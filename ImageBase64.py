import base64
from pathlib import Path

loc = "D:\Ravi\eagle eye.png"      # Read file location; replace with your file path.

file_ext = Path(loc).suffix
with open(loc, "rb") as img_file:
    Base64string = base64.b64encode(img_file.read())

print("data:image/",file_ext,";base64",Base64string.decode('utf-8'))                     # Build prefix to Base64 for it to work in Power BI for e.r: data:image/jpeg;base64
                                                                                         # added decode('utf-8') to avoid prefix e.g: b'string' 
