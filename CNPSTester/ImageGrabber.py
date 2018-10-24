from PIL import ImageGrab
import time
from ctypes import windll

# figure out what machine dpi setting
user32 = windll.user32
user32.SetProcessDPIAware()

# grab image and scan it for colors (dump screenshot to directory)
timeStart = time.time()
image = ImageGrab.grab()
image.save("C:\\test\\testGrab.jpg", "JPEG")
for x in range(0, 3000, 10):
    for y in range(0, 2000, 10):
        color = image.getpixel((x, y))
print(time.time() - timeStart)