import cv2 
import numpy as np





#320x240
image = cv2.imread("Example2.jpeg")

#cv2.imshow('image', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()




b = image[:,:,2]
g = image[:,:,1]
r = image[:,:,0]



#Possible Problem Here, play with the thresholds and see if you can get something a little better
blue = ((b[:,:] - r[:,:] > 40) & (b[:,:] - g[:,:] > 10))
blue_only = image;

#Note that 319 and 239 are in reference to the size of the image
for i in range(319):
    for j in range(239):
        if blue[j,i] == False:
            blue_only[j,i,0] = 0
            blue_only[j,i,1] = 0
            blue_only[j,i,2] = 0



cv2.imshow("blue only", blue_only)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Next step will involve connected components and possibly erosion and dilution
#I need to find a way to convert blue_only into grayscale before I can make it binary
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#You need to choose 4 or 8 for connectivity type
connectivity = 8  
#Perform the operation
output = cv2.connectedComponentsWithStats(gray, connectivity, cv2.CV_32S)
#Get the results
#The first cell is the number of labels
num_labels = output[0]
# The second cell is the label matrix
labels = output[1]
# The third cell is the stat matrix
stats = output[2]
# The fourth cell is the centroid matrix
centroids = output[3]

print(labels)
    
