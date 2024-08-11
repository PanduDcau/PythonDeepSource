from roboflow import Roboflow
import cv2
import uuid
#import Uuid for random number generate

import random
# Generate a random three-digit number
random_id = str(random.randint(100, 999))

# Use the random number as the image name prefix
image_name = f"predictions_{random_id}.jpg"


rf = Roboflow(api_key="ppa")
project = rf.workspace().project("pepper-segmentation")
model = project.version(1).model

# infer on a local image
response = model.predict("images/pp7.JPG", confidence=38, overlap=30).json()

pepper = 0
papaw = 0
for pred in response['predictions']:
    print(pred['class'])
    if pred['class'] == 'pepper':
        pepper += 1
    if pred['class'] == 'papaw':
        papaw += 1
print("Number of Pepper Seeds \t" + str(pepper))

print("Number of Papaw Seeds \t" + str(papaw))

# visualize your prediction
model.predict("images/pp66.JPG", confidence=35, overlap=30).save(f"prediction/{image_name}")
print(f"prediction/{image_name}")

pred_image = cv2.imread(f'prediction/{image_name}', 1)
imS = cv2.resize(pred_image, (900, 750))
cv2.imshow('color image', imS)

# Waits for a keystroke
cv2.waitKey(0)
# Destroys all the windows created
cv2.destroyAllwindows()

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
