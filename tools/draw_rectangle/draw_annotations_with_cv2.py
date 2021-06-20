import cv2
import matplotlib.pyplot as plt
piture_path='D:\datasets\\train_datasets\\images\\c44ed365_f51d_424c_ae8e_f935834ec9bd.jpg'
img=cv2.imread(piture_path)
plt.imshow(img)
plt.show()
x=[1485,1524,1879,1967]
y=[975,990,1603,1310]
z=[896.65,0,2243,4000]
a=(x[0],x[1])#(x1,y1)左上角
b=(x[0]+x[2],x[1]+x[3])#(x2,y2)右下角坐标
cv2.rectangle(img, a, b, (0, 255, 0), 2)
plt.imshow(img)
plt.show()
a='bus'#类别名称
b=0.9586#置信度
font=cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
imgzi = cv2.putText(img, '{} {:.3f}'.format(a,b), (420, 50), font, 0.5, (0, 255, 255), 1)
                # 图像，文字内容，坐标(右上角坐标) ，字体，大小，颜色，字体厚度
cv2.imwrite('./1.jpg',img)
plt.imshow(img)
plt.show()
