import cv2
img1 = cv2.imread("D:\\GET Training\\raj.jpg")

#Reading img from a path
#path=input("Enter your img path=") #directly read img from the path
#img1=cv2.imread(path,0) #reading img from the path & converting to grayscale

#img1 = cv2.imread("D:\\GET Training\\raj.jpg",0) #for black & white
#img1 = cv2.imread('D:\\GET Training\\raj.jpg',-1) #high contrast image

#Rotating the img
#img1=cv2.flip(img1,0) #Accepts -1,0,1

#Resizing
img1=cv2.resize(img1,(1280,1080))

#Printing
print(img1)
cv2.imshow("original",img1) #to see the image

cv2.waitKey() #by default it is 0
#cv2.waitKey(3000) #image display will appear for 3 sec

cv2.destroyAllWindows()

#saving the image
#k=cv2.waitKey() #assigning variable to waitkey
#if k==ord("s"): #if pressing s then it will save
 #   cv2.imwrite("D:\\Raj.png",img1) #mentioning the location with file name and extension
#else:
 #   cv2.destroyAllWindows 
