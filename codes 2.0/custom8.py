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


# %%
# function to make slips with dsheet
def slip(num,cus,msg):
    img = Image.open('input/custom8.jpeg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('input/font/KGBlankSpaceSketch.ttf', 75)
    myFont1 = ImageFont.truetype('Arial', 50)
    myFont2 = ImageFont.truetype('input/font/futura_m.ttf', 40)
    nums = str(num)
    
    # to eliminate the empty names
    k = str(cus)
    if k == "nan":
        cus = "  "
    else:
        print()
    
    d1.text((750, 375),str(cus),(0,0,0),anchor="mm",font=myFont,align='centre')
    d1.text((1285, 90),"#"+nums,(0,0,0),font=myFont1,align='centre')
    d1.text((743, 151),str(msg),(0,0,0),anchor="mm",font=myFont2,align='centre')
   # img.show()
    img.save("output/images/"+nums+".jpg")
    
def slip1(num,cus,msg):
    img = Image.open('input/custom8.jpeg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('input/font/KGBlankSpaceSketch.ttf', 115)
    myFont1 = ImageFont.truetype('Arial', 50)
    myFont2 = ImageFont.truetype('input/font/futura_m.ttf', 40)
    nums = str(num)
    
    # to eliminate the empty names
    k = str(cus)
    if k == "nan":
        cus = "  "
    else:
        print()
    
    d1.text((750, 375),str(cus),(0,0,0),anchor="mm",font=myFont,align='centre')
    d1.text((1285, 90),"#"+nums,(0,0,0),font=myFont1,align='centre')
    d1.text((743, 151),str(msg),(0,0,0),anchor="mm",font=myFont2,align='centre')
   # img.show()
    img.save("output/images/"+nums+".jpg")


# %%


# %%
#without arguments

# single_name = 'Crazziee stuff'
# msg = 'with love from'
# nof = 21



msg = sys.argv[1]
single_name = sys.argv[2]
nof = int(sys.argv[3])


# %%


# %%
# #len(names[87])
# for i in range(nof):
#     print(single_name,1+i)

# %%


# %%
for i in range (nof):
    length = len(str(single_name))
    j = i+1
    if length>24:
        slip(j,single_name,msg)
        print("max",single_name,j)
    else:
        slip1(j,single_name,msg)
        print("mini",single_name,j)
print("Done")

# %%



