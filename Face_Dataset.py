
#To Gather Dataset of person to detect


import cv2
                                                                    # error: (-215) !empty() in function detectMultiScale
                                                                    #face_cascade .xml file not reading properly
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('Cascades\\haarcascade_frontalface_alt.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read()
    faces = face_detector.detectMultiScale(img, 1.3, 5)
   # faces = face_detector.detectMultiScale(
    #    img,
     #   scaleFactor=1.2,
     #   minNeighbors=5
    #)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite('dataset\\User.' + str(face_id) + '.' + str(count) + ".jpg", img[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()