from PIL import Image,ImageFont,ImageDraw
import numpy as np
from pylab import *
# font = ImageFont.truetype('3.ttf',50)

from PIL import ImageDraw,Image
image = Image.open("D:\datasets\\train_datasets\\images\\9d7e0ada_5b7a_4c03_8dc2_a72f4e6fa6da.jpg") # 打开一张图片
# image = Image.open("D:\datasets\\train_datasets\\images\\0b9992c5_df33_4af3_8088_54259cf6a3fe.png") # 打开一张图片

draw = ImageDraw.Draw(image) # 在上面画画
# draw.rectangle([172.41,208.68,379.36,476], outline=(255,0,0) ,width=2) # [左上角x，左上角y，右下角x，右下角y]，outline边框颜色
# draw.text((172.41,208.68), 'person')
# draw.rectangle([173,311,203,349], outline=(255,0,0) ,width=2) # [左上角x，左上角y，右下角x，右下角y]，outline边框颜色
# draw.text((173,311), 'wrongglove')
# draw.rectangle([101.78,16.03,225,435], outline=(255,0,0) ,width=2) # [左上角x，左上角y，右下角x，右下角y]，outline边框颜色
# draw.text((101.78,16.03), 'operatingbar')
# draw.rectangle([279.05,47,294.32,229], outline=(255,0,0) ,width=2) # [左上角x，左上角y，右下角x，右下角y]，outline边框颜色
# draw.text((279.05,47), 'operatingbar')
# draw.rectangle([320,58,352,216], outline=(255,0,0) ,width=2) # [左上角x，左上角y，右下角x，右下角y]，outline边框颜色
# draw.text((320,58), 'operatingbar')
draw.rectangle([1964.22, 511.52, 1964.22+638.8599999999999, 511.52+1738.48], outline=(255,0,0) ,width=4) # [左上角x，左上角y，右下角x，右下角y]，outline边框颜色
draw.text((1964.22, 511.52), 'person')

image.save("drawed_image.png")
image.show() 
