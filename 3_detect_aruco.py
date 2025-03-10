import cv2
import numpy as np
from pynput import keyboard

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters_create()

cap = cv2.VideoCapture(1)

# Define resolution of your web-camera
width = 1920
height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))

save = False
terminate = False


def on_key_press(key):
    global save, terminate
    if key == keyboard.Key.shift:
        print("Image saved!")
        save = True
    if key == keyboard.Key.esc:
        print("###### TERMINATE APPLICATION ######")
        terminate = True


listener = keyboard.Listener(on_press=on_key_press)
listener.start()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect aruco marker with cv2.aruco.detectMarkers (make sure to convert frame to grayscale beforehand)
    ### DO NOT DELETE THIS ###
    ### your code is here ###
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.aruco.detectMarkers()
    ### your code is here ###
    ### DO NOT DELETE THIS ###

    if len(corners) > 0:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            # Extract the marker corners (which are always returned in top-left, top-right, bottom-right, and bottom-left order)
            # Make sure that corners are in integer
            ### DO NOT DELETE THIS ###
            ### your code is here ###
            corners= None
            pass
            ### your code is here ###
            ### DO NOT DELETE THIS ###

            # Draw the bounding box of the ArUCo detection
            ### DO NOT DELETE THIS ###
            ### your code is here ###
            pass
            ### your code is here ###
            ### DO NOT DELETE THIS ###

    cv2.imshow("Aruco cube", frame)
    cv2.waitKey(1)

    if terminate:
        break

cap.release()
cv2.destroyAllWindows()
