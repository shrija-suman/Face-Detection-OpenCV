import cv2
import os
from datetime import datetime
save_dir ='selfies'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret,frame=cap.read()
    if not ret:
        print("Cannot access the frame.")
        break
    cv2.imshow('Selfie capture',frame)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
    if key==ord('c'):
        now=datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"{save_dir}/selfie_{timestamp}.png"
        cv2.imwrite(filename,frame)
        print(f'Selfie saves as{filename}')

cap.release()
cv2.destroyAllWindows()