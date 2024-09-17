# %%
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas as pd
import math
import numpy as np
import os
import sys






if not os.path.exists('output/images'):
   os.makedirs('output/images')





# %%

c_tag = str(sys.argv[1])
msg = sys.argv[2]


# %%
def slip(num,cus):
    img = Image.open('input/slip6_1.jpeg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('input/font/KGBlankSpaceSketch.ttf', 50)
    myFont1 = ImageFont.truetype('input/font/arial.ttf', 45)
    Font_tag = ImageFont.truetype('input/font/arial.ttf', 15)
    Font_msg = ImageFont.truetype('input/font/futura_m.ttf', 33)
    
    nums = str(num)
    
    # to eliminate the empty names
    k = str(cus)
    if k == "nan":
        cus = "  "
    else:
        print()
    
    d1.text((400, 300),str(cus),(0,0,0),anchor="mm",font=myFont)
    d1.text((655, 50),"#"+nums,(0,0,0),font=myFont1,align='centre')
    d1.text((380, 30),"#"+c_tag,(0,0,0),font=Font_tag,align='centre')
    d1.text((402, 115),str(msg),(0,0,0),anchor="mm",font=Font_msg,align='centre')
    
    
    
   # img.show()
    img.save("output/images/"+nums+".jpg")

def slip1(num,cus):
    img = Image.open('input/slip6_1.jpeg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('input/font/KGBlankSpaceSketch.ttf', 40)
    myFont1 = ImageFont.truetype('input/font/arial.ttf', 45)
    Font_tag = ImageFont.truetype('input/font/arial.ttf', 15)
    Font_msg = ImageFont.truetype('input/font/futura_m.ttf', 33)
    
    
    nums = str(num)
    
    # to eliminate the empty names
    k = str(cus)
    if k == "nan":
        cus = "  "
    else:
        print()
    
    d1.text((400, 300),str(cus),(0,0,0),anchor="mm",font=myFont)
    d1.text((655, 50),"#"+nums,(0,0,0),font=myFont1,align='centre')
    d1.text((380, 30),"#"+c_tag,(0,0,0),font=Font_tag,align='centre')
    d1.text((402, 115),str(msg),(0,0,0),anchor="mm",font=Font_msg,align='centre')
    
   # img.show()
    img.save("output/images/"+nums+".jpg")

def slip2(num,cus):
    img = Image.open('input/slip6_1.jpeg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('input/font/KGBlankSpaceSketch.ttf', 35)
    myFont1 = ImageFont.truetype('input/font/arial.ttf', 45)
    Font_tag = ImageFont.truetype('input/font/arial.ttf', 15)
    Font_msg = ImageFont.truetype('input/font/futura_m.ttf', 33)
    
    nums = str(num)
    
    # to eliminate the empty names
    k = str(cus)
    if k == "nan":
        cus = "  "
    else:
        print()
    
    d1.text((400, 300),str(cus),(0,0,0),anchor="mm",font=myFont)
    d1.text((655, 50),"#"+nums,(0,0,0),font=myFont1,align='centre')
    d1.text((380, 30),"#"+c_tag,(0,0,0),font=Font_tag,align='centre')
    d1.text((402, 115),str(msg),(0,0,0),anchor="mm",font=Font_msg,align='centre')
    
   # img.show()
    img.save("output/images/"+nums+".jpg")

# %%


# %%
df = pd.read_csv('output/dsheet.csv', index_col = [0])

# %%


# %%
# %%
names = df["Names"].tolist()
nums = df.index.tolist()

# %%
#len(names[87])
#for i in range(len(nums)):
#   print(len(str(names[i])),names[i],nums[i])

# %%


# %%


# %%
for i,j in zip(names,nums):
    lenght = len(str(i))
    if lenght<24:
        slip(j,i)
        print(j,i)
    elif lenght<27:
        slip1(j,i)
        print(j,i)
    else:
        slip2(j,i)
        print(j,i)

print("Done")

# %%


# %%



