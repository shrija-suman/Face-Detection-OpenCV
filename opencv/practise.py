import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#paint the image of certaing color

  #blank[0:500,0:500]=0,255,0 #red green blue
  #cv.imshow('Green',blank)

#creating rectangle or square

  #cv.rectangle(blank,(0,0),(250,250),color=(0,255,0) , thickness=cv.FILLED)
   #if we do thickness=cv.FILLED then that color will fill in that rectangle or square
  #cv.imshow('Rectangle',blank)

#creating circle

  #cv.circle(blank,(250,250),radius=0,color=(255,0,0),thickness=3)
  #cv.imshow('Circle',blank)

#creating line

  #cv.line(blank,(0,250),(250,250),color=(255,255,255),thickness=2)
  #cv.imshow('Line',blank)

#creating text

  #cv.putText(blank,'Hello..myself Dimpy',(0,250),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255),thickness=2)
  #cv.imshow('Text',blank)

cv.waitKey(0)