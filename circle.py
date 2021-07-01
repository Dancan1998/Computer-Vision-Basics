import numpy as np
import cv2

#VARIABLES
#True while mouse button down, False while mouse button up
drawing = False
ix,iy = -1,-1

#FUNCTION
def draw_circle(event, x, y, flags, params):
    global ix,iy,drawing
    
    if event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        cv2.circle(img2, (x,y), 60, (0,0,255), -1)
        
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             cv2.circle(img, (x,y), 100, (0,0,255), -1)
            
#     elif event == cv2.EVENT_RBUTTONUP:
#         drawing = False
#         cv2.circle(img, (x,y), 100, (0,0,255), -1)

#SHOWING THE IMAGE
img2 = cv2.imread('DATA/dog_backpack.jpg')
cv2.namedWindow(winname='my_image')
cv2.setMouseCallback('my_image', draw_circle)

while True: 
    cv2.imshow('my_image', img2)
    
    #checks for esc key 
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()