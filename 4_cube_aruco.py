import cv2
import numpy as np
from pynput import keyboard

# Load data after calibration
cv_file = cv2.FileStorage()
cv_file.open('./data/calibration/calib_cam.xml', cv2.FileStorage_READ)
camera_matrix = np.array(cv_file.getNode('K').mat(), dtype=np.float64)
dist_coeffs = np.array(cv_file.getNode('dist').mat(), dtype=np.float64)
cv_file.release()

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters_create()

# Define cube model
cube_size = 1
half = cube_size / 2
cube_faces = {
    "top": np.float32([[-half, -half, cube_size], [half, -half, cube_size], [half, half, cube_size], [-half, half, cube_size]]),
    "bottom": np.float32([[-half, -half, 0], [half, -half, 0], [half, half, 0], [-half, half, 0]]),
    "front": np.float32([[-half, -half, 0], [half, -half, 0], [half, -half, cube_size], [-half, -half, cube_size]]),
    "back": np.float32([[-half, half, 0], [half, half, 0], [half, half, cube_size], [-half, half, cube_size]]),
    "left": np.float32([[-half, -half, 0], [-half, half, 0], [-half, half, cube_size], [-half, -half, cube_size]]),
    "right": np.float32([[half, -half, 0], [half, half, 0], [half, half, cube_size], [half, -half, cube_size]])
}

cap = cv2.VideoCapture(0)

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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            # Estimate marker pose using cv2.aruco.estimatePoseSingleMarkers
            ### DO NOT DELETE THIS ###
            ### your code is here ###
            pass
            ### your code is here ###
            ### DO NOT DELETE THIS ###

            # Extract the marker corners (which are always returned in top-left, top-right, bottom-right, and bottom-left order)
            # Make sure that corners are in integer
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners.astype(int)

            # Draw the bounding box of the ArUCo detection
            cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

            # Project cube faces on marker using cv2.projectPoints
            ### DO NOT DELETE THIS ###
            ### your code is here ###
            pass

            # Draw cube wireframe
            pass
            ### your code is here ###
            ### DO NOT DELETE THIS ###

    cv2.imshow("Aruco cube", frame)
    cv2.waitKey(1)

    if terminate:
        break

cap.release()
cv2.destroyAllWindows()
