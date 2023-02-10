import cv2
import numpy as np
from matplotlib import pyplot as plt 

image1 = cv2.imread('/home/sk/Desktop/first.jpg',0)
image2 = cv2.imread('/home/sk/Desktop/first.jpg',1)
image3 = cv2.imread('/home/sk/Desktop/first.jpg',2)

channel = image2.shape[2]
imgSize = image1.size
print("channel = {0}".format(channel))

BLUE = [255,0,0]
replicate = cv2.copyMakeBorder(image1,10,10,10,10,cv2.BORDER_REPLICATE)  
reflect = cv2.copyMakeBorder(image1,10,10,10,10,cv2.BORDER_REFLECT)  
reflect101 = cv2.copyMakeBorder(image1,10,10,10,10,cv2.BORDER_REFLECT_101)  
wrap = cv2.copyMakeBorder(image1,10,10,10,10,cv2.BORDER_WRAP)  
constant= cv2.copyMakeBorder(image1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE) 


plt.subplot(231),plt.imshow(image1,'gray'),plt.title('ORIGINAL')  
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')  
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')  
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')  
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')  
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')  
plt.show() 
# num1 = 10
# num2  = 10
# print(num1)
# c = num1 + num2
# print(c)
# if num1 == num2:
#     print("1st it")
#     if (c > num2):
#         print("{0} is gretwer than {1}".format(c, num2))
#     else:print("aother it")
# else:
#     print("2nd it")

#Image Compare
# if (image1 == image2).any():
#     print("images mached")

cv2.imshow("show",image1,)
pixel = image1[100,100]
print(pixel)

cv2.waitKey(20000)
cv2.destroyAllWindows()
print("shape is {0} . hieght = {1} width = {2} ".format(image1.shape,image1.shape[0],image1.shape[1]))

status = cv2.imwrite('/home/shashi/Desktop/firstcopy.jpg',image1)
print(status)
b,g,r = cv2.split(image2)
print(b)
image1 = cv2.merge((b,g,r))
cv2.imshow("merged",image1)
cv2.waitKey(100000)