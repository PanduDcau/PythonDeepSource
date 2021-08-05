#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pytesseract #importing Terssarct Plugin for identify text from the 


# In[2]:


print(pytesseract.__version__) 


# In[2]:


import cv2 #pip install open-cv Python


# In[4]:


print(cv2.__version__)


# In[5]:


import matplotlib.pyplot as plt


# # Let's Do Configuration 

# In[3]:


#Redirecting the tesseract file Path for use the Define Libraries
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# In[4]:


#Image Read from the Given Path
img = cv2.imread('/Users/Asus/Documents/Atmel Studio/noun.png') 


# In[8]:


#Displaying the Image that Addressed
plt.imshow(img)


# In[9]:


#Creating Boxes for the Letters in the image
imgbox=pytesseract.image_to_boxes(img)


# In[10]:


type(imgbox)


# In[11]:


#The Matrix representation of the Image 
print(imgbox)


# In[12]:


#Parameters to find the Dimention of the Images
imgH, imgW,_ = img.shape


# # Identify the Characters using Image Boxes

# In[13]:


#Show Casing the image dimention
img.shape


# In[14]:


#Iterative Process for Create boxes in the Image
for boxes in imgbox.splitlines():
     boxes = boxes.split(' ')
     x,y,w, h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
     cv2.rectangle(img, (x,imgH-y) , (w,imgH-h), (0,0,255),3)


# In[15]:


plt.imshow(img) #Default Shows cv2=> In BGR


# In[16]:


#Converting to RGB image Format
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


# # Without Using Noice Reduction and Edge Detection in the Image (No Filters)

# In[17]:


#Converting identified boxes into text Representation
im3char=pytesseract.image_to_string(img)
print(im3char)


# # Handwritten Letter Detection With Enhancing the Quality of Image

# ## Without Using Any Filters in the Images

# In[5]:


#Creating boxes in the image to identify text 
h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img2 = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)


# In[6]:


#Another Image 
img2 = cv2.imread('/Users/Asus/Documents/Atmel Studio/Batman.jpg')


# In[7]:


#Same Procedure used to create Boxes in text on the Image
h, w, c = img2.shape
boxes = pytesseract.image_to_boxes(img2) 
for b in boxes.splitlines():
    b = b.split(' ')
    img2 = cv2.rectangle(img2, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('image', img2)
cv2.waitKey(0)


# In[21]:


#Creating the Images 
im2char=pytesseract.image_to_string(img2)


# # Without Applying Any Filters in the Image

# In[22]:


print(im2char)


# # Modify the Image using Filters and Noice Reduction

# In[8]:


import cv2
import numpy as np

image = cv2.imread('/Users/Asus/Documents/Atmel Studio/noun.jpg')

#Run the Program each time for text recaputuring process form the Image

# OpenCv function to get grayscale image
def get_grayscale(image):                    
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #This Function in OpenCV2 Provides to get GrayScale 

# noise removal in Given Image
def remove_noise(image):
    return cv2.medianBlur(image,5) #Removing Noice in the Picture is Way more Important 
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotation = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotation

#template matching
#def match_template(image, template):
  #return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 


# In[9]:


#Using the Filterring Options and Noice Reduction to Identify the texts Clearly
image = cv2.imread('/Users/Asus/Documents/Atmel Studio/Sinhala.jpg')

gray = get_grayscale(image) #Converting Image to a GrayScale Image
thresh = thresholding(gray) #Binary Thresholding Apply for the GrayScale Image
opening = opening(gray)
canny = canny(gray) #Canny Filtering used for the GrayScale Image

language_Config = r'-l sin --psm 6' #Addressing the realted text library in Terreract

#Converting image Matrix into Text Format
image_char=pytesseract.image_to_string(image,config=language_Config)
print(image_char)


# In[40]:


#Run the Filtering Functions 1st
#Using the Filterring Options and Noice Reduction to Identify the texts Clearly
image4 = cv2.imread('/Users/Asus/Documents/Atmel Studio/SinhalaHand.jpg')

gray = get_grayscale(image4) #Converting Image to a GrayScale Image
thresh = thresholding(gray) #Binary Thresholding Apply for the GrayScale Image
opening = opening(gray)
canny = canny(gray) #Canny Filtering used for the GrayScale Image

language_Config = r'-l sin --psm 6' #Addressing the realted text library in Terreract

#Converting image Matrix into Text Format
image_char=pytesseract.image_to_string(image4,config=language_Config)  #WIth the Limitations of the Tesseract Libraries some 
print(image_char)


# In[27]:


#Run the Filter Functions 1st and then Run this Segment
#Using the Filterring Options and Noice Reduction to Identify the texts Clearly
image3 = cv2.imread('/Users/Asus/Documents/Atmel Studio/EngWrite.jpg')

gray = get_grayscale(image3) #Converting Image to a GrayScale Image
thresh = thresholding(gray) #Binary Thresholding Apply for the GrayScale Image
opening = opening(gray)
canny = canny(gray) #Canny Filtering used for the GrayScale Image

#language_Config = r'-l sin --psm 6' #Addressing the realted text library in Terreract

#Converting image Matrix into Text Format
image_char=pytesseract.image_to_string(image3)
print(image_char)

#Represent the Digits in the Image

print("Digits in the Image Respectively:-")
digit_represent = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(image3, config=digit_represent))


# In[107]:


#Reading the Image using OpenCv
#Using the Filterring Options and Noice Reduction to Identify the texts Clearly
#Compile the Function code above before interpret this Segment
image = cv2.imread('/Users/Asus/Documents/Atmel Studio/batman.jpg')


gray = get_grayscale(image) #Converting Image to a GrayScale Image
thresh = thresholding(gray) #Binary Thresholding Apply for the GrayScale Image
opening = opening(gray)
canny = canny(gray)  #Canny Filtering used for the GrayScale Image

#Converting image Matrix into Text Format
image_char=pytesseract.image_to_string(image)
print(image_char)

#Represent the Digits in the Image

print("Digits in the Image Respectively:-")
digit_represent = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(image, config=digit_represent))

print("Characters in the Document Respectively :-")
char_config = r'-c tessedit_char_blacklist=0123456789 --psm 6'
pytesseract.image_to_string(image, config=char_config)


# In[29]:


#Second Example with Appling filters and Noice Reduction
image = cv2.imread('/Users/Asus/Documents/Atmel Studio/noun.png')

gray = get_grayscale(image)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)
Noice = remove_noise(gray)
dil= dilate(gray)

image_char=pytesseract.image_to_string(image)
print(image_char)


print("Digits in the Image Respectively:-")
digit_represent = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(image, config=digit_represent))

print("Characters in the Document Respectively :-")
char_config = r'-c tessedit_char_blacklist=0123456789 --psm 6'  #Blacklisting the digits in the Document
pytesseract.image_to_string(image, config=char_config)


# # Let's Work On Multi-Laguage Texts

# In[92]:


img4 = cv2.imread('/Users/Asus/Documents/Atmel Studio/Spanish.png')


# ## Identifying the Language Resides in the Photo

# In[108]:


#Displaying the Image that Addressed
plt.imshow(img4)


# In[109]:


#Creating Boxes for the Letters in the image
imgbox2=pytesseract.image_to_boxes(img4)


# In[110]:


#Iterative Process for Create boxes in the Image
for boxes in imgbox2.splitlines():
     boxes = boxes.split(' ')
     x,y,w, h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
     cv2.rectangle(img4, (x,imgH-y) , (w,imgH-h), (0,0,255),3)


# In[111]:


#Converting to RGB image Format
plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))


# In[112]:


#Identify text in the image and return laguage Precentages
text_trans = r'-l spa+sin --psm 6' #From tesseract Library you can find the languages reside in the project
translatetxt = pytesseract.image_to_string(img4, config=text_trans)

from langdetect import detect_langs
detect_langs(translatetxt )


# ## Segregating the Digits from the Text Photo

# In[96]:


#Above img4's Digits Segregated Seperately
digit_represent = r'--oem 3 --psm 6 outputbase digits'   #Tesseract Syntax to whitelisting the Digits only
print(pytesseract.image_to_string(img4, config=digit_represent))


# ## Text Recognition in a Video 

# In[11]:


import numpy as np
font_scale = 1.5  #Providing Text size
font = cv2.FONT_HERSHEY_PLAIN #Open CV Font Type

#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture("/Users/Asus/Documents/Atmel Studio/Message.mp4") #Importing the Video 

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IDError("Cannot Open WebCam")
ct =0;

#Until the Video is Over Capturing the letters in the Clip
while True:
    ret, frame = cap.read()
    ct= ct+1;
    #Capture the 40 frames per the Second
    if((ct%40)==0):     
        imgH, imgW,_ = frame.shape
        
        x1,y1,w1,h1 = 0,0,imgH,imgW
         
        imgchar= pytesseract.image_to_string(frame) #Creating the Image's text represenation into text
        
        #Draw The Boxes  
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes=boxes.split(' ')
            x,y,w,h = int(boxes[1]), int(boxes[2]) ,int(boxes[3]) ,int(boxes[4])
            cv2.rectangle(img, (x,imgH-y) , (w,imgH-h), (255,0,0),3)
            
        cv2.putText(frame,imgchar, (x1 + int(w1/50), y1 + int (h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        #Draw the Images
        
        font= cv2.FONT_HERSHEY_SIMPLEX 
        
        
        
        cv2.imshow("Text Detection", frame) #Detected boxes with letters will be printed in top of the Video
        
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
        


# In[ ]:




