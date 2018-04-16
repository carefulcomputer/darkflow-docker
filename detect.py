#!/usr/bin/env python
from darkflow.net.build import TFNet
import cv2
import tensorflow as tf
import numpy as np
import datetime

options = {"model": "/cfg/yolo.cfg", "load": "./yolo.weights",  "threshold": 0.3}

tfnet = TFNet(options)
username = "username"
password = "pass"
minHight = 100
minWidth = 50

count = 0

# garage streamid = 3, inside = 2
def processStream(streamId):
    while True:
        starttime = datetime.datetime.now()
        cam = cv2.VideoCapture("rtsp://" + username + ":" + password + "@192.168.1.1:554/cam="+ str(streamId))
        if not cam.isOpened():
              raise IOError('Can\'t open video')
    	if cv2.waitKey(25) & 0xFF == ord('q'):
              break
        ret, frame = cam.read(cv2.CAP_PROP_POS_FRAMES)
    	cam.release()
        if not ret:
            print('Can\'t read video data. Potential end of stream')
            break

        curr_img_cv2 = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR) #is the frame good and can be opened?
        result = tfnet.return_predict(curr_img_cv2)
        print(result)
        print("----------")
        persons = [entry for entry in result if entry["label"] == "person"]
        print("Total persons are %d " % len(persons))
        
        processDetectionResults(persons, curr_img_cv2)

        endtime = datetime.datetime.now()
        print("time is %d" % (endtime - starttime).microseconds)
        print("-------------------------")

    cv2.destroyAllWindows()
#------------------------------------------------
# draw each person on image and save it along with original
def processDetectionResults(persons, img):
    global count
    if len(persons) > 0:
        imgCopy = img.copy()
        for person in persons:
            drawBoxes(person, imgCopy);
        count += 1    
        cv2.imwrite("/images/Frame%dOriginal.jpg" % count, img)    
        cv2.imwrite("/images/frame%dDetected.jpg" % count, imgCopy)

#------------------------------------------------
# draw boxes on result if they are above certain size
def drawBoxes(result, img):
    # check if size is above minimum
    if ((result["bottomright"]["y"] - result["topleft"]["y"]) > minHight) and ((result["bottomright"]["x"] - result["topleft"]["x"]) > minWidth): 
        # if yes then add rectangle to image
        cv2.rectangle(img, \
                  (result["topleft"]["x"], result["topleft"]["y"]), \
                  (result["bottomright"]["x"], \
                   result["bottomright"]["y"]), \
                  (0, 255, 0), 2)
        # find place for text label
        text_x, text_y = result["topleft"]["x"] - 10, result["topleft"]["y"] - 10 

        # put text label on image 
        cv2.putText(img, result["label"] + "," + str(result["confidence"]), (text_x, text_y), \
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

#------------------------------------------------
processStream(3)

