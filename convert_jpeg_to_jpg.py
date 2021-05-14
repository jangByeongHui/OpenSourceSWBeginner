from PIL import Image
import glob

for filename in glob.iglob('C:/Users/JangByeongHui/Desktop/img/*.jpeg', recursive=True):
    
    im=Image.open(filename).convert("RGB")
    filename=filename.replace("JPEG","JPG")
    im.save(filename)