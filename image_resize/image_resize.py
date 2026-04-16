import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image_resize/City.jpg')
h, w, c = img.shape
print(f"Height and width of original image: {h}, {w}" )

# resize the image
new_size = (700, 900) # new_size=(width, height)
print(f"New height and width: {new_size[1]}, {new_size[0]}" )
resize_img = cv2.resize(img, new_size)

# Convert the images from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
resize_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img), plt.title("Original Image")
plt.subplot(122), plt.imshow(resize_img), plt.title("Resized Image")
plt.show()