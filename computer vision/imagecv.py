import requests
import os
import numpy as np
import cv2 #To insatll library in memeory
def download_image(url, name="image.png"):
    if os.path.exists(name):
        return 
    response = requests.get(url)
    with open(name, "wb") as f:
        f.write(response.content)

url="https://imgsrv.crunchyroll.com/cdn-cgi/image/format=auto,width=480,height=720,fit=contain,quality=85/catalog/crunchyroll/095217fdb4f228410df09b18f151be28.jpe"
download_image(url, "spyxfamily.jpg")



im =cv2.imread("spyxfamily.jpg")
#to print resized version
#im2 = cv2.resize(im2, (400, 500)) resolution given manually
im2 = cv2.resize(im,(0,0), fx=0.75, fy=0.5 ) #resolution given by factor
# print(im) to print full matrix display
#print(im.shape) #to print its shape

bwim =cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
#to see image
# cv2.imshow("spyxfamily", im2)
# cv2.imshow("spyxfamily BW", bwim)

#to concatenate both images
both = np.concatenate((im2, cv2.cvtColor(bwim, cv2.COLOR_GRAY2BGR)), axis=0)
#for both their shapes
print(both.shape)
#to write text in images
cv2.putText(both, "original", (30,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2) #0.5 scale, 2 is for thickness
cv2.putText(both, "copied", (30,40+380), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0), 2)
#to put a rectangle in between the images.
cv2.rectangle(both, (180-100,360-100), (180+100,360+100), (0,255,0), 2)
cv2.imshow("Spyxfamily", both)
cv2.waitKey(0)
