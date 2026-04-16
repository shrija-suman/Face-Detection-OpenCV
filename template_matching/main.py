import cv2 as cv
import matplotlib.pyplot as plt

#importing the images
large_image=cv.imread('template_matching/group_photo.jpg',cv.IMREAD_COLOR)

# Convert the large image to grayscale for template matching
large_image_gray = cv.cvtColor(large_image, cv.COLOR_BGR2GRAY)

small_image=cv.imread('template_matching/Matching_image.jpg',cv.IMREAD_GRAYSCALE)

# Check if the images are loaded properly
if large_image is None or small_image is None:
    print("Error: Could not load images.")


#performing template matching
result=cv.matchTemplate(large_image_gray,small_image,cv.TM_CCOEFF_NORMED)

#getting the location for getting the the rectangle
min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
top_left=max_loc

#get the width,height of small_image so that we can draw rectangle
template_height,template_width=small_image.shape

#calculate bottam right of the rectangle
bottam_right=(top_left[0]+template_width,top_left[1]+template_height)

# Draw a rectangle around the matching region on the color image
cv.rectangle(large_image, top_left, bottam_right, (0,0,0), 2)

# Convert the BGR image (OpenCV default) to RGB for Matplotlip
large_image_rgb = cv.cvtColor(large_image, cv.COLOR_BGR2RGB)
    
    
# Display the result using Matplotlib
plt.imshow(large_image_rgb)
plt.title('Template Matching Result')
plt.show()



